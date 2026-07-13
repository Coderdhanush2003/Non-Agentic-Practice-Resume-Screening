from fastapi import APIRouter, UploadFile, File, Form
from google import genai
from google.genai import types
import os
import json
from dotenv import load_dotenv
from schemas import ScreeningResponse

load_dotenv()

key = os.getenv("GEMINI_RESUME_SCREENING_API")
router = APIRouter()
client = genai.Client(api_key=key)

@router.post('/screen')
async def resume_screening(file: UploadFile | None = None, job_description: str = Form(...)):

    async def user_resume_extraction():
        file_bytes = await file.read()
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                types.Part.from_bytes(data=file_bytes, mime_type="application/pdf"),
                "Extract all professional skills listed in this resume."
            ]
        )
        return response.text
    
    def job_description_extraction():
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Extract all professional skills listed in this Job Description: {job_description}"
        )
        return response.text
    
    def screening_test(user_skills, job_role):
        prompt = (
            f"Analyze the candidate's eligibility for the position.\n\n"
            f"Job Description Skills: {job_role}\n"
            f"Candidate Skills: {user_skills}\n\n"
            f"Provide a status (e.g., 'Not Selected', 'Shortlisted', 'Review Required'), "
            f"the final match percentage as an integer, and a detailed markdown feedback reason summarizing where they lack requirements in maximum 2 to 3 sentence."
        )
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ScreeningResponse,
            ),
        )
        return response.text
    
    user_skills = await user_resume_extraction()
    job_role = job_description_extraction()
    screening_results_str = screening_test(user_skills, job_role)

    print(screening_results_str)

    return json.loads(screening_results_str)
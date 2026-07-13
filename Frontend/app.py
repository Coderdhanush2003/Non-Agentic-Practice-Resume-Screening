import streamlit as st
import requests

st.title("Resume Screening App")

# Added Job Description field because your backend requires it
job_description = st.text_area("Enter the Job Description here:")
uploaded_file = st.file_uploader("Upload a resume (PDF)", type="pdf")

if uploaded_file is not None and job_description:
    st.write("File uploaded successfully!", uploaded_file.name)

    if st.button("Process Resume"):
        with st.spinner("Screening resume..."):
            # Construct the payload matching backend expected Form/File types
            files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
            data = {"job_description": job_description}

        
            try:
                response = requests.post(
                    "http://localhost:8000/screen", # Removed trailing slash to match typical FastAPI setups
                    files=files,
                    data=data
                )
                
                if response.status_code == 200:
                    st.success("Resume processed successfully!")
                    response_data = response.json()
                    
                    # Display structured output safely
                    st.subheader("Results")
                    st.write(f"**Candidate Status:** {response_data.get('candidate_status')}")
                    st.write(f"**Skills Matched:** {response_data.get('skill_match_percentage')}%")
                    st.write(f"**Feedback:** {response_data.get('reason')}")
                    
                else:
                    st.error(f"Backend Error ({response.status_code}): {response.text}")
            except requests.exceptions.ConnectionError:
                st.error("Could not connect to backend server. Make sure FastAPI is running on port 8000.")
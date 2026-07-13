from pydantic import BaseModel

class ScreeningResponse(BaseModel):
    candidate_status: str
    skill_match_percentage: int
    reason: str

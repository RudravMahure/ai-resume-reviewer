from pydantic import BaseModel

class ResumeReview(BaseModel):
    overall_score: int
    ats_score: int
    summary: str
    strengths: list[str]
    weaknesses: list[str]
    suggestions: list[str]
    
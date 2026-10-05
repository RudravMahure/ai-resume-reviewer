from google import genai

from config import GEMINI_API_KEY
from models import ResumeReview
from prompts import RESUME_REVIEW_PROMPT

import time

client = genai.Client(api_key=GEMINI_API_KEY)

def review_resume(resume_text):
    
    try:
        prompt = RESUME_REVIEW_PROMPT.format(
            resume_text = resume_text
        )    
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt,
            config={
                "response_mime_type":"application/json",
                "response_schema":ResumeReview
            }
        )
        return ResumeReview.model_validate_json(response.text)
    except Exception as e:
            if "503" in str(e):
                print("Model is temporarily unavailable. Retrying...")
                time.sleep(5)
            else:
                raise e

    raise Exception("Model is still unavailable after multiple retries.") 
from pydantic import BaseModel



class VerifySessionPayload(BaseModel):
    session_token: str
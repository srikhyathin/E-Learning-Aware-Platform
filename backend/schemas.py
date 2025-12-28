from pydantic import BaseModel

class EngagementState(BaseModel):
    emotion: str
    interest: str | None = None
    activity: str

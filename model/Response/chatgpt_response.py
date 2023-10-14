from pydantic import BaseModel

class ChatgptResponse(BaseModel):
    success: bool
    msg: str
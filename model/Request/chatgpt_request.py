from pydantic import BaseModel

class ChatgptRequest(BaseModel):
    session_id: str
    text: str
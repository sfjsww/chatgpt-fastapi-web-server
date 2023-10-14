from pydantic import BaseModel

class ChatgptResponse(BaseModel):
    msg: str
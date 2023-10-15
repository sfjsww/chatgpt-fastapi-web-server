from fastapi import APIRouter

from service import ChatGPTBot
from service.chatgpt.context import Context, ContextType
from model.Request.chatgpt_request import ChatgptRequest
from model.Response.chatgpt_response import ChatgptResponse

v1 = APIRouter()

chat_gpt = ChatGPTBot()
API_KEY = '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'

@v1.post('/gpt')
async def chatgpt(data: ChatgptRequest):
    try:
        res = chat_gpt.reply(data.text, Context(ContextType.TEXT, kwargs={'session_id': data.session_id, 'openai_api_key': API_KEY}))
        return ChatgptResponse(success=True, msg=res.content)
    except Exception as e:
        print(e)
        return ChatgptResponse(success=False, msg=str(e))
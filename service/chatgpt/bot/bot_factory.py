"""
channel factory
"""
CHATGPT = "chatGPT"

def create_bot(bot_type: str):
    """
    create a bot_type instance
    :param bot_type: bot type code
    :return: bot instance
    """

    if bot_type == CHATGPT:
        # ChatGPT 网页端web接口
        from chatgpt.chat_gpt_bot import ChatGPTBot
        return ChatGPTBot()

    raise RuntimeError
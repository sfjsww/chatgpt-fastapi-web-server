"""
Auto-replay chat robot abstract class
"""


from chatgpt.context import Context
from chatgpt.reply import Reply


class Bot(object):
    def reply(self, query, context: Context = None) -> Reply:
        """
        bot auto-reply content
        :param req: received message
        :return: reply content
        """
        raise NotImplementedError
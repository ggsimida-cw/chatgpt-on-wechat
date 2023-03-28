

"""
聊天机器人的抽象类，向自定义的聊天机器人，可以继承此类

Auto-replay chat robot abstract class
"""


from bridge.context import Context
from bridge.reply import Reply


class Bot(object):
    def reply(self, query, context : Context =None) -> Reply:
        """
        bot auto-reply content
        :param req: received message
        :return: reply content
        """
        raise NotImplementedError

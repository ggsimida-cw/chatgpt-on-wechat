"""
通道抽象类
自定义通道可以继承此类
"""

from bridge.bridge import Bridge
from bridge.context import Context
from bridge.reply import Reply

class Channel(object):
    def startup(self):
        """
        init channel
        """
        raise NotImplementedError

    def handle_text(self, msg):
        """
        接受文本信息
        process received msg
        :param msg: message object
        """
        raise NotImplementedError

    def send(self, msg, receiver):
        """
        发送信息
        send message to user 发送方
        :param msg: message content 发送的内容
        :param receiver: receiver channel account 指明接受者
        :return: 
        """
        raise NotImplementedError

    def build_reply_content(self, query, context : Context=None) -> Reply:
        """
        构建发送的内容
        :param query:
        :param context:
        :return:
        """
        return Bridge().fetch_reply_content(query, context)

    def build_voice_to_text(self, voice_file) -> Reply:
        """
        构建语音到文本
        :param voice_file:
        :return:
        """
        return Bridge().fetch_voice_to_text(voice_file)
    
    def build_text_to_voice(self, text) -> Reply:
        """
         构建文本到语音
        :param text:
        :return:
        """
        return Bridge().fetch_text_to_voice(text)

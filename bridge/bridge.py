from bridge.context import Context
from bridge.reply import Reply
from common.log import logger
from bot import bot_factory
from common.singleton import singleton
from voice import voice_factory
from config import conf
from common import const


@singleton
class Bridge(object):
    def __init__(self):
        self.btype={
            "chat": const.CHATGPT, # 默认chatgpt
            "voice_to_text": conf().get("voice_to_text", "openai"), # 默认openai
            "text_to_voice": conf().get("text_to_voice", "baidu") # 默认百度
        }
        model_type = conf().get("model")
        if model_type in ["text-davinci-003"]:
            self.btype['chat'] = const.OPEN_AI
        if conf().get("use_azure_chatgpt"):
            self.btype['chat'] = const.CHATGPTONAZURE
        self.bots={} # 聊天机器人实例集合

    def get_bot(self,typename):
        """
        根据相应的信息类型创建对应的聊天机器人对象，并赋值给self.bots
        :param typename:  信息类型（text_to_voice，voice_to_text，chat）
        :return:
        """
        if self.bots.get(typename) is None:
            logger.info("create bot {} for {}".format(self.btype[typename],typename))
            if typename == "text_to_voice":
                self.bots[typename] = voice_factory.create_voice(self.btype[typename])
            elif typename == "voice_to_text":
                self.bots[typename] = voice_factory.create_voice(self.btype[typename])
            elif typename == "chat":
                self.bots[typename] = bot_factory.create_bot(self.btype[typename])
        return self.bots[typename]
    
    def get_bot_type(self,typename):
        '''
        根据信息类型获取聊天机器人
        :param typename:
        :return:
        '''
        return self.btype[typename]

    def fetch_reply_content(self, query, context : Context) -> Reply:
        """
        拉取回复的内容（文本）
        :param query:  查询的消息
        :param context:
        :return:
        """
        return self.get_bot("chat").reply(query, context)

    def fetch_voice_to_text(self, voiceFile) -> Reply:
        """
        拉取回复的声音转文本内容
        :param voiceFile:
        :return:
        """

        return self.get_bot("voice_to_text").voiceToText(voiceFile)

    def fetch_text_to_voice(self, text) -> Reply:
        """
        拉取回复的文本转语音内容
        :param text:
        :return:
        """
        return self.get_bot("text_to_voice").textToVoice(text)

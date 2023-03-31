# encoding:utf-8

from config import conf, load_config
from channel import channel_factory
from common.log import logger

from plugins import *

def run():
    try:
        # load config
        # 加载配置文件
        load_config()

        # create channel
        channel_name=conf().get('channel_type', 'wx')
        channel = channel_factory.create_channel(channel_name)
        if channel_name=='wx': # 目前仅支持ichat拥有插件
            PluginManager().load_plugins()

        # startup channel
        channel.startup() #　启动
    except Exception as e:
        logger.error("App startup failed!")
        logger.exception(e)

if __name__ == '__main__':
    run()
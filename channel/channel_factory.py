"""
channel factory
通道工厂

"""

def create_channel(channel_type):
    """
    create a channel instance
    :param channel_type: channel type code
    :return: channel instance
    """
    # 该通道基于ichat-uos实现
    if channel_type == 'wx':
        from channel.wechat.wechat_channel import WechatChannel
        return WechatChannel()
    # 该通道基于wechaty实现
    elif channel_type == 'wxy':
        from channel.wechat.wechaty_channel import WechatyChannel
        return WechatyChannel()
    elif channel_type == 'terminal':
        from channel.terminal.terminal_channel import TerminalChannel
        return TerminalChannel()
    raise RuntimeError

import ujson as json
import re

from nonebot.drivers import Response
from nonebot.utils import logger_wrapper


log = logger_wrapper("Gewechat")


def resp_json(resp: Response) -> dict:
    """
    将Response对象转换为JSON格式
    """
    return json.loads(resp.content.decode("utf-8"))  # type: ignore

def get_sender(xml: str) -> str:
    """
    获取发送者的wxid
    """
    reg = re.compile(r'^wxid_[a-zA-Z0-9]+:\n')
    if reg.findall(xml):
        sender = reg.findall(xml)[0].split(":")[0]
        return sender
    else:
        return ""

def remove_prefix_tag(xml: str) -> str:
    """
    移除信息中发送者的前置标签, 返回正确的字符串
    """

    result = re.sub(r'^\d+@chatroom:\n', '', xml)
    result = re.sub(r'^wxid_[a-zA-Z0-9]+:\n', '', result)
    return result

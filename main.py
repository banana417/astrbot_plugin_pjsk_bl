from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import re

@register("astrbot_plugin_pjsk_bl","bunana417","倍率计算插件，根据输入的五组数据计算结果","1.0.0",)
class RateCalculatorPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        logger.info("倍率计算插件已加载")

  @on_message
    async def handle_message(self, ctx: MessageEvent):
        # 获取用户消息内容
        message = event.message_str.strip()
        
        # 匹配"倍率+五组数据"格式 (例如: "倍率 100 20 30 40 50")
        pattern = r'^倍率\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)$'
        match = re.match(pattern, message)
        
        if not match:
            return  # 不匹配则不处理
        
        try:
            # 提取五个数字
            num1 = float(match.group(1))
            num2 = float(match.group(2))
            num3 = float(match.group(3))
            num4 = float(match.group(4))
            num5 = float(match.group(5))
            
            # 执行计算
            result1 = num1 + (num2 + num3 + num4 + num5) * 0.2
            result2 = result1 * 0.01 + 1  # 1%即0.01
            
            # 格式化输出结果
            response = f"您的模拟卡组为：{result2:.2f}倍率；技能实际值为{result1:.2f}%"
            yield event.plain_result(response)
            
        except Exception as e:
            logger.error(f"计算出错: {str(e)}")
            yield event.plain_result("计算失败，请检查输入格式是否正确")

    async def terminate(self):
        logger.info("倍率计算插件已卸载")

from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register(
    name="pjsk_bl",
    author="bunana",
    description="倍率计算插件，用于计算模拟卡组的倍率和技能实际值",
    version="1.0.0",
    repository="https://github.com/yourusername/astrbot_plugin_pjsk_bl"
)
class RateCalculatorPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        logger.info("倍率计算插件已加载")

    @filter.command(
        "倍率",
        args_tip="倍率 <卡1总合力> <卡2总合力> <卡3总合力> <卡4总合力> <卡5总合力>"
    )
    async def calculate_rate(self, event: AstrMessageEvent, num1: float, num2: float, num3: float, num4: float, num5: float):
        '''处理倍率计算指令，格式: 倍率 <卡1总合力> <卡2总合力> <卡3总合力> <卡4总合力> <卡5总合力>'''
        try:
            # 直接使用注入的参数进行计算
            result1 = num1 + (num2 + num3 + num4 + num5) * 0.2
            result2 = result1 * 0.01 + 1

            # 格式化输出结果
            response = f"您的模拟卡组：\n倍率: {result2:.2f}\n技能实际值: {result1:.2f}"
            yield event.plain_result(response)

        except Exception as e:
            logger.error(f"计算出错: {str(e)}")
            yield event.plain_result("计算过程中发生未知错误，请联系管理员")

    async def terminate(self):
        logger.info("倍率计算插件已卸载")
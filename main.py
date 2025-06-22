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

   # 1. 在装饰器中添加 `args_tip`，当用户输入错误时，AstroBot会用它来提示用户
@filter.command("倍率", args_tip="倍率 <卡1总合力> <卡2总合力> <卡3总合力> <卡4总合力> <卡5总合力>")
# 2. 直接在函数签名中定义参数和类型，AstroBot会自动解析和注入
async def calculate_rate(self, event: AstrMessageEvent, num1: float, num2: float, num3: float, num4: float, num5: float):
    '''处理倍率计算指令'''
    try:
        # 3. 删除了所有手动解析的代码，直接使用注入的参数进行计算
        result1 = num1 + (num2 + num3 + num4 + num5) * 0.2
        result2 = result1 * 0.01 + 1

        # 格式化输出结果
        response = f"您的模拟卡组：\n倍率: {result2:.2f}\n技能实际值: {result1:.2f}"
        yield event.plain_result(response)

    # 4. 异常处理逻辑可以简化。因为AstroBot已保证参数是5个浮点数，
    #    这里的异常捕获主要用于防御计算过程本身可能出现的未知错误。
    except Exception as e:
        logger.error(f"计算出错: {str(e)}")
        yield event.plain_result("计算过程中发生未知错误，请联系管理员")

async def terminate(self):
    logger.info("倍率计算插件已卸载")

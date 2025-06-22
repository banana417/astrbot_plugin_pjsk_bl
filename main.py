from astrbot.api import filter, register
from astrbot.api.star import Star, Context
from astrbot.api.event import AstrMessageEvent

@register("cardsimulator")
class CardSimulatorPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.context.logger.info("卡组模拟插件已加载")

    # 添加 args_tip 参数用于格式提示
    @filter.command("倍率", 
                   priority=1, 
                   args_tip="数字1 数字2 数字3 数字4 数字5",
                   description="计算卡组倍率和技能实际值")
    async def calculate_ratio(self, event: AstrMessageEvent, *args: str):
        """卡组倍率计算器
        格式: 倍率 数字1 数字2 数字3 数字4 数字5
        示例: 倍率 80 90 85 95 100
        """
        try:
            # 验证参数数量
            if len(args) != 5:
                error_msg = (
                    "参数数量错误！需要5个数字参数\n"
                    "正确格式: 倍率 数字1 数字2 数字3 数字4 数字5\n"
                    "示例: 倍率 80 90 85 95 100"
                )
                return event.plain_result(error_msg)
            
            # 转换参数为浮点数
            numbers = [float(arg) for arg in args]
            
            # 执行计算
            result1 = numbers[0] + (numbers[1] + numbers[2] + numbers[3] + numbers[4]) * 0.2
            result2 = result1 * 0.01 + 1
            
            # 格式化输出（在技能实际值后添加%符号）
            response = (
                f"您的模拟卡组：\n"
                f"倍率为 {result2:.2f}\n"
                f"技能实际值为 {result1:.2f}%"
            )
            
            return event.plain_result(response)
            
        except ValueError:
            error_msg = (
                "参数类型错误！所有参数必须是数字\n"
                "正确格式: 倍率 数字1 数字2 数字3 数字4 数字5\n"
                "示例: 倍率 80 90 85 95 100"
            )
            return event.plain_result(error_msg)
        except Exception as e:
            self.context.logger.error(f"计算错误: {str(e)}")
            return event.plain_result("计算失败，请稍后再试")

    async def terminate(self):
        self.context.logger.info("卡组模拟插件已卸载")

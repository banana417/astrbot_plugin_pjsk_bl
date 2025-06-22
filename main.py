from astrbot.api import filter, register, logger
from astrbot.api.star import Star, Context
from astrbot.api.event import AstrMessageEvent
from typing import List

@register("astrbot_plugin_pjsk_bl", "bunana417", "1.0.0")
class CardSimulatorPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        logger.info("卡组模拟插件已加载")

    @filter.command("倍率", priority=1)
    async def calculate_ratio(self, event: AstrMessageEvent, *args: str):
        """卡组倍率计算器
        格式: 倍率 数字1 数字2 数字3 数字4 数字5
        示例: 倍率 80 90 85 95 100
        """
        try:
            # 验证参数数量
            if len(args) != 5:
                raise ValueError("需要5个参数，请检查输入格式")
            
            # 转换参数为浮点数
            numbers = [float(arg) for arg in args]
            
            # 执行计算
            result1 = self._calculate_result1(numbers)
            result2 = self._calculate_result2(result1)
            
            # 格式化输出
            response = (
                f"您的模拟卡组：\n"
                f"倍率为 {result2:.2f}\n"
                f"技能实际值为 {result1:.2f}"
            )
            
            yield event.plain_result(response)
            
        except ValueError as e:
            error_msg = f"参数错误: {str(e)}\n正确格式: 倍率 数字1 数字2 数字3 数字4 数字5"
            yield event.plain_result(error_msg)
        except Exception as e:
            logger.error(f"计算发生错误: {str(e)}")
            yield event.plain_result("计算失败，请稍后再试")

    def _calculate_result1(self, numbers: List[float]) -> float:
        """计算技能实际值: 数字1+(数字2+数字3+数字4+数字5)*0.2"""
        return numbers[0] + sum(numbers[1:]) * 0.2

    def _calculate_result2(self, result1: float) -> float:
        """计算倍率: 结果1*1%+1"""
        return result1 * 0.01 + 1

    async def terminate(self):
        logger.info("卡组模拟插件已卸载")

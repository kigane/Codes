from enum import Enum


class Type(Enum):
    FLAT = 100
    PERCENT_ADD = 200 # 独立增加的百分比
    PERCENT_MULTI = 300 # 可叠加的百分比


class StatModifier():
    def __init__(self, value: float, type: Type, order: int = None, source=None) -> None:
        self.value = value
        self.type = type
        if order is None:
            self.order = self.type.value
        else:
            self.order = order
        self.source = source # 跟踪Modifier的来源，便于UI显示功能的丰富，也便于实现物品的装备，卸下。Nice!
    

from sqlalchemy import false
from StatModifier import StatModifier, Type


class CharacterStat():
    def __init__(self, base_value) -> None:
        self.base_value = base_value
        self.__modifier_lst = []
        self.__isDirty = True
        self.__final_value = 0
        self.__sum_percent = 0

    def AddModifier(self, modifier):
        self.__isDirty = True
        self.__modifier_lst.append(modifier)

    def RemovedModifier(self, modifier) -> bool:
        try:
            self.__modifier_lst.remove(modifier)
            self.__isDirty = True
        except ValueError:
            return False
        return True

    def RemovedAllModifierFromSource(self, source) -> bool:
        did_remove = False
        for i in reversed(range(len(self.__modifier_lst))):
            if self.__modifier_lst[i].source == source:
                did_remove = True
                self.__isDirty = True
                self.__modifier_lst.pop(i)
        return did_remove

    def CalcFinalValue(self):
        self.__modifier_lst.sort(key=lambda modifier: modifier.order)
        final_value = self.base_value
        for idx, modifier in enumerate(self.__modifier_lst):
            if modifier.type == Type.FLAT:
                final_value += modifier.value
            elif modifier.type == Type.PERCENT_ADD:
                self.__sum_percent += modifier.value
                if idx + 1 >= len(self.__modifier_lst) or self.__modifier_lst[idx + 1].type != Type.PERCENT_ADD:
                    self.__final_value *= (1 + self.__sum_percent)
                    self.__sum_percent = 0
            elif modifier.type == Type.PERCENT_MULTI:
                final_value *= (1 + modifier.value)
        return round(final_value, 4)

    @property
    def FinalValue(self):
        if self.__isDirty:
            self.__final_value = self.CalcFinalValue()
            self.__isDirty = False
        return self.__final_value

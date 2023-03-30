from black import main

from CharacterStat import CharacterStat
from StatModifier import StatModifier, Type


class Character():
    def __init__(self, stat: CharacterStat) -> None:
        self.stat = stat


class Item():
    def __init__(self) -> None:
        pass
        
    def Equip(self, c: Character):
        mod1 = StatModifier(10, Type.FLAT, source=self)
        mod2 = StatModifier(0.1, Type.PERCENT_MULTI, source=self)
        c.stat.AddModifier(mod1)
        c.stat.AddModifier(mod2)

    def Unequip(self, c: Character):
        c.stat.RemovedAllModifierFromSource(self)

if __name__ == '__main__':
    stat = CharacterStat(10)
    character = Character(stat)
    item = Item()
    item.Equip(character)
    print(character.stat.FinalValue)
    item.Unequip(character)
    print(character.stat.FinalValue)

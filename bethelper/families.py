"""
This is the class file for families
"""


class Family:
    def __init__(self, name: str = None, age: int = 18):
        self._name = name
        self._age = age

    def get_power_trait(self):
        return self._power

    def get_speed_trait(self):
        return self._speed

    def get_knowledge_trait(self):
        return self._knowledge

    def get_sanity_trait(self):
        return self._sanity

    def take_general_damage(self, trait: str, dmg: int):
        pass

    def take_general_damages(self, total_dmg: int):
        """
        Take multiple points of damages
        Either take # dice of damage or take # points of damage
        """
        dmg_taken = 0  # damage taken
        while dmg_taken <= total_dmg:
            t = None  # TODO: ask the user from console which trait
            dmg = 0  # TODO: ask the user/generate damage
            self.take_general_damage(t, dmg)
            dmg_taken += dmg

    def take_mental_damage(self, trait: str):
        pass

    def take_physical_damage(self, trait: str):
        pass

    def revert_last_step(self):
        """
        Revert last modification to the family character
        """
        pass

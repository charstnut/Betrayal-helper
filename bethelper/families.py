"""
This is the class file for families
"""
from abc import ABC


class BaseFamily(ABC):
    """
    Base family class
    """
    def __init__(self, name: str = None, age: int = 18):
        self._name = name
        self._age = age
        # The start indices have to be changed in subclasses
        # These trait lists are to be replaced within each concrete family class
        self._trait_dict = {
            "power": [],
            "speed": [],
            "knowledge": [],
            "sanity": [],
            "start_idx": []
        }
        self._power_idx: int
        self._speed_idx: int
        self._knowledge_idx: int
        self._sanity_idx: int

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def power(self):
        """
        Getter method for trait value. The class only keeps track of the index
        """
        return self._trait_dict["power"][self._power_idx]

    @property
    def speed(self):
        return self._trait_dict["speed"][self._speed_idx]

    @property
    def knowledge(self):
        return self._trait_dict["knowledge"][self._knowledge_idx]

    @property
    def sanity(self):
        return self._trait_dict["sanity"][self._sanity_idx]


TRAIT_TABLE = {
    "Red": {
        "power": [4, 4, 4, 4, 5, 6, 7, 8],
        "speed": [2, 3, 3, 4, 5, 5, 6, 7],
        "knowledge": [2, 3, 3, 3, 5, 5, 6, 6],
        "sanity": [3, 3, 3, 3, 5, 5, 6, 7],
        "start_idx": [4, 4, 3, 3]
    },
    "Blue": {
        "power": [2, 2, 3, 4, 4, 6, 7, 7],
        "speed": [2, 3, 4, 5, 5, 5, 6, 6],
        "knowledge": [3, 4, 4, 5, 5, 6, 7, 8],
        "sanity": [3, 3, 4, 4, 5, 5, 6, 7],
        "start_idx": [3, 3, 4, 3]
    },
    "Yellow": {
        "power": [3, 4, 4, 4, 5, 6, 7, 8],
        "speed": [3, 3, 3, 4, 5, 6, 7, 8],
        "knowledge": [3, 4, 4, 4, 5, 6, 7, 8],
        "sanity": [3, 3, 3, 4, 5, 6, 7, 8],
        "start_idx": [3, 4, 3, 3]
    },
    "Green": {
        "power": [2, 3, 3, 4, 4, 5, 6, 6],
        "speed": [4, 4, 4, 6, 7, 7, 8, 8],
        "knowledge": [3, 3, 3, 4, 5, 6, 7, 8],
        "sanity": [2, 3, 3, 4, 4, 5, 5, 6],
        "start_idx": [4, 3, 3, 4]
    },
    "Purple": {
        "power": [3, 3, 3, 3, 4, 5, 6, 7],
        "speed": [2, 3, 4, 5, 6, 6, 7, 7],
        "knowledge": [2, 3, 4, 4, 4, 5, 5, 6],
        "sanity": [4, 4, 5, 5, 6, 7, 8, 8],
        "start_idx": [4, 3, 3, 3]
    }
}


class Family(BaseFamily):
    def __init__(self, color: str, name: str = None, age: int = 18):
        super().__init__(name, age)
        self._color = color
        # Initialize the class traits depending on the family color
        self._trait_dict = TRAIT_TABLE.get(color)
        if self._trait_dict is None:
            raise ValueError("Family color {} not found.".format(color))
        self._power_idx: int = self._trait_dict["start_idx"][0]
        self._speed_idx: int = self._trait_dict["start_idx"][1]
        self._knowledge_idx: int = self._trait_dict["start_idx"][2]
        self._sanity_idx: int = self._trait_dict["start_idx"][3]
        self._current_items = []  # list of items
        self._current_omens = []

    @property
    def color(self):
        return self._color

    def print_status(self):
        print("This is family member {} from the {} family".format(
            self.name, self.color))
        print(
            "Current traits are: Power {} | Speed {} | Knowledge {} | Sanity {}"
            .format(self.power, self.speed, self.knowledge, self.sanity))
        # print("Carrying items: \n")
        # for it in self._items():
        #     if it.is_heirloom(self):
        #         print("{}*".format(it.name))
        #     else:
        #         print(it.name)

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

    def add_omen(self, omen: str):
        self._current_omens.append(omen)
        print("Current omens: {}".format(self._current_omens))

    def add_item(self, item: str):
        self._current_items.append(item)
        print("Current items: {}".format(self._current_items))

    def _use_object(self, obj: str):
        pass

    def _set_object_as_used(self, obj: str):
        pass

    def use_omen(self, omen: str):
        self._use_object(omen)
        self._set_object_as_used(omen)

    def use_item(self, item: str):
        self._use_object(item)
        self._set_object_as_used(item)

    def revert_last_step(self):
        """
        Revert last modification to the family character
        """
        pass

    def _set_object_as_unused(self, obj: str):
        pass

    def end_turn(self):
        # End this family's turn
        for i in self._current_items:
            self._set_object_as_unused(i)
        for i in self._current_omens:
            self._set_object_as_unused(i)


if __name__ == "__main__":
    x = Family("Purple", "Hello")
    x.print_status()

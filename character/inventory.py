from .item import Item
from .inv_slot import InvSlot


class Inventory:
    
    inv_list:list
    
    def __init__(self, inv_list: list = [InvSlot() for i in range(25)]) -> None:
        self.inv_list = inv_list

    def additem(self, item:Item, position = 26):
        if position == 26:
            #TODO place the item in the lowest inv slot with that has None
            temp_position = 0
            position = temp_position
        if self.inv_list[position] == None:
            self.inv_list[position] = item
            return True
        else:
            print("There is already an item in that slot.")
            #TODO potentially have it switch places with other item once class for hand is created

"""
classes to make:

character- to hold inv and maybe use items
bag


"""


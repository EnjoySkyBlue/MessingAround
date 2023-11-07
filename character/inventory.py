from .item import Item
from .inv_slot import InvSlot


class Inventory:
    
    inv_list:list
    
    def __init__(self, inv_list: list = [InvSlot() for i in range(25)]) -> None:
        self.inv_list = inv_list

    def additem(self, item:Item, position = 25) -> bool:
        if position == 25:

            for slot_num, slot_item in enumerate(self.inv_list, 0):
                if slot_item == None:
                    self.additem(item, slot_num)
                    break
            
            return self.item_already_in_slot()

        if self.inv_list[position] == None:
            self.inv_list[position] = item
            return True
        else:
            return self.item_already_in_slot(item, position)
            

    def item_already_in_slot(self,item:Item, position) -> bool:

        print(f"There is already an item in slot {position}")
        return False
        #TODO returns False if unable to stack item or switch item, return True if able to switch
        #TODO potentially have it switch places with other item once class for hand is created
"""
classes to make:

character- to hold inv and maybe use items
bag


"""


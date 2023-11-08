from .item import Item
from .inv_slot import InvSlot



class Inventory:
    
    inv_list:list[InvSlot]
    inv_size = 25

    def __init__(self, inv_list: list = None, inv_size = 25) -> None:
        self.inv_list = [InvSlot() for i in range(25)]  if inv_list == None else inv_list
        self.inv_size = inv_size

    def __str__(self):
        return "".join(self.get_inv())

    def additem(self, item:Item, position = inv_size, amount = 1) -> bool:
        item_within_bounds = (position < self.inv_size and position >= 0)
        
        #Inserts Item if given position is within bounds of inv_size
        if item_within_bounds:
            
            slot_empty = (not self.inv_list[position].has_item)
            if slot_empty:
                self.inv_list[position].insert_item(item, amount)
                return True
            
            is_same_item = (self.inv_list[position].item.get_data() == item.get_data())
            if is_same_item:
                self.inv_list[position].insert_item(item, amount)
                return True
            
            return self.item_already_in_slot(item, position, amount)

        # #Assigns it to the lowest Empty slot if position isn't given        
        new_slot = self.find_empty_slot()
        if type(new_slot) is int:
            return self.additem(item, new_slot, amount)
        else:
            return new_slot
            
    def find_empty_slot(self):
        for slot_num, slot in enumerate(self.inv_list, 0):
            if not slot.has_item:
                return slot_num
        return self.inv_full()

    def inv_full(self):
        print("Inv Full")
        return False        

    def item_already_in_slot(self,item:Item, position, amount) -> bool:
        print(f"There is already an item in slot {position}")
        return False
        #TODO returns False if unable to stack item or switch item, return True if able to switch
        #TODO potentially have it switch places with other item once class for hand is created

    def get_inv(self, pos = None):
        # getting item in list for each slot
        item_list = [f"{place}: {inv_slot.item if inv_slot.has_item else 'No item'} [{inv_slot.amount}]\n" for place, inv_slot in enumerate(self.inv_list,1)]
        if pos == None:
            return item_list
        return "".join(item_list[:pos])

{
    "func": lambda a,b:a*b
}


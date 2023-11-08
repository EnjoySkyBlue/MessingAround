from .item import Item

class InvSlot:

    item: Item
    enabled: bool
    has_item: bool
    amount: int

    def __init__(self, item = None, amount = 0) -> None:
        if type(item) == Item:
            self.insert_item(item)
        else:
            self.has_item = False
        self.amount = amount

    def insert_item(self, item:Item, amount = 1):
        self.amount += amount
        self.item = item
        self.has_item = True
        return item
    


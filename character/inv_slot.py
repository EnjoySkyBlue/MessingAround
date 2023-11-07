from .item import Item

class InvSlot:

    item: Item
    enabled: bool
    has_item: bool

    def __init__(self, item = None) -> None:
        if type(item) == Item:
            self.add_item(item)
            self.has_item = True
        else:
            self.has_item = False

    def __str__(self):
        if not self.has_item:
            return "This slot does not contain an item"
        return self.item

    def add_item(self, item:Item):
        self.item = item
        return item
    




class Item:
    
    name:str
    item_type:str
    stackable:bool
    amount:int
    stats: dict
    descripton:str

    def __init__(self, name:str = "", item_type:str = "", stackable:bool = False, amount:int = 0, stats: dict={}, descripton:str = "") -> None:
        self.name = name
        self.item_type = item_type
        self.stackable = stackable
        self.amount = amount
        self.desccription = descripton

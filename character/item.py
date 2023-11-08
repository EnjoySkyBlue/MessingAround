

class Item:
    
    name:str
    item_type:str
    stackable:bool
    stats: dict
    descripton:str

    def __init__(self, name:str = "", item_type:str = "", stackable:bool = False, amount:int = 0, stats: dict={}, descripton:str = "") -> None:
        self.name = name
        self.item_type = item_type
        self.stackable = stackable
        self.amount = amount
        self.description = descripton

    def __str__(self):
        return f"{self.name}"

    def get_data(self):
        return {
            "name": self.name,
            "item_type": self.item_type,
            "stackable": self.stackable,
            "amount": self.amount,
            "description": self.description
        }
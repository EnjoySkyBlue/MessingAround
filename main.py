
from character.inventory import Inventory, Item, InvSlot


backpack = Inventory()

item_data = {
    "name":"Waterskin",
    "item_type": "supplies",
    "stackable": "false",
    "amount": 1,
    "stats": {},
    "descripton":"Holds Water"
}

waterskin = Item(**item_data)

backpack.additem(waterskin)
print(backpack.get_inv(3))

backpack.additem(waterskin,0)
print(backpack.get_inv(3))


"""
classes to make:
character- to hold inv and maybe use items
bag

amount should be handled by inv_slot

"""





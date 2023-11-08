# Being Silly With Python
print("="*25,"\n")
# Method------------------------------------------
def add(a,b):
    return a+b

# Dictionary of Func------------------------------
value = {
    "func": lambda a,b:a*b,
    "key": 5
}

# Variables---------------------------------------
x = 4
y = 5
multiply = value["func"]

# Assigning Functions-----------------------------
output = value["func"](x,y)
print("Multiply: ", output)

value["func"] = add
output = value["func"](x,y)
print("Add: ", output)

# AutoInstantiation of Classes--------------------
class Obj:
    pass

object1 = Obj()
object1.x, object1.y = (x,y)
object1.add = add

print("Class: ",object1.add(object1.x,object1.y))

# Other ------------------------------------------
print("\n")
print("="*25)


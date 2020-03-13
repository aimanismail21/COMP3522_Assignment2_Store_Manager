"""
Store contains the methods and classes responsible for:
1. Receiving orders and maintainingits inventory
2. Getting items from a factory class if the store does not have enough stock.
3. Creating Daily Transaction Report

"""

# todo Special Requirements
# The first time the store receives an order for an item, it is likely that it won't have the item in it's inventory since the store should be initialized with an empty inventory.
# In the event the store receives an order for an item that it does not have inventory for, then it should go ahead and get a 100 of those items made by the corresponding factory class.


class Store:
    pass


class OrderProcessor:
    """
    An Order Processor is an object that is responsible for reading a order
    file to create an Order object.

    Factory Object?
    """
    def __init__(self):
        pass

    def read_order(self):
        pass


class Order:
    """
    An Order is an analogy for an business transaction that orders a variety
    of items with appropriate business attributes like order number,
    product ids.
    """
#  todo Add functionality
# •	Order number
# •	Product ID
# •	Item - The type of item (Toy, StuffedAnimal and Candy).
# •	Name of the item
# •	A dictionary of product details. These details are the rest of the attributes of the item as specified in the excel sheet EXCEPT the name of the holiday — Easter, Christmas or Halloween.
# •	The order should also contain a reference to the appropriate Factory object that can create this item.

"""
Contains all the classes and logic related to orders, reading order files.
"""

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

# todo 9 factories to map and the mapping should return an instantiated
#  concrete factory
factory_mapping = {
    1: "Create a factory for a specific type of item",
    2: "2",
    3: "3",
    4: "",
    5: "",
    6: "",
    7: "",
    8: "",
    9: ""

}

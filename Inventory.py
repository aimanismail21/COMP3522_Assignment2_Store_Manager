"""
Maintains the store inventory.

Manages Toys, Stuffed Animals, and Candy objects.
"""
from abc import ABC

class ItemFactory(ABC):
    """
    #todo
    """
    pass

class Toy(ABC):
    """
    Toy defines the interface that the ItemFactory is responsible to create.
    """

    def __init__(self, is_battery_operated, min_age, name, description, product_id):
        """
        Initialize a toy.
        """
        self.has_battery = is_battery_operated
        self.min_age = min_age
        self.name = name
        self.description = description
        self.product_id = product_id

    pass

class StuffedAnimal(ABC):
    """
    StuffedAnimal defines the interface that the ItemFactory is responsible to create.
    """

    stuffing_options = ['polyester', 'fiberfill', 'woll']
    size_options = ['small', 'medium', 'large']
    fabric_options = ['linen', 'cotton', 'acrylic']

    def __init__(self, stuffing, size, fabric, name, description, product_id):
        """
        Initialize a Stuffed animal
        """

        self.stuffing = stuffing
        self.size = size
        self.fabric = fabric
        self.name = name
        self.description = description
        self.product_id = product_id

class Candy(ABC):
    """
    #todo
    """

    def __init__(self, has_nuts, has_lactose, name, description, product_id):
        self.has_nuts = has_nuts
        self.has_lactose = has_lactose
        self.description = description
        self.product_id = product_id
    pass

class SantasWorkShop(Toy):
    """
    #todo
    """



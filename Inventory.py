"""
Maintains the store inventory.

Manages Toys, Stuffed Animals, and Candy objects.
"""
from abc import ABC, abstractmethod

#todo concrete item classes should raises errors if properties are invalid
# or missing

# todo errors raised in concrete item classes must be caught in higher level
#  modules (item factories) where the error will result in the order being
#  invalidated with the proper reason why the error occured.

class InvalidDataError(Exception):
    """
    An invalid data error is an error that is raised when a constructor
    is initialized with invalid arguments that do not match the class
    requirements.
    """

    def __init__(self, error_message):
        """
        Initialize an InvalidDataError.
        :param error_message: a str, the message that contains the error
        which raised InvalidDataError
        """
        super().__init__(f"InvalidDataError - {error_message}")
        self.missing_word = error_message


class ItemFactory(ABC):
    """
    The base factory class which creates a Toy, StuffedAnimal and Candy.
    """

    @abstractmethod
    def create_toy(self):
        """
        Create a toy
        :return: a Toy
        """
        pass

    @abstractmethod
    def create_stuffed_animal(self):
        """
        Create a stuffed animal
        :return: a StuffedAnimal
        """
        pass

    @abstractmethod
    def create_candy(self):
        """
        Create a Candy
        :return: a Candy
        """
        pass


class ChristmasItemFactory(ItemFactory):
    """
    This factory class implements the ItemFactory Interface. It
    returns a product family consisting of SantasWorkShop, Reindeer,
    and Candy respectively as subclasses to the Toy, StuffedAnimal
    and Candy class.
    """

    def create_toy(self, **kwargs):
        """
        Create a toy
        :return: a Toy
        """
        toy = SantasWorkShop(**kwargs)
        return toy

    def create_stuffed_animal(self, **kwargs):
        """
        Create a stuffed animal
        :return: a StuffedAnimal
        """

        stuffed_animal = Reindeer(**kwargs)
        return stuffed_animal

    def create_candy(self, **kwargs):
        """
        Create a Candy
        :return: a Candy
        """

        candy = CandyCane(**kwargs)
        return candy


class HalloweenItemFactory(ItemFactory):
    """
    This factory class implements the ItemFactory Interface. It
    returns a product family consisting of RCSpider, DancingSkeleton
    and PumpkinCaramelToffee respectively as subclasses to the Toy,
    StuffedAnimal and Candy class.
    """

    def create_toy(self, **kwargs):
        """
        Create a toy
        :return: a Toy
        """
        toy = RCSpider(**kwargs)
        return toy

    def create_stuffed_animal(self, **kwargs):
        """
        Create a stuffed animal
        :return: a StuffedAnimal
        """

        stuffed_animal = DancingSkeleton(**kwargs)
        return stuffed_animal

    def create_candy(self, **kwargs):
        """
        Create a Candy
        :return: a Candy
        """

        candy = PumpkinCaramelToffee(**kwargs)
        return candy


class EasterItemFactory(ItemFactory):
    """
    This factory class implements the ItemFactory Interface. It
    returns a product family consisting of RobotBunny, EasterBunny,
    CremeEgg respectively as subclasses to the Toy, StuffedAnimal
    and Candy class.
    """

    def create_toy(self, **kwargs):
        """
        Create a toy
        :return: a Toy
        """
        toy = RobotBunny(**kwargs)
        return toy

    def create_stuffed_animal(self, **kwargs):
        """
        Create a stuffed animal
        :return: a StuffedAnimal
        """

        stuffed_animal = EasterBunny(**kwargs)
        return stuffed_animal

    def create_candy(self, **kwargs):
        """
        Create a Candy
        :return: a Candy
        """

        candy = CremeEgg(**kwargs)
        return candy


class Toy(ABC):
    """
    Toy defines the interface that the ItemFactory is responsible to
    create.
    """

    def __init__(self, is_battery_operated, min_age, name, description,
                 product_id):
        """
        Initialize a toy.
        """
        if type(is_battery_operated) != bool:
            raise InvalidDataError("Toy: is_battery_operated must be"
                                   "a bool.")
        self.has_battery = is_battery_operated

        if type(min_age) != int:
            raise InvalidDataError("Toy: min_age must be"
                                   "a bool.")
        self.min_age = min_age

        if type(name) != str:
            raise InvalidDataError("Toy: name must be a string")
        self.name = name

        if type(description) != str:
            raise InvalidDataError("Toy: description must be a string")
        self.description = description

        if type(product_id) != str:
            raise InvalidDataError("Toy: product id must be a string")
        self.product_id = product_id

    pass


class StuffedAnimal(ABC):
    """
    StuffedAnimal defines the interface that the ItemFactory is
    responsible to create.
    """

    def __init__(self, stuffing, size, fabric, name, description, product_id):
        """
        Initialize a Stuffed animal
        :param stuffing: a str, the stuffing used
        :param size: a str, size of the StuffedAnimal
        :param fabric: a str, the material of fabric used
        :param name: a str, the name of the StuffedAnimal
        :param description: a str, a description of the StuffedAnimal
        :param product_id: a str, the product id of the StuffedAnimal
        """

        stuffing_options = ['polyester fiberfill', 'wool']
        size_options = ['small', 'medium', 'large']
        fabric_options = ['linen', 'cotton', 'acrylic']

        if not stuffing or stuffing.lower() not in stuffing_options:
            raise InvalidDataError("StuffedAnimal: "
                                   "stuffing must be polyester fiberfill"
                                   "or wool")
        self.stuffing = stuffing

        if not size or size.lower() not in size_options:
            raise InvalidDataError("StuffedAnimal: "
                                   "size must be small medium "
                                   "or large")

        self.size = size

        if not fabric or fabric.lower() not in fabric_options:
            raise InvalidDataError("StuffedAnimal: "
                                   "Fabric must be linen, cotton or"
                                   "acrylic")
        self.fabric = fabric

        if type(name) != str:
            raise InvalidDataError("StuffedAnimal: "
                                   "Name must be a string")

        self.name = name

        if type(description) != str:
            raise InvalidDataError("StuffedAnimal: "
                                   "Description id must be a string")

        self.description = description

        if type(product_id) != str:
            raise InvalidDataError("StuffedAnimal: "
                                   "product id must be a string")

        self.product_id = product_id


class Candy(ABC):
    """
    Candy defines the interface that the ItemFactory is responsible to
    create.
    """

    def __init__(self, has_nuts, has_lactose, name, description, product_id):
        """
        Initialize a Candy.
        :param has_nuts: a bool, if the candy contains nuts of not
        :param has_lactose: a bool, if the candy contains lactose or not
        :param name: a str, the name of the candy
        :param description: a str, the description of the candy
        :product_id: a str, the product id of the candy
        """

        if type(has_nuts) != bool:
            raise InvalidDataError("Candy: has nuts must be a bool")

        self.has_nuts = has_nuts

        if type(has_lactose) != bool:
            raise InvalidDataError("Candy: has lactose must be a bool")
        self.has_lactose = has_lactose

        if type(name) != str:
            raise InvalidDataError("Candy: name must be a str")

        self.name = name

        if type(description) != str:
            raise InvalidDataError("Candy: Description must be a str")

        self.description = description

        if type(product_id) != str:
            raise InvalidDataError("Candy: product id must be a str")

        self.product_id = product_id


class SantasWorkShop(Toy):
    """
    SantasWorkshop is a type of Toy that has dimensions and the number
    of rooms as additional fields.
    """
    def __init__(self, dimensions, num_rooms, **kwargs):
        """
        Initialize a SantasWorkShop
        :param dimensions: a tuple #todo
        :param num_rooms: an int, the number of rooms
        :param kwargs: Any additional keyword attributes for base class
        :raises: InvalidDataError, when an attribute is assigned an
        invalid data type or given data that does not meet requirements
        """
        super().__init__(**kwargs)

        #todo
        if len(dimensions) != 2:
            raise InvalidDataError("SantasWorkshop: Number of rooms"
                                   "is not in length by width")
        #todo
        for dimension in dimensions:
            if type(dimension) != int:
                raise InvalidDataError("SantasWorkshop: Number of rooms"
                                       "is not an integer")
        if type(num_rooms) != int:
            raise InvalidDataError("SantasWorkshop: Number of rooms is not an"
                                   "integer value")
        self._dimensions = dimensions
        self._num_rooms = num_rooms


class RCSpider(Toy):
    """
    RCSpider is a type of Toy that has speed, a jump height, can glow
    or not and a specific spider type as additional fields.
    """

    def __init__(self, speed, jump_height, has_glow, spider_type, **kwargs):
        """
        Initialize a RCSpider
        :param speed: an int, specified speed of RCSpider units in m/s
        :param jump_height: an int, specified jump height of RCSpider
        :param has_glow: a boolean, if the RCSpider glows or not
        :param spider_type: a string, either a Tarantula or a
        WolfSpider type otherwise nothing else
        :param kwargs: Any additional keyword attributes for base class
        :raises: InvalidDataError, when an attribute is assigned an
        invalid data type or given data that does not meet requirements
        """
        fastest_toy_speed = 1.6
        rc_spider_types = ['tarantula', 'wolf spider']
        super().__init__(**kwargs)
        if type(speed) != int:
            raise InvalidDataError("RCSpider: Must be given an integer")

        if speed >= fastest_toy_speed:
            raise InvalidDataError(f"RCSpider: Capped speed is"
                                   f"{fastest_toy_speed} meters/seconds")

        if speed < 0:
            raise InvalidDataError(f"RCSpider: Speed is negative")

        if jump_height < 0:
            raise InvalidDataError(f"RCSpider: Jump height is negative")

        if not spider_type or spider_type.lower() not in rc_spider_types:
            raise InvalidDataError(f"RCSpider: spider type is either "
                                   f"{rc_spider_types} or nothing else")
        self.speed = speed
        self.jump_height = jump_height
        self.has_glow = has_glow
        self.spider_type = spider_type


class RobotBunny(Toy):
    """
     RobotBunny is a type of Toy that has a number of sound effects and
     a colour as additional fields.
    """
    def __init__(self, num_sound, colour, **kwargs):
        """
        Initialize a RobotBunny
        :param num_sound: an int, the number of sound effects
        :param colour: a string, specified colour of RobotBunny
        :param kwargs: Any additional keyword attributes for base class
        :raises: InvalidDataError, when an attribute is assigned an
        invalid data type or given data that does not meet requirements
        """
        super().__init__(**kwargs)
        robot_bunny_colours = ['orange', 'blue', 'pink']
        if type(num_sound) != int:
            raise InvalidDataError(f"RobotBunny: number of sound effect "
                                   f"must be an integer")

        if not colour or colour.lower() not in robot_bunny_colours:
            raise InvalidDataError("RobotBunny: Color has either be"
                                   "orange, blue, pink or nothing else")

        self.num_sound = num_sound
        self.colour = colour


class DancingSkeleton(StuffedAnimal):
    """
    DancingSkeleton is a type of Stuffed Animal that made of Acrylic
    yarn and is stuffed with polyester fiberfill it also glows as an
    additional field.
    """
    def __init__(self, has_glow, **kwargs):
        """
        Initialize a Dancing Skeleton
        :param has_glow: a boolean, to determine if the Stuffed Animal
        glows or not
        :param kwargs: Any additional keyword attributes for base class.
        :raises: InvalidDataError, when an attribute is assigned an
        invalid data type or given data that does not meet requirements
        """
        super().__init__(**kwargs)
        self.has_glow = has_glow


class Reindeer(StuffedAnimal):
    """
    Reindeer is a stuffed animal that is made of cotton and stuffed with
    wool, it also glows as an additional field.
    """

    def __init__(self, has_glow, **kwargs):
        """
        Initialize a Reindeer
        :param has_glow: a boolean, to determine if the Stuffed Animal
        glows or not
        :param kwargs: Any additional keyword attributes for base class.
        """
        super().__init__(**kwargs)
        self.has_glow = has_glow


class EasterBunny(StuffedAnimal):
    """
    EasterBunny is a stuffed animal that is made of linen and stuffed
    with polyester fiberfill. It also comes in various colours as an
    additional field (White, Grey, Pink, Blue or None).
    """

    def __init__(self, colour, **kwargs):
        """
        Initialize an EasterBunny
        :param colour: a string, a specified color that is white, grey,
        pink, blue or nothing else
        :param kwargs: Any additional keyword attributes for base class.
        :raises: InvalidDataError, when an attribute is assigned an
        invalid data type or given data that does not meet requirements
        """
        super().__init__(**kwargs)

        colour_options = ['white', 'grey', 'pink', 'blue']

        if not colour or colour.lower() not in colour_options:
            raise InvalidDataError("EasterBunny: Color has either be"
                                   "orange, blue, pink or nothing else")

        self.colour = colour


class PumpkinCaramelToffee(Candy):
    """
    Pumpkin caramel toffee is a candy that is not lactose free and may
    contain traces of nuts. It comes in two varieties, sea salt or
    regular.
    """

    def __init__(self, variety, **kwargs):
        """
        Initialize a Pumpkin caramel toffee
        :param variety: a string, the variety of the candy that is
        either in sea salt or regular
        :param kwargs: Any additional keyword attributes for base class.
        :raises: InvalidDataError, when an attribute is assigned an
        invalid data type or given data that does not meet requirements
        """
        super().__init__(**kwargs)

        if not variety or variety.lower() not in variety:
            raise InvalidDataError("EasterBunny: Color has either be"
                                   "orange, blue, pink or nothing else")
        self.variety = variety


class CandyCane(Candy):
    """
    Candy cane is a candy that is lactose free and contain no nuts.
    """

    def __init__(self, stripes, **kwargs):
        """
        Initialize a Candy Cane
        :param stripes: a string, the colour of the stripes
        :param kwargs: Any additional keyword attributes for base class.
        :raises: InvalidDataError, when an attribute is assigned an
        invalid data type or given data that does not meet requirements
        """
        super().__init__(**kwargs)

        stripe_options = ['red', 'green']

        if not stripes or stripes.lower() not in stripe_options:
            raise InvalidDataError("CandyCane: Stripe has either be"
                                   "red or green")

        self.stripes = stripes


class CremeEgg(Candy):
    """
    Creme egg is a candy that is not lactose free and may contain traces
    of nuts
    """

    def __init__(self, pack_size, **kwargs):
        """
        Initialize a creme egg
        :param pack_size: a string, the variety of the candy that is
        either in sea salt or regular
        :param kwargs: Any additional keyword attributes for base class.
        :raises: InvalidDataError, when an attribute is assigned an
        invalid data type or given data that does not meet requirements
        """
        super().__init__(**kwargs)

        if type(pack_size) != int:
            raise InvalidDataError("CremeEgg: Must be an integer for"
                                   "pack size")

        self.pack_size = pack_size


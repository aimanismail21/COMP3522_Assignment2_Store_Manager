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
    Toy defines the interface that the ItemFactory is responsible to
    create.
    """

    def __init__(self, is_battery_operated, min_age, name, description,
                 product_id):
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
    StuffedAnimal defines the interface that the ItemFactory is
    responsible to create
    """

    stuffing_options = ['polyester fiberfill', 'woo']
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
        self.name = name
        self.description = description
        self.product_id = product_id
    pass


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
        :param kwargs: Any additional keyword attributes for base class.
        #todo add more comments later
        """
        super().__init__(**kwargs)
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
        :param speed: an int, specified speed of RCSpider
        :param jump_height: an int, specified jump height of RCSpider
        :param has_glow: a boolean, if the RCSpider glows or not
        :param spider_type: a string, either a Tarantula or a
        WolfSpider type otherwise nothing else
        :param kwargs: Any additional keyword attributes for base class.
        #todo add more comments later
        """
        super().__init__(**kwargs)
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
        :param kwargs: Any additional keyword attributes for base class.
        #todo add more comments later
        """
        super().__init__(**kwargs)
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
        #todo add more comments later
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
        #todo add more comments later
        """
        super().__init__(**kwargs)
        self.has_glow = has_glow


class EasterBunny(StuffedAnimal):
    """
    EasterBunny is a stuffed animal that is made of linen and stuffed
    with polyester fiberfill. It also comes in various colours as an
    additional field (White, Grey, Pink, Blue or None).
    """

    colour_options = ['white', 'grey', 'pink', 'blue']

    def __init__(self, colour, **kwargs):
        """
        Initialize an EasterBunny
        :param colour: a string, a specified color that is white, grey,
        pink, blue or nothing else
        :param kwargs: Any additional keyword attributes for base class.
        #todo add more comments later
        """
        super().__init__(**kwargs)
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
        #todo add more comments later
        """
        super().__init__(**kwargs)
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
        #todo add more comments later
        """
        super().__init__(**kwargs)
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
        #todo add more comments later
        """
        super().__init__(**kwargs)
        self.variety = pack_size


class ChristmasItemFactory(ABC):
    """
    This factory class implements the ItemFactory Interface. It
    returns a product family consisting of #todo
    """

    def create_toy(self):
        """

        :return:
        """
        toy = SantasWorkShop()
        return toy


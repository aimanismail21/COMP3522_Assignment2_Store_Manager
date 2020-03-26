"""
Contains all the classes and logic related to orders, reading order files.
"""
import pandas as pd
from Inventory import ChristmasItemFactory, EasterItemFactory, HalloweenItemFactory


class OrderProcessor:
    """
    An Order Processor is an object that is responsible for reading a order
    file to create an Order object.

    Factory Object?
    """

    def __init__(self):
        self.file_name = None
        self.order_file = None

    def file_name_request(self):
        self.file_name = input("What is the name of the input file?\n>>>")

    def read_order_file(self):
        path = f"./resources/{self.file_name}"
        try:
            temp_order = pd.read_excel(path,
                                       columns=['order_number',
                                                'holiday',
                                                'item',
                                                'name',
                                                'product_id',
                                                'quantity',
                                                'description',
                                                'has_batteries',
                                                'min_age',
                                                'dimensions',
                                                'num_rooms',
                                                'speed',
                                                'jump_height',
                                                'has_glow',
                                                'spider_type',
                                                'num_sound',
                                                'colour',
                                                'has_lactose',
                                                'has_nuts',
                                                'variety',
                                                'pack_size',
                                                'stuffing',
                                                'size',
                                                'fabric'])
        except FileNotFoundError as e:
            print("Unable to find file specified.")
        else:
            print("File Accepted")
            temp_order.fillna('NaN', inplace=True)
            # Replaces None values (nan) with string.
            self.order_file = temp_order
        finally:
            print("File Loaded")

    def create_order_from_order_file(self):
        print("Creating Orders from Order File")
        for row in self.order_file.iterrows():
            order = Order(**row[1])
            yield order


class Order:
    """
    An Order is an analogy for an business transaction that orders
    a variety of items with appropriate business attributes
    like order number, product ids.
    """
    #  todo test that mapping works
    holiday_factory_mapping = {
        'Christmas': ChristmasItemFactory,
        'Easter': EasterItemFactory,
        'Halloween': HalloweenItemFactory
    }
    """
    Holiday Factory Mapping is a dictionary to map a holiday to its
    appropriate factory class.
    """
    def __init__(self, order_number, holiday, product_id, item,
                 name, **kwargs):
        self.order_number = order_number
        self.product_id = product_id
        self.item = item
        self.name = name
        self.product_details = {key: value for key, value
                                in kwargs.items() if value != 'NaN'}

        self.factory = Order.holiday_factory_mapping[holiday]
        self.holiday = holiday


    def __repr__(self):
        return f"Order {self.order_number}, " \
               f"Item {self.item}, " \
               f"Product ID {self.product_id}, " \
               f"Name \"{self.name}\", " \
               f"Quantity {self.product_details['quantity']}"

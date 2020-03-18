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
        self.orders = []

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
            temp_order.fillna('NaN', inplace=True)
            # Replaces None values (nan) with string.
            self.order_file = temp_order
        finally:
            print("Finishing reading of file.")

    def create_order_from_order_file(self):
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
        # todo error handling for incorrect values
        # 1. product_id (first letter should be first letter of holiday
        # followed by 4 digits and first letter of item type
        # Ex. Christmas Stuffed Animal -> C1234S
        # Could be more things to error check
        self.order_number = order_number
        self.factory = Order.holiday_factory_mapping[holiday]
        self.product_id = product_id
        self.item = item
        self.name = name
        self.product_details = {key: value for key, value
                                in kwargs.items() if value != 'NaN'}
        # Removes NaN K:V pairs from product details

    def __repr__(self):
        return f"Order#: {self.order_number}\n" \
               f"Factory: {self.factory}\n" \
               f"ProductID: {self.product_id}\n" \
               f"Item Type: {self.item}\n" \
               f"Item Name: {self.name}\n" \
               f"Product Details: {self.product_details}"

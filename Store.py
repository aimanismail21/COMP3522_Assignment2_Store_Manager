"""
Store contains the methods and classes responsible for:
1. Receiving orders and maintainingits inventory
2. Getting items from a factory class if the store does not have enough stock.
3. Creating Daily Transaction Report
"""
import datetime


# todo Special Requirements
# The first time the store receives an order for an item, it is likely that it won't
# have the item in it's inventory since the store should be initialized with an empty inventory.
# In the event the store receives an order for an item that it does not have inventory for,
# then it should go ahead and get a 100 of those items made by the corresponding factory class.


class Store:
    def __init__(self):
        self.order_records = {}
        self.inventory = {} # {productID: {}}
        self._number_of_items_to_create = 100

    def validate_order(self, order) -> bool:
        print(f"Processing Order {order.order_number}")
        valid_order = True
        invalid_data_reasons = []
        if order.order_number in self.order_records:
            valid_order = False
            invalid_data_reasons.append("Order # was processed previously.")
        if order.holiday[0] != order.product_id[0] or order.item[0] != \
                order.product_id[5]:
            valid_order = False
            invalid_data_reasons.append("Product ID has the wrong format.")
        if not order.product_id[1:5].isdigit():
            valid_order = False
            invalid_data_reasons.append("Product ID has the wrong format.")
        if order.item not in ['Toy', 'StuffedAnimal', 'Candy']:
            valid_order = False
            invalid_data_reasons.append("Invalid Item for Order")
        if not valid_order:
            self.order_records[
                order.order_number] = f"Order {order.order_number}, " \
                                      f"Could not " \
                                      f"process order as" \
                                      f" data was corrupted," \
                                      f" InvalidDataError -" \
                                      f" {invalid_data_reasons}"
            return False
        else:
            self.order_records[order.order_number] = order
            return True

    def create_items(self, order, quantity):
        """
        Creates more items from a factory class
        :param item_factory: a factory to produce a type of item
        :return: an item
        """
        factory = self.factory()
        for number_of_items_to_creates\
                in range(0, self._number_of_items_to_create):
            if order.item == "Toy":
                toy = factory.create_toy(order.product_details)
            if order.item == "StuffedAnimal":
                stuffed_animal = factory.create_stuffed_animal(
                    order.product_details)
            if order.item == "Candy":
                candy = factory.create_candy(order.product_details)

    def daily_transaction_report(self):
        # create a text file
        # text file is a list of reco   rded orders in the day
        # convention DTR_DDMMYY_HHMM.txt
        today = datetime.datetime.now()
        format_string = datetime.date.strftime(today, "DTR_%d%m%y_%H%M.txt")
        with open(format_string, mode="w", encoding="UTF-8") as file_output:
            file_output.write("HOLIDAY STORE - DAILY TRANSACTION REPORT ("
                              "DRT)\n")
            file_output.write(datetime.datetime.strftime(
                today,
                "%d-%m-%Y %H:%M\n\n"))
            for order in self.order_records:
                file_output.write(order)

    def process_order(self, order) -> int:
        if order.product_id in self.inventory.keys():
            try:
                for i in range(order.product_details['quantity']):
                    create_items()


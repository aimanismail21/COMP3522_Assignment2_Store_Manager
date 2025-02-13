"""
Store contains the methods and classes responsible for:
1. Receiving orders and maintaining its inventory
2. Getting items from a factory class if the store does not have enough stock.
3. Creating Daily Transaction Report
"""
import datetime

from OrderProcessor import OrderProcessor


class Store:
    """
    Store is where a user can process web orders, check inventory levels,
    and create a daily transaction report when exiting.
    """

    def __init__(self):
        """
        Initializes a Store class.
        """
        self.order_records = {}
        self.inventory = {}
        self._number_of_items_to_create = 100
        self._counter_of_records = 1

    def validate_order(self, order) -> bool:
        """
        Validates an order for any discrepancies before processing.
        :param order: Order object
        :return: bool, True if valid
        """
        valid_order = True
        invalid_data_reasons = []
        if order.order_number in self.order_records:
            order.order_number = self._counter_of_records
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
                self._counter_of_records] = \
                f"Order {self._counter_of_records}, " \
                f"Could not " \
                f"process order as" \
                f" data was corrupted," \
                f" InvalidDataError -" \
                f" {invalid_data_reasons}"
            self._counter_of_records += 1
            return False
        else:
            self.order_records[self._counter_of_records] = order
            self._counter_of_records += 1
            return True

    def create_items(self, order, quantity):
        """
        Creates an item using the order's item factory.
        :param order: Order object, current order being processed
        :param quantity: int, number of items to create
        :return: None
        """
        factory = order.factory()
        number_to_create = self._number_of_items_to_create - quantity
        for number_of_items_to_creates \
                in range(0, number_to_create):
            if order.item == "Toy":
                toy = factory.create_toy(**order.product_details)
                yield toy
            if order.item == "StuffedAnimal":
                stuffed_animal = factory.create_stuffed_animal(
                    **order.product_details)
                yield stuffed_animal
            if order.item == "Candy":
                candy = factory.create_candy(**order.product_details)
                yield candy

    def daily_transaction_report(self):
        """
        Creates a daily transaction report that nicely formats the orders
        processed during the day.
        :return: None
        """
        today = datetime.datetime.now()
        format_string = datetime.date.strftime(today, "DTR_%d%m%y_%H%M.txt")
        with open(format_string, mode="w", encoding="UTF-8") as file_output:
            file_output.write("HOLIDAY STORE - DAILY TRANSACTION REPORT ("
                              "DRT)\n")
            file_output.write(datetime.datetime.strftime(
                today,
                "%d-%m-%Y %H:%M\n\n"))
            for order in self.order_records.values():
                if type(order) == str:
                    file_output.write(order.replace("'", "") + "\n")

                else:
                    file_output.write(order.__repr__() + "\n")

    def process_order(self, product_id, quantity_requested, product_name) -> \
            int:
        """
        Processes an order by removing items sold and returning the number
        of items unfulfilled in the order.
        :param product_id: a str, product id of the item being processed
        :param quantity_requested: an int, requested number of items to be sold
        :param product_name: a str, name of the item
        :return: int, the number of items unfulfilled
        """
        if product_id not in self.inventory.keys():
            self.inventory[product_id] = {'quantity': 0,
                                          'item': [],
                                          'name': product_name}
            return quantity_requested
        else:
            product_ledger = self.inventory[product_id]
            item_list = product_ledger['item']
            if product_ledger['quantity'] < quantity_requested:
                unfulfilled_orders = int(product_ledger['quantity']) - \
                                     int(quantity_requested)
                for item_to_remove in range(product_ledger['quantity']):
                    item_list.pop()
                product_ledger['quantity'] = 0
                return abs(unfulfilled_orders)
            if product_ledger['quantity'] > quantity_requested:
                for item_to_remove in range(quantity_requested):
                    item_list.pop()
                product_ledger['quantity'] -= quantity_requested
                return 0

    def check_inventory(self):
        """
        Reports the current inventory levels and status of each existing
        product line.
        :return: None
        """
        for product_line_ledger in self.inventory.values():
            stock_level = "IN STOCK"
            if product_line_ledger['quantity'] == 0:
                stock_level = "OUT OF STOCK"
            if product_line_ledger['quantity'] < 3:
                stock_level = "VERY LOW"
            if product_line_ledger['quantity'] < 10:
                stock_level = "LOW"
            print(f"Product: {product_line_ledger['name']}, Quantity: "
                  f"{product_line_ledger['quantity']},"
                  f" Stock Status: {stock_level}")

    def menu_order_processing(self):
        """
        Uses OrderProcessor to read and process and order file.
        :return: None
        """
        new_order_processing = OrderProcessor()
        new_order_processing.file_name_request()
        new_order_processing.read_order_file()
        for order in new_order_processing.create_order_from_order_file():
            valid = self.validate_order(order)
            if valid:
                unfulfilled_quantity = self.process_order(order.product_id,
                                                          order.quantity,
                                                          order.name)
                if unfulfilled_quantity > 0:
                    for item in self.create_items(order, unfulfilled_quantity):
                        product_ledger = self.inventory[order.product_id]
                        product_ledger['quantity'] += 1
                        product_ledger['item'].append(item)

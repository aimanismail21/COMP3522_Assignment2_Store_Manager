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
        # inventory of items
        self.order_records = ["fake data", "fakedate"]
        pass

    def read_order(self):
        pass

    def order_items(self, item_factory):
        """
        Creates more items from a factory class
        :param item_factory: a factory to produce a type of item
        :return: an item
        """
        # This function needs to create 100 items of a specific type.
        # We can yield these items until we have 100.

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


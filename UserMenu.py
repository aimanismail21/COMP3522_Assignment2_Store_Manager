"""
User Menu contains the logic to allow a user to do the following:
1. Process Web Orders
2. Check Inventory

This is likely the client
"""
import traceback
import Inventory
from Store import Store
from OrderProcessor import OrderProcessor, Order


class UserMenu:
    """

    """

    @staticmethod
    def menu_order_processing():
        new_order_processing = OrderProcessor()
        new_order_processing.file_name_request()
        new_order_processing.read_order_file()
        store = Store()
        for order in new_order_processing.create_order_from_order_file():
            # store receives the order and appends to its record
            valid = store.validate_order(order)
            if valid:
                unfufilled_quantity = store.process_order(order.product_id,
                                                          order.quantity,
                                                          order.name)
                for item in store.create_items(order, unfufilled_quantity):
                    product_ledger = store.inventory[order.product_id]
                    product_ledger['quantity'] += 1
                    product_ledger['item'].append(item)

    def __init__(self):
        self.user_menu_map = {

            "1": UserMenu.menu_order_processing,
            "2": Inventory, # todo test mapping
            "3": Store.daily_transaction_report
        }

    def prompt_menu(self):
        """

        :return:
        """
        invalid_selection = True
        while invalid_selection:
            option = input(
                "\nSelect option by inputting a digit.\n"
                "1: Process Web Orders\n"
                "2. Check Inventory\n"
                "3. Exit Program\n"
                ">>>")
            try:
                menu_option_selected = self.user_menu_map[option]
            except (KeyError, ValueError, AttributeError) as e:
                print("Invalid Selection")
            else:
                menu_option = menu_option_selected()
                invalid_selection = False


def main():
    um = UserMenu()
    um.prompt_menu()

if __name__ == '__main__':
    main()

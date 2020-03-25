"""
todo docstring
"""
import traceback
import Inventory
from Store import Store
from OrderProcessor import OrderProcessor, Order


class UserMenu:
    """
    User Menu contains the logic to allow a user to do the following:
    1. Process Web Orders
    2. Check Inventory
    3. Exit the program with a daily transaction report.
    """

    @staticmethod
    def menu_order_processing():
        new_order_processing = OrderProcessor()
        new_order_processing.file_name_request()
        new_order_processing.read_order_file()
        print("Attempting to create orders")
        new_order_processing.create_order_from_order_file()

    def __init__(self):
        self.user_menu_map = {
            # todo test mapping
            "1": UserMenu.menu_order_processing,
            "2": Inventory,
            "3": Store.daily_transaction_report
        }

    def prompt_menu(self):
        """
        Prompts the user for input to access the three available options.
        1. Process Web Orders
        2. Check Inventory
        3. Exit the Program with a Transaction Report
        :return: None
        """
        invalid_selection = True
        while invalid_selection:
            option = input(
                "Welcome!\nSelect option by inputting a digit.\n"
                "1: Process Web Orders\n"
                "2. Check Inventory\n"
                "3. Exit Program\n"
                ">>>")
            try:
                menu_option_selected = self.user_menu_map[option]
            except (KeyError, ValueError) as e:
                traceback.print_tb(e)
                print("Invalid Selection")
            else:
                menu_option = menu_option_selected()
                invalid_selection == False
                if option == "3":
                    pass
                    #add transaction report
                #todo invalid_selection flag to false on 3 selection


def main():
    um = UserMenu()
    um.prompt_menu()

if __name__ == '__main__':
    main()

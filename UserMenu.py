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

user_menu_map = {
    # todo test mapping
    "1": OrderProcessor,
    "2": Inventory,
    "3": Store.daily_transaction_report
}


class UserMenu:
    """

    """

    def prompt_menu(self):
        """

        :return:
        """
        invalid_selection = True
        while invalid_selection:
            option = input("Welcome!\nSelect option by inputting a digit.\n"
                           "1: Process Web Orders\n"
                           "2. Check Inventory\n"
                           "3. Exit Program\n")
            try:
                menu_option_selected = user_menu_map[option]
            except (KeyError, ValueError) as e:
                traceback.print_tb(e)
                print("Invalid Selection")
            else:
                menu_option_selected()
                invalid_selection = False


def main():
    pass


if __name__ == '__main__':
    main()

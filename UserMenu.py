"""
User Menu contains the logic to allow a user to do the following:
1. Process Web Orders
2. Check Inventory

This is likely the client
"""
import traceback

user_menu_map = {
        "1": "ProcessWebOrders",  # todo function should go here
        "2": "CheckInventory" , # todo function should go here
        "3": exit  # exit the program todo may need some clean up function
    }
class UserMenu():
    def prompt_menu(self):
        invalid_selection = True
        while invalid_selection:
            input("Welcome!\nSelect option by inputting a digit.\n"
                  "1: Process Web Orders\n"
                  "2. Check Inventory\n"
                  "3. Exit Program\n")
            try:
                menu_option_selected = user_menu_map[input]
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

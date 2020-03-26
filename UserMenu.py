from Store import Store
from OrderProcessor import OrderProcessor, Order


class UserMenu:
    """

    """

    def __init__(self):
        self.store = Store()
        self.user_menu_map = {
            "1": self.store.menu_order_processing,
            "2": self.store.check_inventory,
            "3": self.store.daily_transaction_report
        }

    def prompt_menu(self):
        """

        :return:
        """
        invalid_selection = True
        menu_option = None
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
                if option == "3":
                    print("Exiting Program\n"
                          "Creating Daily Transaction Report")
                    invalid_selection = False


def main():
    um = UserMenu()
    um.prompt_menu()


if __name__ == '__main__':
    main()

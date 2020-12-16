import keyboard
import os


class Item:
    def __init__(self, text: str, options: list):
        self.above = False
        self.selected = False
        self.text = text
        self.options = options


    def print_options(self):
        clear_terminal()
        for i in self.options:
            print(i)


class Arrow:
    def __init__(self):
        self.above = None


class Menu:
    def __init__(self):
        self.items = []
        self.arrow = Arrow()
        self.selected_menu_option = 0


    def show(self):
        clear_terminal()
        for i in range(len(self.items)):
            if i == self.selected_menu_option:
                self.arrow.above = self.items[i]
                print(">>> {}".format(self.items[i].text))
            else:
                print(self.items[i].text)


    def up_arrow_pressed(self):
        if self.selected_menu_option == 0:
                self.selected_menu_option = len(self.items) - 1
        else:
            self.selected_menu_option -= 1

        self.arrow.above = self.items[self.selected_menu_option]
        self.show()


    def down_arrow_pressed(self):
        if self.selected_menu_option == len(menu.items) - 1:
                self.selected_menu_option = 0
        else:
            self.selected_menu_option += 1

        self.arrow.above = self.items[self.selected_menu_option]
        self.show()


def clear_terminal():
    """
    This function clears the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')



if __name__ == "__main__":
    i1 = Item('Item 1', ["Nome", "CPF", "Idade"])
    i2 = Item('Item 2', ["Idade"])
    i3 = Item('Item 3', ["Parentes"])
    menu = Menu()
    menu.items = [i1, i2, i3]
    menu.show()
    while True:
        if keyboard.read_key() == "q":
            print("You pressed q\nQuiting...")
            break

        elif keyboard.read_key() == "up":
            menu.up_arrow_pressed()

        elif keyboard.read_key() == "down":
            menu.down_arrow_pressed()

        elif keyboard.read_key() == "enter":
            menu.arrow.above.print_options()

        elif keyboard.read_key() == "backspace":
            menu.arrow.above.print_options()
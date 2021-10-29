from main_menu import main_menu
from products_menu import products_menu
from couriers_menu import couriers_menu
from orders_menu import orders_menu

#Required to run the app and avoid circular imports 
def main():
    main_menu.main_menu()

if __name__ == "__main__":
    main()

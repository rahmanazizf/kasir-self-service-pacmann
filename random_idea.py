class Cashier:

    item = {}

    def add_item():
        item_name = input("Item name: ")
        number_of_item = int(input("Number of item: "))
        price_per_item = int(input("Price per item: "))

        if item_name in Cashier.item:
            print("Item name already exist in database.\n")
            add_item()
        else:
            Cashier.item[item_name] = {'number of item': number_of_item,
                                        'price per item': price_per_item}
    
    def show_all():
        # show all item with tabulate

    def delete_item():
        print("you are about to delete an item.\n")
        item_name = input("Please input an item name: ")
        del Cashier.item[item_name]

    
        
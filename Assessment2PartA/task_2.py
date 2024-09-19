def requisitions_total():
    item_name = [] #this is the list which store the items which user enters
    price_of_total_items = 0
    while True:
            item = input("Enter the name of items (or typr end to finish) :")
            if item.lower() == 'end':
                       break
            try:
                price = float(input(f"Enter the label price of {item}: $"))
                item_name.append((item_name, price))
                price_of_total_items += price
            except ValueError:
                print("Invalid Price. Please Enter the number value for price")

    return item_name, price_of_total_items
    
def main():
    print("Name of items and label price")
    item_name, price = requisitions_total ()
        
    if not item_name:
            print("No item were found")
    else:
            print("\nList of items :")
            for item_name, price in item_name:
                    print("item,price:", item_name, price)
                    print("total_cost:", price_of_total_items)

main()








from HashTable import HashTable
from Product import BabyProduct

def menu():
    print('==========================')
    print('Baby Product Retail Shop')
    print('==========================')
    print('[1] Add Product')
    print('[2] Search Product')
    print('[3] Edit Product')
    print('[4] Delete Product')
    print('[5] Display All Product')
    print('[6] Exit')
    print('==========================')

def display_category(hash_table):
    #display all available category
    categories = hash_table.get_categories()

    if categories:
        print("\nAvailable product category:")
        for i, cat in enumerate(categories, 1):
            print(f"{i}) {cat}")

    else:
        print(f"\nCategories not available")

def add_product(hash_table):
    pid = input("Enter product ID: ")
    name = input("Enter product name:")
    category = input("Enter product category: ")

    try:
        price = float(input("Enter product price (RM): "))
        quantity = int(input("Enter product quantity"))

        #create the product object
        product = BabyProduct(pid, name, category, price, quantity)

        #insert into the hash_table
        #use the product category as the hash value
        hash_table.insert(category, product)

        print(f'Product added successfully!')

    except ValueError:
        print("Invalid input! Price must be a number and quantity must be an integer...")

def search_product(hash_table):
    display_category(hash_table)
    category = input("Enter product category to search: ")

    #search items by category
    products = hash_table.search(category)

    if products:
        print(f"\nFound {len(products)} product(s) in category '{category}'")
        print("=" * 30)
        for product in products:
            product.print()
        print("=" * 30)

    else:
        print(f"\nNo product(s) found in category '{category}'...")

def edit_product(hash_table):
    display_category(hash_table)
    category = input("Enter product category: ")

    products = hash_table.search(category)

    if not products:
        print(f"No product(s) found in category '{category}'...")
        return

    print("\nProducts in category '{category}'.")

    for i, product in enumerate(products, 1):
        print(f"{i}) {product.get_product_id()} - {product.get_name()}")

    product_id = input("\nEnter product ID to edit: ")

    print("\nLeave blank to keep current value (press ENTER to skip)")
    new_name = input("Enter new product name: ")
    new_price = float(input("Enter new price (RM): "))
    new_quantity = int(input("Enter new quantity: "))

    if hash_table.edit(category, product_id, new_name, new_price, new_quantity):
        print("\nProduct information updated successfully!")
    else:
        print("\nProduct ID not found...")

def delete_product(hash_table):
    display_category(hash_table)
    category = input("Enter product category: ")

    products = hash_table.search(category)

    #check for the products in the category
    if not products:
        print(f"\nProduct(s) not found in category {category}...")
        return

    print(f"\nProduct(s) in category '{category.upper()}'")

    for i, product in enumerate(products, 1):
        print(f"{i}) {product.get_product_id()} - {product.get_name()}")


def main():
    #initialize hash table with
    hashTable = HashTable(10)

    #insert some existing data
    # Clothing products
    hashTable.insert("clothing", BabyProduct("P001", "Baby Onesie", "Clothing", 15.99, 50))
    hashTable.insert("clothing", BabyProduct("P002", "Baby Socks Set", "Clothing", 8.99, 100))
    hashTable.insert("clothing", BabyProduct("P003", "Baby Hat", "Clothing", 12.50, 75))

    # Toys products
    hashTable.insert("toys", BabyProduct("P004", "Soft Plush Bear", "Toys", 25.99, 30))
    hashTable.insert("toys", BabyProduct("P005", "Rattle Set", "Toys", 10.99, 60))
    hashTable.insert("toys", BabyProduct("P006", "Building Blocks", "Toys", 35.00, 40))

    # Feeding products
    hashTable.insert("feeding", BabyProduct("P007", "Baby Bottle", "Feeding", 12.99, 80))
    hashTable.insert("feeding", BabyProduct("P008", "Sippy Cup", "Feeding", 9.99, 65))
    hashTable.insert("feeding", BabyProduct("P009", "Baby Spoon Set", "Feeding", 7.50, 90))

    # Diapering products
    hashTable.insert("diapering", BabyProduct("P010", "Diapers Pack", "Diapering", 29.99, 120))
    hashTable.insert("diapering", BabyProduct("P011", "Baby Wipes", "Diapering", 15.99, 150))
    hashTable.insert("diapering", BabyProduct("P012", "Changing Mat", "Diapering", 22.50, 45))


    while True:
        menu()
        try:
            option = int(input("Option: "))

            match option:
                case 1:
                    print("=== Add New Product ===")
                    add_product(hashTable)

                case 2:
                    print("=== Search Product === ")
                    search_product(hashTable)

                case 3:
                    print("=== Edit Product ===")
                    edit_product(hashTable)

                case 4:
                    print("=== Delete Product ===")
                    delete_product(hashTable)

                case 5:
                    print("=== Display All Product ===")
                    hashTable.display_all()

                case 6:
                    print("\nProgram terminated... Thank you for using!")
                    break

                case _:
                    print("\nInvalid option! Please select 1-6")

        except ValueError:
            print(f"\nInvalid input! Please enter a number.")
        except KeyboardInterrupt:
            print("\nExiting Program...")
            break


if __name__ == '__main__':
    main()



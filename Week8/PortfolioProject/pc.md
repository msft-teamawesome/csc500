### Pseudocode for Online Shopping Cart

1. **Class Definitions:**
   - **ItemToPurchase Class:**
     - Attributes: `item_name`,`item_price`,`item_quantity`
     - Methods: `print_item_cost'
   - **ShoppingCart Class:**
     - Attributes: `customer_name`, `current_date`, `cart_items`
     - Methods: `add_item(item)`, `remove_item(item_name)`, `modify_item(item)`, `print_total`,`print_descriptions'

2. **Main Functionality:**
   - **Prompt for Customer's Name and Date:**
     - Use `input' to get the customer's name.
     - Use `input' to get today's date.
     - Print the customer's name and today's date.
     - Create a `ShoppingCart` object with the provided name and date.

3. **Print Menu Function:**
   - Display menu options:
     - `a` - Add item to cart
     - `r` - Remove item from cart
     - `c` - Change item quantity
     - `i` - Output items' descriptions
     - `o` - Output shopping cart
     - `q` - Quit
   - **Handle User Choices:**
     - If `a`:
       - Prompt for item details (name, description, price, quantity).
       - Create an `ItemToPurchase` object with the provided details.
       - Add the item to the shopping cart.
     - If `r`:
       - Prompt for the name of the item to remove.
       - Call the `remove_item` method on the shopping cart with the provided name.
     - If `c`:
       - Prompt for the item name and new quantity.
       - Create an `ItemToPurchase' object with the provided name and new quantity.
       - Call the `modify_item` method on the shopping cart with the created item.
     - If `i`:
       - Call the `print_descriptions` method on the shopping cart.
     - If `o`:
       - Call the `print_total` method on the shopping cart.
     - If `q`:
       - Break the loop to quit.
     - Else:
       - Print "Invalid option. Please try again."

4. **Main Execution:**
   - Call the main functionality to prompt for customer details and print the menu.
from cart.cart import Cart


WelcomeMSG = """
Welcome to the F-Mart checkout system.
            Price List:
            +--------------|--------------|---------+
            | Product Code |     Name     |  Price  |
            +--------------|--------------|---------+
            |     CH1      |   Chai       |  $3.11  |
            |     AP1      |   Apples     |  $6.00  |
            |     CF1      |   Coffee     | $11.23  |
            |     MK1      |   Milk       |  $4.75  |
            |     OM1      |   Oatmeal    |  $3.69  |
            +--------------|--------------|---------+
            Auto Deails:
                1. BOGO -- Buy-One-Get-One-Free Special on Coffee. (Unlimited)
                2. APPL -- If you buy 3 or more bags of Apples, the price drops to $4.50.
                3. CHMK -- Purchase a box of Chai and get milk free. (Limit 1)
                4. APOM -- Purchase a bag of Oatmeal and get 50% off a bag of Apples
            Command options:
               - add: Add item by product code in cart
               - del: Remove item by product code from the cart
               - print: Show Cart items
               - clear: Reinitialize the cart
               - exit: Exit from the application
"""

ExitMSZ = """Thank you for shopping at F-Mart. Have a nice day!"""


def action(cart, action_type='Add'):
    while True:
        cmd = input(f'{action_type} an item using product code (enter "stop" to go back): ')
        if cmd == 'stop':
            return

        if action_type == 'Add':
            cart.add(cmd)
        else:
            cart.remove(cmd)


def main():
    print(WelcomeMSG)
    state = True
    cart = Cart()
    while state:

        command = input('Please enter a command: ')
        if command == 'add':
            action(cart, action_type='Add')
        elif command == 'del':
            action(cart, action_type='Remove')
        elif command == 'print':
            cart.print()
        elif command == 'clear':
            cart.clear()
        elif command == 'exit':
            state = False
            print(ExitMSZ)
        else:
            print(f'Command {command} is invalid. Please pick one of these commands: add, del, print, clear, exit.')


if __name__ == '__main__':
    main()

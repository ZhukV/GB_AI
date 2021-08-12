import re


class ProductManager:
    def __init__(self):
        self.products = []  # type: list[tuple[int, dict]]

    def add_product(self, insert_product):
        """
        :param touple insert_product: The product for insert
        """
        self.products.append(insert_product)

    def generate_attributes_map(self):
        """
        Generate a attributes map from product
        :rtype: list
        """
        attribute_maps = {}

        for product in self.products:
            for attribute_name, attribute_value in product[1].items():
                if not attribute_name in attribute_maps:
                    attribute_maps[attribute_name] = []

                if not attribute_value in attribute_maps[attribute_name]:
                    attribute_maps[attribute_name].append(attribute_value)

        return attribute_maps

    def make_product_item_from_stdin(self):
        """
        Make a product item with promp data in customer and read from stdin
        """

        name = input('Please enter a name of product: ')
        price = input('Please enter a price of product (only double supported): ')
        quantity = input('Please enter a available quantity (only int supported): ')
        units = input('Please enter a units: ')

        if not re.match(r'^\d+(\.(\d+))?$', price):
            raise TypeError('You are enter invalid price. Only double supported.')

        if not re.match(r'^\d+$', quantity):
            raise TypeError('You are enter invalid quantity. Only int supported.')

        return self.make_product_item(len(self.products) + 1, name, float(price), int(quantity), units)

    @staticmethod
    def make_product_item(identifier, name, price, quantity, units):
        """
        Make a one product item

        :param int identifier:
        :param str name:
        :param float price:
        :param int quantity:
        :param str units:
        """

        return (
            identifier,
            {
                'name': name,
                'price': price,
                'quantity': quantity,
                'units': units
            }
        )


def output_client_menu():
    print('Please choose operation: ')
    print('1 - add new product')
    print('2 - group attributes')
    print('3 - exit from application')


product_manager = ProductManager()

while True:
    output_client_menu()
    command = input('Please choose: ')

    if command == '1':
        product = product_manager.make_product_item_from_stdin()
        product_manager.add_product(product)
        continue

    elif command == '2':
        print('Possible products are:')
        print(product_manager.products)
        print('')
        print('Grouped attributes are:')
        print(product_manager.generate_attributes_map())

    elif command == '3':
        break

    else:
        print(f'The command {command} is\'t supported.')

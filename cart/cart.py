import copy

from .items import PRODUCTS


class Cart(object):

    def __init__(self):
        self.items = []
        self.item_qty = {
            'CH1': 0,
            'AP1': 0,
            'CF1': 0,
            'MK1': 0,
            'OM1': 0
        }
        self.chmk = False  # Ensure limit 1 for CHMK discount
        self.apom = False  # Ensure limit 1 for APOM discount

    @property
    def amount_total(self):
        amount_total = 0
        for item in self.items:
            amount_total += item['price']
            if 'discount' in item:
                amount_total += item['discount']
        return amount_total

    @staticmethod
    def print_item(item):
        print('{0:<18}{1:>17.2f}'.format(item['code'], item['price']/100))
        if 'promotion' in item:
            print(' '*12+'{0:<11}{1:>12.2f}'.format(
                item['promotion'], item['discount']/100))

    def print(self):
        print('{0:<18}{1:>17}($)'.format('Item', 'Price'))
        print('{0:<18}{1:>17}'.format('-'*4, '-'*5))
        for item in self.items:
            self.print_item(item)
        print('-'*35)
        print('{:>35.2f}'.format(self.amount_total/100))

    def add(self, code):
        item_code = code.upper()
        item = PRODUCTS.get(item_code)
        if item is None:
            print(f"Item {code} not exists.")
            return False
        item = copy.deepcopy(item)
        self.items.append(item)
        self.item_qty[item['code']] += 1
        self.compute_discount()
        self.print()
        return True

    def find(self, code):
        for index, item in enumerate(self.items):
            if item['code'] == code:
                return index
        return None

    def clear(self):
        self.items.clear()
        self.item_qty = dict.fromkeys(self.item_qty, 0)
        self.chmk = self.apom = False
        self.print()
        return True

    def remove(self, code):
        item_code = code.upper()
        item_index = self.find(item_code)
        if item_index is None:
            print(f"Item {code} not exists in cart.")
            return False
        del self.items[item_index]
        self.item_qty[item_code] -= 1
        self.compute_discount()
        self.print()
        return True

    def compute_discount(self):

        if self.item_qty['CF1'] >= 2:
            cf1_count = self.item_qty['CF1']
            coffee_qty = ((cf1_count - cf1_count % 2) / 2)
        else:
            coffee_qty = 0

        for item in self.items:
            if 'promotion' in item:
                item.pop('promotion', None)
                item.pop('discount', None)
                self.chmk = False
                self.apom = False

            # Apply Unlimited discount on Coffee
            if item['code'] == 'CF1' and coffee_qty >= 1:
                item['promotion'] = 'BOGO'
                item['discount'] = -1123
                coffee_qty -= 1

            # Apply Unlimited discount on Apples
            if self.item_qty['AP1'] >= 3 and item['code'] == 'AP1':
                item['promotion'] = 'APPL'
                item['discount'] = -150

            # Apply Limited discount on Milk with Chai
            if self.item_qty['OM1'] > 0 and self.item_qty['AP1'] > 0 and self.apom is False:
                if item['code'] == 'AP1':
                    item['promotion'] = 'APOM'
                    item['discount'] = -item['price'] / 2
                    self.apom = True

            # Apply Limited discount on Apples with Oatmeal
            if self.item_qty['CH1'] > 0 and self.item_qty['MK1'] > 0 and self.chmk is False:
                if item['code'] == 'MK1':
                    item['promotion'] = 'CHMK'
                    item['discount'] = -475
                    self.chmk = True

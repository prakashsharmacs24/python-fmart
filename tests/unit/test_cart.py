import pytest
from cart.cart import Cart
from cart.items import PRODUCTS


def price(code):
    return PRODUCTS[code]['price']


def get_cart(items):
    """Initialize cart with items"""
    cart = Cart()
    for item in items:
        cart.add(item)
    return cart


def test_cart_add():
    """Test inserting items into cart"""
    cart = Cart()
    res = cart.add("CH1")
    assert res is True
    assert len(cart.items) == 1

    res = cart.add("MK1")
    assert res is True
    assert len(cart.items) == 2

    res = cart.add("cH1")
    assert res is True
    assert len(cart.items) == 3


def test_cart_add_invalid_item():
    """Test inserting invalid item into cart"""
    cart = Cart()
    res = cart.add("XYZ")
    assert res is False


def test_cart_find():
    """Test finding item into cart"""
    cart = get_cart(items=['CH1', 'MK1'])
    assert cart.find('CH1') == 0
    assert not cart.find('XYZ')
    assert not cart.find('aP1')


def test_cart_remove():
    """Test removing items from cart"""
    items = ['CH1', 'AP1', 'AP1']
    cart = get_cart(items=items)
    assert cart.remove('AP1') is True
    assert len(cart.items) == len(items) - 1


def test_cart_remove_invalid():
    """Test removing invalid item from cart"""
    items = ['CH1', 'AP1', 'AP1']
    cart = get_cart(items=items)
    assert cart.remove('XYZ') is False
    assert len(cart.items) == len(items)


def test_cart_clear():
    """Test remove all items from cart"""
    items = ['CH1', 'AP1', 'AP1']
    cart = get_cart(items=items)
    cart.clear()
    assert len(cart.items) == 0


@pytest.mark.parametrize(
    "items,amount_total",
    [
        (['CH1'], price('CH1')),
        (['CH1', 'AP1'], price('CH1') + price('AP1')),
        (['AP1', 'AP1'], price('AP1') + price('AP1')),
        (['MK1', 'AP1'], price('MK1') + price('AP1')),
        (['MK1', 'OM1'], price('MK1') + price('OM1')),

    ])
def test_cart_amount_total_without_discount(items, amount_total):
    cart = get_cart(items=items)
    assert cart.amount_total == amount_total


def test_cart_amount_total_with_bogo_rule():
    """Test BOGO Rule
        Buy-One-Get-One-Free Special on Coffee. (Unlimited)

    """
    items = ['CF1', 'CF1', 'CF1', 'CF1', 'CF1']
    cart = get_cart(items=items)
    expected_amount_total = (
        (price('CF1') * (len(items) - len(items) % 2) / 2)
        + (len(items) % 2) * price('CF1')
     )
    assert cart.amount_total == expected_amount_total


def test_cart_amount_total_with_appl_rule():
    """Test APPL Rule
       Rule: If you buy 3 or more bags of Apples, the price drops to $4.50.

    """
    items = ['AP1', 'AP1', 'AP1', 'AP1']
    cart = get_cart(items=items)
    expected_amount_total = (price('AP1') - 150) * len(items)
    assert cart.amount_total == expected_amount_total


def test_cart_amount_total_chmk():
    """Test CHMK Rule
        Rule: Purchase a box of Chai and get milk free. (Limit 1)

    """
    cart = get_cart(items=['CH1', 'MK1', 'CH1', 'CH1', 'MK1'])
    expected_amount_total = price('CH1') * 3 + price('MK1') * 0 + price('MK1')
    assert cart.amount_total == expected_amount_total


def test_cart_amount_total_apom():
    """Test APOM Rule
        Purchase a bag of Oatmeal and get 50% off a bag of Apples

    """
    cart = get_cart(items=['OM1', 'AP1', 'AP1'])
    expected_amount_total = price('OM1') + price('AP1') + price('AP1') / 2
    assert cart.amount_total == expected_amount_total


def test_cart_removed_discount():
    """Test amount total after discount removal"""
    cart = get_cart(items=['AP1', 'AP1', 'AP1'])
    cart.remove('AP1')
    expected_amount_total = 600 * 2
    assert cart.amount_total == expected_amount_total

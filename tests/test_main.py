from ecommerce.discount import Discount
from ecommerce.main import create_country_list, select_country, create_country, make_product, create_basket, add_to_basket, buy_products
from ecommerce.country import ListCountries, Country
from ecommerce.basket import Basket
from ecommerce.product import Product

def test_create_country_list():
    country_list = create_country_list()
    assert isinstance(country_list, ListCountries)

def test_select_country():
    country_list = create_country_list()
    country = select_country(country_list, 'ES')
    assert isinstance(country, Country)

def test_create_country():
    country = create_country('United States', 'ES', '€')
    assert isinstance(country, Country)

def test_make_product():
    product = make_product('iPhone', 999.99, 'ES')
    assert isinstance(product, Product)

def test_create_basket():
    basket = create_basket()
    assert isinstance(basket, Basket)

def test_add_to_basket():
    basket = create_basket()
    product = make_product('iPhone', 999.99, 'ES')
    add_to_basket(basket, product, quantity=2)
    assert basket.get_total_items() == 2

def test_buy_products():
    basket = create_basket()
    product = make_product('iPhone', 999.99, 'US')
    add_to_basket(basket, product, quantity=2)
    result = buy_products(basket)
    assert isinstance(result, str)


def test_case_one_es():
    country_list = create_country_list()
    basket = create_basket()
    country = select_country(country_list, 'ES')
    product_es = make_product('product A', 50, 'ES')
    add_to_basket(basket, product_es, 2)
    result = buy_products(basket)
    assert result == '100 euros. Thank you for your purchase!'
    

def test_case_one_gb():
    country_list = create_country_list()
    basket = create_basket()
    country = select_country(country_list, 'GB')
    product_gb = make_product('product A', 55, 'GB')
    add_to_basket(basket, product_gb, 2)
    result = buy_products(basket)
    assert result == '99.0 euros. Thank you for your purchase!'

def test_case_one_it():
    country_list = create_country_list()
    basket = create_basket()
    country = select_country(country_list, 'IT')
    product_it = make_product('product A', 55, 'IT')
    add_to_basket(basket, product_it, 2)
    result = buy_products(basket)
    assert result == '82.5 euros. Thank you for your purchase!'

def test_case_two_es_65_euros():
    country_list = create_country_list()
    basket = create_basket()
    country = select_country(country_list, 'ES')
    discount = Discount(10)
    product_es_a = make_product('product A', 50, 'ES', discount)
    product_es_b = make_product('product B', 20, 'ES')
    add_to_basket(basket, product_es_a, 1)
    add_to_basket(basket, product_es_b, 1)
    basket.apply_promotion_code('promo5')
    result = buy_products(basket)
    assert result == '65.0 euros. Thank you for your purchase!'
    
def test_case_two_es_105_euros():
    country_list = create_country_list()
    basket = create_basket()
    country = select_country(country_list, 'ES')
    discount = Discount(10)
    product_es_a = make_product('product A', 50, 'ES', discount)
    product_es_b = make_product('product B', 20, 'ES')
    add_to_basket(basket, product_es_a, 2)
    add_to_basket(basket, product_es_b, 1)
    basket.apply_promotion_code('promo5')
    result = buy_products(basket)
    assert result == '105.0 euros. Thank you for your purchase!'
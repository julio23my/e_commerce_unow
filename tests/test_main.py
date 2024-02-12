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
    
def test_static_discount_5_euros():
    country_list = create_country_list()
    basket = create_basket()
    country = select_country(country_list, 'ES')
    discount_1_product_a = Discount(45, False, 3)
    discount_2_product_a = Discount(10, is_base=True)
    discount_product_a = [discount_1_product_a, discount_2_product_a]
    product_es_a = make_product('product A', 50, 'ES', discount_product_a)
    discount_by_quantity_1_product_b = Discount(5, False, 10)
    discount_by_quantity_2_product_b = Discount(10, True, 50)
    discount_by_quantity_3_product_b = Discount(20, True, 200)
    discounts_product_b = [discount_by_quantity_1_product_b, discount_by_quantity_2_product_b, discount_by_quantity_3_product_b]
    product_es_b = make_product('product B', 1.5, 'ES', discounts_product_b)
    add_to_basket(basket, product_es_a, 1)
    add_to_basket(basket, product_es_b, 1)
    basket.apply_promotion_code('promo100')
    result = buy_products(basket)
    assert result == '46.5 euros. Thank you for your purchase!'
    
    
    
def test_static_discount_3_9():
    country_list = create_country_list()
    basket = create_basket()
    country = select_country(country_list, 'ES')
    discount_1_product_a = Discount(45, False, 3)
    discount_2_product_a = Discount(10, is_base=True)
    discount_product_a = [discount_1_product_a, discount_2_product_a]
    product_es_a = make_product('product A', 50, 'ES', discount_product_a)
    discount_by_quantity_1_product_b = Discount(5, False, 10)
    discount_by_quantity_2_product_b = Discount(10, True, 50)
    discount_by_quantity_3_product_b = Discount(20, True, 200)
    discounts_product_b = [discount_by_quantity_1_product_b, discount_by_quantity_2_product_b, discount_by_quantity_3_product_b]
    product_es_b = make_product('product B', 1.5, 'ES', discounts_product_b)
    add_to_basket(basket, product_es_a, 3)
    add_to_basket(basket, product_es_b, 9)
    basket.apply_promotion_code('promo100')
    result = buy_products(basket)
    assert result == '103.5 euros. Thank you for your purchase!'
    
def test_static_discount_3_10():
    country_list = create_country_list()
    basket = create_basket()
    country = select_country(country_list, 'ES')
    discount_1_product_a = Discount(45, False, 3)
    discount_2_product_a = Discount(10, is_base=True)
    discount_product_a = [discount_1_product_a, discount_2_product_a]
    product_es_a = make_product('product A', 50, 'ES', discount_product_a)
    discount_by_quantity_1_product_b = Discount(5, False, 10)
    discount_by_quantity_2_product_b = Discount(10, True, 50)
    discount_by_quantity_3_product_b = Discount(20, True, 200)
    discounts_product_b = [discount_by_quantity_1_product_b, discount_by_quantity_2_product_b, discount_by_quantity_3_product_b]
    product_es_b = make_product('product B', 1.5, 'ES', discounts_product_b)
    add_to_basket(basket, product_es_a, 3)
    add_to_basket(basket, product_es_b, 10)
    basket.apply_promotion_code('promo100')
    result = buy_products(basket)
    assert result == '100.0 euros. Thank you for your purchase!'
    
def test_static_discount_3_60():
    country_list = create_country_list()
    basket = create_basket()
    country = select_country(country_list, 'ES')
    discount_1_product_a = Discount(45, False, 3)
    discount_2_product_a = Discount(10, is_base=True)
    discount_product_a = [discount_1_product_a, discount_2_product_a]
    product_es_a = make_product('product A', 50, 'ES', discount_product_a)
    discount_by_quantity_1_product_b = Discount(5, False, 10)
    discount_by_quantity_2_product_b = Discount(10, True, 50)
    discount_by_quantity_3_product_b = Discount(20, True, 200)
    discounts_product_b = [discount_by_quantity_1_product_b, discount_by_quantity_2_product_b, discount_by_quantity_3_product_b]
    product_es_b = make_product('product B', 1.5, 'ES', discounts_product_b)
    add_to_basket(basket, product_es_a, 3)
    add_to_basket(basket, product_es_b, 60)
    basket.apply_promotion_code('promo100')
    result = buy_products(basket)
    assert result == '171.0 euros. Thank you for your purchase!'
    
def test_static_discount_4_110():
    country_list = create_country_list()
    basket = create_basket()
    country = select_country(country_list, 'ES')
    discount_1_product_a = Discount(45, False, 3)
    discount_2_product_a = Discount(10, is_base=True)
    discount_product_a = [discount_1_product_a, discount_2_product_a]
    product_es_a = make_product('product A', 50, 'ES', discount_product_a)
    discount_by_quantity_1_product_b = Discount(5, False, 10)
    discount_by_quantity_2_product_b = Discount(10, True, 50)
    discount_by_quantity_3_product_b = Discount(20, True, 200)
    discounts_product_b = [discount_by_quantity_1_product_b, discount_by_quantity_2_product_b, discount_by_quantity_3_product_b]
    product_es_b = make_product('product B', 1.5, 'ES', discounts_product_b)
    add_to_basket(basket, product_es_a, 4)
    add_to_basket(basket, product_es_b, 110)
    basket.apply_promotion_code('promo100')
    result = buy_products(basket)
    assert result == '183.5 euros. Thank you for your purchase!'
    
def test_static_discount_6_200():
    country_list = create_country_list()
    basket = create_basket()
    country = select_country(country_list, 'ES')
    discount_1_product_a = Discount(45, False, 3)
    discount_2_product_a = Discount(10, is_base=True)
    discount_product_a = [discount_1_product_a, discount_2_product_a]
    product_es_a = make_product('product A', 50, 'ES', discount_product_a)
    discount_by_quantity_1_product_b = Discount(5, False, 10)
    discount_by_quantity_2_product_b = Discount(10, True, 50)
    discount_by_quantity_3_product_b = Discount(20, True, 200)
    discounts_product_b = [discount_by_quantity_1_product_b, discount_by_quantity_2_product_b, discount_by_quantity_3_product_b]
    product_es_b = make_product('product B', 1.5, 'ES', discounts_product_b)
    add_to_basket(basket, product_es_a, 6)
    add_to_basket(basket, product_es_b, 200)
    basket.apply_promotion_code('promo100')
    result = buy_products(basket)
    assert result == '365.0 euros. Thank you for your purchase!'
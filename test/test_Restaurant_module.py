import pytest
from Restaurant_modlue.Restaurant import calculate_total_price

# Define prices
pizza_price = {
    "Small": 5,
    "Medium": 7,
    "Large": 10
}
burger_price = {
    "Classic": 5,
    "Big": 7
}
drinks_price = 2
extra_cheese_price = 1
extra_ketchup_price = 1

@pytest.mark.parametrize("order_data", [
    # Existing cases
    {
        "pizza_qty": 2,
        "pizza_size": "Small",
        "burger_qty": 1,
        "burger_size": "Classic",
        "drinks_qty": 3,
        "extra_cheese": False,
        "extra_ketchup": False
    },
    {
        "pizza_qty": 1,
        "pizza_size": "Medium",
        "burger_qty": 2,
        "burger_size": "Big",
        "drinks_qty": 0,
        "extra_cheese": True,
        "extra_ketchup": False
    },
    {
        "pizza_qty": 3,
        "pizza_size": "Large",
        "burger_qty": 2,
        "burger_size": "Classic",
        "drinks_qty": 4,
        "extra_cheese": False,
        "extra_ketchup": True
    },
    {
        "pizza_qty": 0,
        "pizza_size": "Small",
        "burger_qty": 0,
        "burger_size": "Big",
        "drinks_qty": 0,
        "extra_cheese": False,
        "extra_ketchup": False
    },
    # Additional cases
    {
        "pizza_qty": 5,
        "pizza_size": "Medium",
        "burger_qty": 3,
        "burger_size": "Big",
        "drinks_qty": 2,
        "extra_cheese": True,
        "extra_ketchup": True
    },
    {
        "pizza_qty": 0,
        "pizza_size": "Large",
        "burger_qty": 5,
        "burger_size": "Classic",
        "drinks_qty": 1,
        "extra_cheese": False,
        "extra_ketchup": True
    },
    {
        "pizza_qty": 1,
        "pizza_size": "Small",
        "burger_qty": 0,
        "burger_size": "Classic",
        "drinks_qty": 0,
        "extra_cheese": True,
        "extra_ketchup": True
    },
    {
        "pizza_qty": 4,
        "pizza_size": "Large",
        "burger_qty": 0,
        "burger_size": "Big",
        "drinks_qty": 0,
        "extra_cheese": False,
        "extra_ketchup": False
    },
    {
        "pizza_qty": 1,
        "pizza_size": "Large",
        "burger_qty": 1,
        "burger_size": "Classic",
        "drinks_qty": 0,
        "extra_cheese": True,
        "extra_ketchup": False
    },
    {
        "pizza_qty": 2,
        "pizza_size": "Medium",
        "burger_qty": 2,
        "burger_size": "Big",
        "drinks_qty": 2,
        "extra_cheese": True,
        "extra_ketchup": True
    }
])
def test_calculate_total_price(order_data):
    expected_total = (
        order_data["pizza_qty"] * pizza_price[order_data["pizza_size"]] +
        order_data["burger_qty"] * burger_price[order_data["burger_size"]] +
        order_data["drinks_qty"] * drinks_price +
        order_data["extra_cheese"] * extra_cheese_price +
        order_data["extra_ketchup"] * extra_ketchup_price
    )
    assert calculate_total_price(**order_data) == expected_total

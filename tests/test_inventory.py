import pytest
from inventory import Inventory

def test_low_stock_all_items_above_threshold():
    inv = Inventory()
    inv.add_item("Apple", 10, 2.0)
    inv.add_item("Banana", 5, 3.0)

    assert inv.low_stock_items(3) == []

def test_low_stock_includes_equal_threshold():
    inv = Inventory()
    inv.add_item("Apple", 3, 2.0)
    inv.add_item("Banana", 5, 3.0)

    assert inv.low_stock_items(3) == ["Apple"]

def test_low_stock_sorted_by_name():
    inv = Inventory()
    inv.add_item("Orange", 2, 2.0)
    inv.add_item("Apple", 2, 2.0)
    inv.add_item("Banana", 1, 2.0)

    assert inv.low_stock_items(2) == ["Apple", "Banana", "Orange"]

def test_low_stock_empty_inventory():
    inv = Inventory()

    assert inv.low_stock_items(5) == []

def test_low_stock_threshold_zero():
    inv = Inventory()
    inv.add_item("Apple", 0, 2.0)
    inv.add_item("Banana", 1, 2.0)

    assert inv.low_stock_items(0) == ["Apple"]

def test_low_stock_negative_threshold():
    inv = Inventory()
    inv.add_item("Apple", 0, 2.0)

    assert inv.low_stock_items(-1) == []
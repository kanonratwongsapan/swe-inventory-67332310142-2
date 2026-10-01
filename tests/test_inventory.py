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


from inventory import InventoryItem


# --- Tests สำหรับ InventoryItem Validation ---

def test_inventory_item_validations():
    with pytest.raises(ValueError, match="ชื่อสินค้าต้องไม่ว่างเปล่า"):
        InventoryItem("", 10, 100.0)

    with pytest.raises(ValueError, match="ชื่อสินค้าต้องไม่ว่างเปล่า"):
        InventoryItem("   ", 10, 100.0)

    with pytest.raises(ValueError, match="จำนวนสินค้าต้องไม่ติดลบ"):
        InventoryItem("Item", -1, 100.0)

    with pytest.raises(ValueError, match="ราคาต้องมากกว่าศูนย์"):
        InventoryItem("Item", 10, 0.0)


# --- Tests สำหรับ Inventory: add_item ซ้ำ ---

def test_add_duplicate_item_raises_error():
    inv = Inventory()
    inv.add_item("Apple", 10, 2.0)
    with pytest.raises(ValueError, match="มีอยู่ในระบบแล้ว"):
        inv.add_item("Apple", 5, 2.0)


# --- Tests สำหรับ Inventory: restock ---

def test_restock_success():
    inv = Inventory()
    inv.add_item("Apple", 10, 2.0)
    assert inv.restock("Apple", 5) == 15


def test_restock_not_found():
    inv = Inventory()
    with pytest.raises(KeyError, match="ไม่พบสินค้า"):
        inv.restock("Unknown", 5)


def test_restock_invalid_amount():
    inv = Inventory()
    inv.add_item("Apple", 10, 2.0)
    with pytest.raises(ValueError, match="จำนวนที่เติมต้องมากกว่าศูนย์"):
        inv.restock("Apple", 0)


# --- Tests สำหรับ Inventory: sell ---

def test_sell_success():
    inv = Inventory()
    inv.add_item("Apple", 10, 2.0)
    assert inv.sell("Apple", 4) == 6


def test_sell_not_found():
    inv = Inventory()
    with pytest.raises(KeyError, match="ไม่พบสินค้า"):
        inv.sell("Unknown", 1)


def test_sell_invalid_amount():
    inv = Inventory()
    inv.add_item("Apple", 10, 2.0)
    with pytest.raises(ValueError, match="จำนวนที่ขายต้องมากกว่าศูนย์"):
        inv.sell("Apple", -1)


def test_sell_insufficient_stock():
    inv = Inventory()
    inv.add_item("Apple", 5, 2.0)
    with pytest.raises(ValueError, match="ไม่เพียงพอสำหรับการขาย"):
        inv.sell("Apple", 10)


# --- Tests สำหรับ Inventory: get_total_value ---

def test_get_total_value():
    inv = Inventory()
    assert inv.get_total_value() == 0.0
    inv.add_item("Apple", 2, 10.0)
    inv.add_item("Banana", 3, 20.0)
    assert inv.get_total_value() == 80.0
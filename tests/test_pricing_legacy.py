import pytest
import pricing_legacy as p


@pytest.fixture(autouse=True)
def reset_globals():
    p.member_points.clear()
    p.LOG.clear()


def test_calc_normal_price():
    assert p.calc([("Apple", 2, 10)]) == 21.4


def test_calc_bulk_discount_50():
    assert p.calc([("Apple", 50, 10)]) == 508.25


def test_calc_bulk_discount_100():
    assert p.calc([("Apple", 100, 10)]) == 963.0


def test_calc_zero_quantity_is_ignored():
    assert p.calc([("Apple", 0, 10)]) == 0.0


def test_calc_member_updates_points():
    assert p.calc([("Apple", 2, 10)], member="A") == 20.33
    assert p.member_points["A"] == 0


def test_calc_coupon_save50():
    assert p.calc([("Apple", 10, 10)], coupon="SAVE50") == 53.5
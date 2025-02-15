import pytest
import parentDir
import task4

def test_task4():
    # int price, int discount
    assert task4.calculate_discount(50, 20) == 40

    # float price, int discount
    assert task4.calculate_discount(19.99, 10) == 17.99

    # float price, float discount
    assert task4.calculate_discount(33.99, 33.3) == 22.67

    # int price, float discount
    assert task4.calculate_discount(15, 50) == 7.50

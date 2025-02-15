def calculate_discount(price, discount):
    finalPrice = price - (price * (discount * .01))
    return round(finalPrice, 2)


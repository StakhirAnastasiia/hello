import random
import math

def calculate_discount(price):
    discount = random.randint(5, 15)
    result = price * (100 - discount) / 100
    return math.floor(result * 100) / 100
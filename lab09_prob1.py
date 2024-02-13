"""
CISC 131 Problem 1 - Andrew Schmaderer (schm4013) and Harrison Amorim (Amor7967)
"""

def main():
    print(factors(31))
    print(exists(3,[1, 5, 3, 9]))
    print(gcd(15, 25))

def factors(num_input):
    factor = []
    i = 1
    while i <= num_input:
        if num_input % i == 0:
            factor.append(i)
        i = i + 1
    return factor

def exists(integer, input_list):
    bool_val = 0
    for item in input_list:
        if item == integer:
            bool_val = 1
    return bool(bool_val)

def gcd(integer_1, integer_2):
    list_1 = factors(integer_1)
    list_2 = factors(integer_2)
    factors_in_common = []
    for item_1 in list_1:
        for item_2 in list_2:
            if item_1 == item_2:
                factors_in_common.append(item_1)
    last_value = len(factors_in_common) - 1
    return factors_in_common[last_value]

main()

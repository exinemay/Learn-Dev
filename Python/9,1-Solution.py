price_of_house = 100000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price_of_house
else:
    down_payment = 0.2 * price_of_house
print(f'Down payment: {down_payment} USD')
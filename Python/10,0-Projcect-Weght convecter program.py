from lib2to3.pytree import convert


Weight = float(input('Your weight: '))
unit = input('(L)bs or (K)g: ')

if unit.upper() == "L":
    converted = Weight * 0.45
    print(f"You're {converted} kilos")
elif unit.upper() == "K":
    converted = Weight / 0.45
    print(f"You're {converted} pounds ")
else:
    print("Bạn đã nhập sai kí tự")
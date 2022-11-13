name = input('Hãy đặt tên: ')
if len(name) < 3:
    print("Too short")
elif len(name) > 25:
    print("Too long")
else:
    print("Name looks good!!")
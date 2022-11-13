'''
Giống như trong cấu trúc vi máy tính
Toán tử logic gồm: and, or, not
'''
oil_skin = True
dry_skin = False
if dry_skin and oil_skin:
    skin_name = 'da hỗn hợp'
elif dry_skin and not oil_skin:
    skin_name = 'da khô'
elif not dry_skin and oil_skin:
    skin_name = 'da dầu'
elif not dry_skin and not oil_skin:
    skin_name = 'da thường'

print(f'Da của bạn là {skin_name}')
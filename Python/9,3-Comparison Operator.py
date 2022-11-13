diem_tb = 10

if diem_tb >= 8:
    xep_loai = "giỏi"
else:
    if diem_tb >= 6.5:
        xep_loai = "khá"
    else:
        xep_loai = "kém"

print(xep_loai)
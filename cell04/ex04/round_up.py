
import math
user_input = input("กรุณาป้อนตัวเลข: ")
try:
    number = float(user_input)
    # คำนวณการปัดขึ้น
    rounded_number = math.ceil(number)
    print(f"ตัวเลขที่ปัดขึ้นคือ: {rounded_number}")
except ValueError:
    print("กรุณาป้อนตัวเลขที่ถูกต้อง")

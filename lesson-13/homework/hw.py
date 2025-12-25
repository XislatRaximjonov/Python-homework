from datetime import date

birth = input("Tug‘ilgan sanangizni kiriting (YYYY-MM-DD): ")
birth_date = date.fromisoformat(birth)
today = date.today()

years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

if days < 0:
    months -= 1
if months < 0:
    years -= 1
    months += 12

print(f"Yoshingiz: {years} yil, {months} oy")


from datetime import date

birth = input("Tug‘ilgan sana (YYYY-MM-DD): ")
b = date.fromisoformat(birth)
today = date.today()

next_birthday = date(today.year, b.month, b.day)
if next_birthday < today:
    next_birthday = date(today.year + 1, b.month, b.day)

print("Keyingi tug‘ilgan kungacha:", (next_birthday - today).days, "kun")


from datetime import datetime, timedelta

start = input("Boshlanish vaqti (YYYY-MM-DD HH:MM): ")
hours = int(input("Soat: "))
minutes = int(input("Daqiqa: "))

start_time = datetime.strptime(start, "%Y-%m-%d %H:%M")
end_time = start_time + timedelta(hours=hours, minutes=minutes)

print("Yig‘ilish tugaydi:", end_time)


from datetime import datetime
from zoneinfo import ZoneInfo

dt = input("Sana va vaqt (YYYY-MM-DD HH:MM): ")
from_zone = input("Hozirgi timezone (Asia/Tashkent): ")
to_zone = input("Qaysi timezone ga (Europe/London): ")

time = datetime.strptime(dt, "%Y-%m-%d %H:%M")
time = time.replace(tzinfo=ZoneInfo(from_zone))

print("Natija:", time.astimezone(ZoneInfo(to_zone)))


import time
from datetime import datetime

target = input("Kelajak vaqt (YYYY-MM-DD HH:MM:SS): ")
target_time = datetime.strptime(target, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    diff = target_time - now
    if diff.total_seconds() <= 0:
        print("Vaqt tugadi!")
        break
    print("Qolgan vaqt:", diff)
    time.sleep(1)

import re

email = input("Email kiriting: ")
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern, email):
    print("Email to‘g‘ri")
else:
    print("Email noto‘g‘ri")


phone = input("Telefon raqam (10 ta raqam): ")

formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
print("Format:", formatted)


password = input("Parol kiriting: ")

if (len(password) >= 8 and
    any(c.isupper() for c in password) and
    any(c.islower() for c in password) and
    any(c.isdigit() for c in password)):
    print("Parol kuchli")
else:
    print("Parol kuchsiz")


text = "Python is easy. Python is powerful."
word = input("So‘z kiriting: ")

positions = [i for i in range(len(text.split())) if text.split()[i] == word]
print("Topilgan joylar:", positions)


import re

text = input("Matn kiriting: ")
dates = re.findall(r"\d{4}-\d{2}-\d{2}", text)

print("Topilgan sanalar:", dates)

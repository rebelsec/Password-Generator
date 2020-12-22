import random

u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l = u.lower()
n = '1234567890'
s = '`~!@#$%^&*()_+\][|}{";:/.,?><'

print("""

Password Generator By :
 ____      _          _
|  _ \ ___| |__   ___| |___  ___  ___
| |_) / _ \ '_ \ / _ \ / __|/ _ \/ __|
|  _ <  __/ |_) |  __/ \__ \  __/ (__
|_| \_\___|_.__/ \___|_|___/\___|\___|

Note :
default : uppercase + lowecase + number + symbol
silahkan ganti True ke False jika ingin mengcostum password di dalam program
Misal : upper = False
""")

upper, lower, number, symbol = True, True, True, True

all = ""
if upper:
    all += u
if lower:
    all += l
if number:
    all += n
if symbol:
    all += s

length = int(input("Panjang Karakter ? : "))
rows = int(input("Banyak Baris ? :"))

for i in range(rows):
    passwords = "".join(random.sample(all, length))
    print(passwords, "\n")

i = int(input("i "))
base = int(input("base "))
r = ""
while i > 0:
    r = str(i % base) + r
    i //= base

print(r)

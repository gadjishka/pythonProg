# a = ""
a = "Переправа , переправа ,берег левый , берег правыыый"
print(a)
print(a[-1])
print(a[:9])
print(a[28:34])
print(a[37:])
print(a[-12:-1])
print(a[:9:3])
print(a[::-1])

print(len(a))
b = "   "
print(len(b))
print(a.upper())
print(a.lower())
print(a.title())
print(a.count("берег"))
print(a.find("берег"))
print(a.rfind("берег"))

print(a.lower().count("переправа"))
print(a.replace("берег", "крекер"))

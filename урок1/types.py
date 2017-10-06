buys = [" хлеб", "молоко" ,"телевизор","шуруповерт'Bosh'"]
print(buys[1])
print(buys[-1])
print(buys[1:])
buys.append("маска человека паука")
print(buys)
buys.insert(2, "маска человека паука")
print(buys)
another_buys = (" холодильник","плойка")
buys.extend(another_buys )
print(buys)

del buys[1]
print(buys)

buys.remove("плойка")
print(buys)
print(buys.pop(2))

print(buys)
# buys2 = buys
buys2 = buys[:]
del buys[2]
print(buys2)
print(buys)

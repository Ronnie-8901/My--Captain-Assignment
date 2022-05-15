F0 = 0
F1 = 1
Fn = 1
print(F0)
print(F1)
while Fn > 0:
    print(Fn)
    F0 = F1
    F1 = Fn
    Fn = F0 + F1

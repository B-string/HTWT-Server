class test:
    a = 9


l = []

t1 = test()
print(t1)
l.append(t1)
t1 = test()
print(t1)
l.append(t1)
t1 = test()
print(t1)
l.append(t1)

l[0].a = 10
l[1].a = 12
l[2].a = 14
print(l)

for i in l:
    print(i.a)

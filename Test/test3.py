so = int(input('So can tinh: '))
#
# print(len(so))

a=0
while so % 10 != 0:
    so //= 10
    a+=1

print('So chu so: ' + str(a))


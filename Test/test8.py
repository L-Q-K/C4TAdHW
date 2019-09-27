l = [1, 5, -9, 3]
inte = input('Vi tri can xoa ')

if inte.lower() == 'head':
    print(*l[1:(len(l))])
elif inte.lower() == 'tail':
    print(*l[:len(l)-1])
else:
    print('Khong xac dinh')
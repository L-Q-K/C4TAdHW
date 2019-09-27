l = [38,27,43,3,9,82,10]

def merge(l,r):
    res = []

    while (len(l)!=0) and (len(r)!=0):
        if l[0]<r[0]:
            res.append(l.pop(0))
        elif l[0]>r[0]:
            res.append(r.pop(0))

    res += l
    res += r

    return res

def sort(arr):
    if len(arr)==1:
        return arr
    else:
        mid = len(arr)//2
        left = sort(arr[:mid])
        right = sort(arr[mid:])

        return merge(left, right)

print(sort([12 ,11 ,13 ,5 ,6 ,7]))




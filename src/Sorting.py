def bubble(array):

    def _swap(x,y):
        tmp = array[x]
        array[x]=array[y]
        array[y]=tmp

    sort = True
    while sort:
        sort = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                _swap(i,i+1)
                sort = True
    return array

def merge(array):

    def _merge(l,r):
        print("merging: {} and {}".format(l,r))
        res = []
        while len(l) is not 0 and len(r) is not 0:
            if l[0] <= r[0]:
                res.append(l[0])
                l = l[1:]
            else:
                res.append(r[0])
                r = r[1:]
        for i in range(len(l)):
            res.append(l[i])
        for i in range(len(r)):
            res.append(r[i])
        print("Result: {} <--> {}  {}".format(res,l,r))
        return res

    if len(array) == 1:
        return array
    l1 = array[:len(array)//2]
    l2 = array[len(array)//2:]

    l1 = merge(l1)
    l2 = merge(l2)

    return _merge(l1,l2)

def count(array):
    res = []
    freq = {}
    for i in array:
        if i not in freq.keys():
            freq[i] = 1
        else:
            freq[i] += 1

    for i in freq.keys():
        for j in range(freq[i]):
            res.append(i)
    return res

def search(array):
    raise NotImplementedError

def bubble():
    raise NotImplementedError

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
    raise NotImplementedError

def search():
    raise NotImplementedError

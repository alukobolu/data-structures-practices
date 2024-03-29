class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self ,key):
        h=0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found = False
        for idx ,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[idx] = (key,val)
                found = True
                break
        if not found:
            self.arr[h].append((key,val))

    def  __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def  __delitem__(self,key):
        h = self.get_hash(key)
        for index , element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

t = HashTable()
# print("ans: ",t.get_hash('march 6'))
# print("ans: ",t.get_hash('march 17'))
t['march 6'] = 'bolu'
t['march 17'] = 'obani'
t['april 1'] = 'mum'
print("get: ",t['march 6'])
del t['april 1']
print("get: ",t.arr)
# class HashTable:
#     def __init__(self):
#         self.MAX = 100
#         self.arr = [None for i in range(self.MAX)]
#
#     def getHash(self,key):
#         h = 0
#         for char in key:
#             h += ord(char)
#         return h % self.MAX
#
#     def __setitem__(self, key, value):
#         h = self.getHash(key)
#         self.arr[h] = value
#
#     def __getitem__(self, key):
#         h = self.getHash(key)
#         return self.arr[h]
#
#     def __delete__(self, key):
#         h = self.getHash(key)
#         self.arr[h] = None
#
# if __name__ == '__main__':
#     t = HashTable()
#     t['march 3'] = 142
#     t['march 4'] = 150
#     t['march 10'] = 200
#     t['dec 1'] = 90
#     print(t.arr)
#     print(t['march 3'])
#     t.__delete__('march 3')
#     print(t.arr)
#


###################### Hash table collistion handling ######################

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h%self.MAX

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if  len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
        if not found:
            self.arr[h].append((key, value))

    def __delete__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("Del", index)
                del self.arr[arr_index][index]


t = HashTable()
t['march 6'] = 219
t['march 7'] = 239
t['march 8'] = 389
t['march 17'] = 3234

print(t.get_hash('march 6'))
print(t.get_hash('march 17'))
print(t.arr)
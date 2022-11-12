# word_count = {}
# with open("poem.txt","r") as f:
#     for line in f:
#         tokens = line.split(" ")
#         for token in tokens:
#             token = token.replace('\n', '')
#             if token in word_count:
#                 word_count[token] +=1
#             else:
#                 word_count[token] = 1
#
#
# print(word_count)


class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h = ord(char)
        return h%self.MAX

    def get_porb_length(self,index):
        return [*range(index, len(self.arr))] + [*range(0, index)]



HashMap = HashTable()
length = HashMap.get_porb_length(4)
print(length)
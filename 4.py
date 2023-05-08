# task 4
import re
seq = input('input the DNA sequence:')
seq = seq.upper()
FOXC1 = 'TATGTAAATAT'
FOXL1 = 'GTAAACA'
class find(object):
    def __init__(self):
        self.len = len(self)
    def position(self, tseq):
        location = []
        index = -1
        while True:
            index = tseq.find(self, index + 1)  # 如果匹配到一样的碱基，就继续匹配下一个，直到匹配结束或者失败
            if index == -1:
                break
            location.append(index)
        return location  # 返回值如果是-1，代表匹配不成功
if re.search(r'[^ATCG]', seq):
    print('The input is incorrect')
else:
    print('The input is correct')
    FOXC1_p = find.position(FOXC1, seq)  # print(FOXC1p)
    FOXL1_p = find.position(FOXL1, seq)  # print(FOXL1p)  print(type(FOXC1p[1])) type: int
    for i in FOXC1_p:
        for l in FOXL1_p:
            if i + len(FOXC1) - l < 0 or i + len(FOXC1) - l >= len(FOXC1) + len(FOXL1):
                print('can bind simultaneously')
            else:
                print('can not bind simultaneously')

# task 4
'''
Can two transcription factors bind at the same location in this DNA?
nonoverlapping
non ambiguise
'''
import re
seq=input('Please input the DNA sequence:')
seq=seq.upper()
FOXC1 = 'TATGTAAATAT' 
FOXL1 = 'GTAAACA'

class motifinseq(object):
   def __init__(self):
      self.len=len(self)
   def bindsites(self,tseq):
     position = []
     index=-1
     while True:
        index = tseq.find(self,index+1) #' ' is certain motif (what this mean?)
        if index==-1:
            break
        position.append(index)
     return position

if re.search(r'[^ATCG]',seq):
    print ('input is incorrect')
else: 
    print ('input is correct')
    FOXC1p=motifinseq.bindsites(FOXC1,seq)
    #print(FOXC1p)
    FOXL1p=motifinseq.bindsites(FOXL1,seq)  # print(FOXL1p) / print(type(FOXC1p[1])) type: int
    
    if FOXC1p[0]+len(FOXC1) <= FOXL1p[-1]:
       print("FOXC1 and FOXL1 CAN bind simultaneously.")
    elif FOXL1p[0]+len(FOXL1) <= FOXC1p[-1]:
       print("FOXC1 and FOXL1 CAN bind simultaneously.")
    else:
       print("FOXC1 and FOXL1 CANNOT bind simultaneously")

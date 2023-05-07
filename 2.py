import re
from itertools import product

# Import IUPAC ambiguity codes for nucleotide degeneracy
R = ['A', 'G']
K = ['G', 'T']
S = ['G', 'C']
Y = ['C', 'T']
M = ['A', 'C']
W = ['A', 'T']
B = ['C', 'G', 'T']
H = ['A', 'C', 'T']
N = ['A', 'C', 'G', 'T']
D = ['A', 'G', 'T']
V = ['A', 'C', 'G']

# There is no spacer directly for nucleotides in each resulting sequence
separator = ''

print('The potential binding motifs for FOXC1 are:')

""" 
use the fuction 'product' to caculate the Cartesian product to get possible combinations of the binding motifs for 
FOXC1 and FOXL1and use the fuction 'join' to convert each result to a string 
"""
for FOXC1_combinations in product(W, R, W, R, H, M, ['A'], ['A'], Y, ['A'], W):
    FOXC1_binding_motif = separator.join(FOXC1_combinations)
    print(FOXC1_binding_motif, end=' ')

# Start on another line
print('\n')

print('The potential binding motifs for FOXL1 are:')

for FOXL1_combinations in product(R, Y, M, ['A'], ['A'], ['A'], Y, ['A']):
    FOXL1_binding_motif = separator.join(FOXL1_combinations)
    print(FOXL1_binding_motif, end=' ')

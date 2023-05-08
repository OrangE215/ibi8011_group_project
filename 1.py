def check_binding(DNA):
    FOXC1 = 'TATGTAAATAT'
    FOXL1 = 'GTAAACA'
    if set(DNA).issubset('ACTG'):
        if FOXC1 in DNA or FOXL1 in DNA:
            print('FOCX1 or FOCXL1 can bind this DNA')
        else:
            print('Both FOCX1 and FOCXL1 can not bind this DNA')
    else:
        print('Warning! The input format is incorrect! Please use the capital letter "A" "C" "T" "G" to denote the nucleotide sequence of DNA')


dna_sequence = 'AGCGA'
check_binding(dna_sequence)

# define a function called check_binding
# define the binding sites for FOXC1 and FOXL1
# check whether the input format is correct, if not, give a warning.
# check if the input DNA contains the binding sites for FOXL1 or FOXC1, if so, print True. If not cases, print False.

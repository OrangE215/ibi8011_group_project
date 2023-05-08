def check_binding(DNA):
    FOXC1 = 'TATGTAAATAT'
    FOXL1 = 'GTAAACA'
    if set(DNA).issubset('ACTG'):
        if FOXC1 in DNA or FOXL1 in DNA:
            print("True")
        else:
            print("False")
    else:
        print("Warning! The input format is incorrect!")


dna_sequence = 'AGCGA'
check_binding(dna_sequence)

# define a function called check_binding
# define the binding sites for FOXC1 and FOXL1
# check whether the input format is correct, if not, give a warning.
# check if the input DNA contains the binding sites for FOXL1 or FOXC1, if so, print True. If not cases, print False.

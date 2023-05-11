import re


def check_binding_with_ambiguities(DNA):
    # Use regular expressions to express the ambiguities in FOXC1 or FOXL1
    FOXC1_ambiguities = '[T|A][A|G][T|A][G|A][T|A|C][A|C]AA[T|C]A[T|A]'
    FOXL1_ambiguities = '[G|A][T|C][A|C]AA[C|T]A'
    
    # Check whether the input format is correct. if not, give a warning
    if set(DNA).issubset('ACTG'):
        
        # Check if the ambiguities in FOXC1 or FOXL1 allow them to bind this DNA
        if re.search(FOXC1_ambiguities, DNA) and re.search(FOXL1_ambiguities, DNA):
            print('The ambiguities in both FOXC1 and FOXL1 allow the binding')
        elif re.search(FOXC1_ambiguities, DNA):
            print('The ambiguities in FOXC1 (not FOXL1) allow the binding')
        elif re.search(FOXL1_ambiguities, DNA):
            print('The ambiguities in FOXL1 (not FOXC1) allow the binding')
        else:
            print('The ambiguities in FOXC1 and FOXL1 don not allow the binding')
    else:
        print('Warning! The input format is incorrect!')


dna_sequence = 'AAAAAAAATAA'
check_binding_with_ambiguities(dna_sequence)

# define a function called check_binding_with_ambiguities
# define the binding sites with ambiguities for FOXC1 and FOXL1
# check whether the input format is correct, if not, give a warning
# check if the ambiguities in FOXC1 or FOXL1 allow them to bind this DNA, and present the result by 'check_binding_with_ambiguities(dna_sequence)'

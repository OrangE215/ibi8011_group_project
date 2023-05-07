import re


def check_binding_with_ambiguities(DNA):
    FOXC1_ambiguities = '[T|A][A|G][T|A][G|A][T|A|C][A|C]AA[T|C]A[T|A]'
    FOXL1_ambiguities = '[G|A][T|C][A|C]AAA[C|T]A'

    if set(DNA).issubset('ACTG'):
        if re.search(FOXC1_ambiguities, DNA) and re.search(FOXL1_ambiguities, DNA):
            result = 'The ambiguities in both FOXC1 and FOXL1 allow the binding'
        elif re.search(FOXC1_ambiguities, DNA):
            result = 'The ambiguities in FOXC1 allow the binding'
        elif re.search(FOXL1_ambiguities, DNA):
            result = 'The ambiguities in FOXL1 allow the binding'
        else:
            result = 'The ambiguities in FOXC1 and FOXL1 don not allow the binding'
    else:
        result = 'Warning! The input format is incorrect! Please use the capital letter "A" "C" "T" "G" to denote the nucleotide sequence of DNA.'

    return result


dna_sequence = 'ACAAAACA'
check = check_binding_with_ambiguities(dna_sequence)
print(check)

# define a function called check_binding_with_ambiguities
# define the binding sites with ambiguities for FOXC1 and FOXL1
# check whether the input format is correct, if not, give a warning
# check if the ambiguities in FOXC1 or FOXL1 allow them to bind this DNA, and present the result by 'check_binding_with_ambiguities(dna_sequence)'

import re

FOXC1 = 'TATGTAAATAT'
FOXL1 = 'GTAAACA'


def check_both_binding(DNA):
    FOXC1_position = [match.start() for match in re.finditer(FOXC1, DNA)]
    FOXL1_position = [match.start() for match in re.finditer(FOXL1, DNA)]
    if FOXC1_position == [] or FOXL1_position == []:  # Check if hve both motif
        return 'can not bind simultaneously'
    else:  # Check if there are at least two position with no overlap
        for i in FOXC1_position:
            for j in FOXL1_position:
                if i - j >= len(FOXC1):
                    return 'can bind simultaneously'
                if j - i >= len(FOXL1):
                    return 'can bind simultaneously'
        for j in FOXC1_position:
            for i in FOXL1_position:
                if j - i >= len(FOXL1):
                    return 'can bind simultaneously'
                if i - j >= len(FOXC1):
                    return 'can bind simultaneously'
        else:
            return 'can not bind simultaneously'


dna_sequence = "TATGTAAATATAAAAGTAAAC"
result = check_both_binding(dna_sequence)
print(result)

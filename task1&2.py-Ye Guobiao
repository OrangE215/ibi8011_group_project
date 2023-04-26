# task1
def has_foxc1_binding_site(dna_sequence):
    binding_motif = 'TATGTAAATAT'
    if binding_motif in dna_sequence:
        return True
    else:
        return False
    
def has_foxl1_binding_site(dna_sequence):
    binding_motif = 'GTAAACA'
    if binding_motif in dna_sequence:
        return True
    else:
        return False

# task2
def has_foxl1_binding_site(dna_sequence):
    binding_motif = 'GTAAACA'
    allowed_ambiguities = {'R': ['A', 'G'], 'K': ['G', 'T'], 'S': ['G', 'C'], 'Y': ['C', 'T'], 'M': ['A', 'C'], 'W': ['A', 'T']}

    for i, nucleotide in enumerate(binding_motif):
        if nucleotide in allowed_ambiguities.keys():
            # Check if the nucleotide is in the allowed ambiguity list
            if dna_sequence[i] not in allowed_ambiguities[nucleotide]:
                return False
        else:
            # If the nucleotide is not an allowed ambiguity, check if it matches the binding motif
            if dna_sequence[i] != nucleotide:
                return False
    
    # If all the nucleotides match the binding motif or the allowed ambiguities, return True
    return True

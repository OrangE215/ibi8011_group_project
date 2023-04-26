def events(dna_sequence):
    # Define the binding motif for FOXC1 and FOXL1
    foxc1_motif = "TATGTAAATAT"
    foxl1_motif = "GTAAACA"

    # Initialize counters for FOXC1 and FOXL1 binding events
    foxc1_count = 0
    foxl1_count = 0

    # Loop through the DNA sequence, counting non-overlapping binding events
    for i in range(len(dna_sequence) - len(foxc1_motif) + 1):
        # Check for FOXC1 binding motif
        if dna_sequence[i:i + len(foxc1_motif)] == foxc1_motif:
            # Increment FOXC1 counter and skip the binding site
            foxc1_count += 1
            i += len(foxc1_motif)

        # Check for FOXL1 binding motif
        elif dna_sequence[i:i + len(foxl1_motif)] == foxl1_motif:
            # Increment FOXL1 counter and skip the binding site
            foxl1_count += 1
            i += len(foxl1_motif)

        # Otherwise, continue searching for binding motifs
        else:
            continue

    # Return the maximum number of non-overlapping binding events
    return foxc1_count, foxl1_count
                                                                                                                                      

dna_sequence ="AAAAAAAAAAAAAAAAAAATGTAAATATTATGTAAATATTATGTAAATATTATGTAAATATTATGTAAATATTATGTAAATATGTAAACAGTAAACAGTAAACAGTAAACAGTAAACA"
events = events(dna_sequence)
print(events)

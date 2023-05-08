def count_instance(dna_sequence):
    # Define the binding motif for FOXC1 and FOXL1
    FOXC1 = "TATGTAAATAT"
    FOXL1 = "GTAAACA"

    # Initialize counters for FOXC1 and FOXL1 binding events
    foxc1_count = 0
    foxl1_count = 0

    # Loop through DNA, counting non-overlapping binding events
    for i in range(len(dna_sequence) - len(FOXC1) + 1):
        # Check for FOXC1 binding motif
        if dna_sequence[i:i + len(FOXC1)] == FOXC1:
            # Increment FOXC1 counter and skip the binding site
            foxc1_count += 1
            i += len(FOXC1)

        # Check for FOXL1 binding motif
        elif dna_sequence[i:i + len(FOXL1)] == FOXL1:
            # Increment FOXL1 counter and skip the binding site
            foxl1_count += 1
            i += len(FOXL1)

        # Otherwise, continue searching for binding motifs
        else:
            continue

    # Print the maximum number of non-overlapping binding events
    print(f"FOXC1 number: {foxc1_count} , FOXL1 number: {foxl1_count}")


dna_sequence = "AAATGTAAATATTATGTAAATATTATGTAAATATTATGTAAATATTATGTAAATATTATGTAAATATGTAAACAGTAAACAGTAAACAGTAAACAGTAAACA"
count_instance(dna_sequence)

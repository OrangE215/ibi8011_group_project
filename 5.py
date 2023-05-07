dna_sequence = "TATGTAAATATGTAAATATACGTATGTAAATAT"
FOXC1 = "TATGTAAATAT"
motif_count = 0
location = ""
overlap_count = 0
prev_loc = -1  # Initialize to -1, indicating that there was no previous match

for i in range(len(dna_sequence) - len(FOXC1) + 1):
    if dna_sequence[i:i + len(FOXC1)] == FOXC1:
        motif_count += 1  # Count the motif number
        location += str(i) + '-' + str(i + len(FOXC1)) + ','
        if prev_loc != -1 and i - prev_loc == 8:
            overlap_count += 1  # Check for overlaps with the previous match
        prev_loc = i  # Update the previous match location

print("motif count:", motif_count)
print("motif locations:", location[:-1])
print("overlap count:", overlap_count)

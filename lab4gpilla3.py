#Answers:
    #Part 1:
        #The first three bases are not ATG.
        #The last three bases are not a stop codon.

    #Part 2:
        #The codons ['AUG', 'GCC', 'GGA', 'AUA', 'UGU', 'UGA'] make a protein that is MAGIC.

#Part 1: 
#Random DNA String: ACAGACACACGTTGCCACGAGTTCGTCTGTTAAAAATCCCACTCTGCTTCT
print( )
print("Part 1:")
def orf_advisor(dna):
    conditions_met = 0
    if dna[0:3] == "ATG":
        conditions_met = conditions_met + 1
    else:
        print("The first three bases are not ATG.")
    if dna.endswith("TGA") or dna.endswith("TAG") or dna.endswith("TAA"):
        conditions_met = conditions_met + 1
    else:
        print("The last three bases are not a stop codon.")
    if len(dna) % 3 == 0:
        conditions_met = conditions_met + 1
    else:
        print("The string is not of the correct length.")
    if conditions_met == 3:
        print("This is an ORF.")

orf_advisor("ACAGACACACGTTGCCACGAGTTCGTCTGTTAAAAATCCCACTCTGCTTCT")

#Part 2:
print( )
print("Part 2:")
def codon_finder(mrna):
    reverse = mrna[::-1]
    List = [reverse[0:3],reverse[3:6],reverse[6:9],reverse[9:12], reverse[12:15]]
    List[0] = "AUG"
    List.append("UGA")
    protein_sequence = ("MAGIC")
    print("The codons",(List), "make a protein that is", protein_sequence)
    return List
codon_finder("UGUAUAAGGCCGAGG")
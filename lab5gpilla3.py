##Test causes and outputs:
#comp_nuc('A','DNA')
#Out[41]: 'T'

#comp_nuc('T','DNA')
#Out[42]: 'A'

#comp_nuc('C','DNA')
#Out[43]: 'G'

#comp_nuc('A','mRNA')
#Out[44]: 'U'

#comp_to_dna('ACTTGCGCA')
#Out[45]: 'TGAACGCGT'

#comp_to_rna('ACTTGCGCA')
#Out[46]: 'UGAACGCGU'

#gc_content("ACGGCGTTGCAACTTTCAGGGCCTAATCTGACCGTTCTAG")
#Out[47]: '52%'

## PART 1:
def comp_nuc(x,y):
    if y == "DNA":
        if x == "A":
            return "T"
        elif x == "C":
            return "G"
        elif x == "T":
            return "A"
        elif x == "G":
            return "C"
    else:
        if x == "A":
            return "U"
        elif x == "C":
            return "G"
        elif x == "T":
            return "A"
        elif x == "G":
            return "C"

## PART 2:
def comp_to_dna(DNA):
    a = []
    DNA_list = list(DNA)
    for base in DNA_list:
        if base == "A":
            a.append("T")
        elif base == "C":
            a.append("G")
        elif base == "T":
            a.append("A")
        elif base == "G":
            a.append("C")
    return ''.join(a)

## PART 3:
def comp_to_rna(DNA_string):
    b = []
    DNA_string_list = list(DNA_string)
    for base in DNA_string_list:
        if base == "A":
            b.append("U")
        elif base == "C":
            b.append("G")
        elif base == "T":
            b.append("A")
        elif base == "G":
            b.append("C")
    return ''.join(b)

## PART 4:
def gc_content(nucleotide):
    GC = 0
    for base in nucleotide:
        if base == "G" or base =="C":
            GC += 1
            GC_content = "{:.0%}".format(sum(base in "GC" for base in nucleotide) / len(nucleotide))
    return GC_content
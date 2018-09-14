gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

## Part 1:

def translate_dna(DNA):
    '''Translates the DNA sequence'''
    answer = []
    DNA = DNA.upper()
    if 'ATG' in DNA:
        ATG = DNA.find('ATG')
        DNA = DNA[ATG:]
        DNA_list = [DNA[i:i+3] for i in range(0, len(DNA), 3)] #Creates a list by splitting the sequence into 3 codons.
        for codon in DNA_list:
            if len(codon) == 3:
                if codon in gencode:
                    answer.append(gencode[codon])
                else:
                    answer.append('X')
        return ''.join(answer)
    else:
        DNA_list = [DNA[i:i+3] for i in range(0, len(DNA), 3)] #Creates a list by splitting the sequence into 3 codons.
        for codon in DNA_list:
            if len(codon) == 3:
                if codon in gencode:
                    answer.append(gencode[codon])
                else:
                    answer.append('X')
        return ''.join(answer)

## Part 2:

def translate_reverse(DNA):
    '''Gets the reverse compliment of a DNA sequence'''
    DNA = DNA.upper()
    Compliment = str.maketrans('ACTG','TGAC') #Found str.maketrans and translate in "7.3: String methods" of zybooks. There is a link that takes you to all available string methods you can use. The link can be found in the comparing strings section of string methods.
    DNA_compliment = DNA.translate(Compliment)
    DNA_reverse = DNA_compliment[::-1]
    return translate_dna(DNA_reverse)

#Test Sequence from Genbank:
    
    # Accession Number: GQ366753
    # Sequence: CGTCCAGCAGGTAGCTGTAAGTAGTTCAAGACTGTGTATGGCCATCTGCAGCCCACAGTTTTTAGCTTCTCCAAAATGACCATATTCTGTCCACATTCTTTATCCCTTTCTATCTATAAGCCTACCACACTCCAGACTCACCCAGTCAGCAGTGC
   
    # Output for translate_dna with selected sequence: 
    #             'MAICSPQFLASPK_PYSVHILYPFLSISLPHSRLTQSAV'
    
    # Output for translate_reverse with selected sequence: 
    #             'MWTEYGHFGEAKNCGLQMAIHSLELLTATCWT'
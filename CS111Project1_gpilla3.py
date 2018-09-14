##I worked with Vishal Patel in certain parts of the program.
##I was able to also get help from the T.A's Daisy and Lola through Vishal
##I also used Stack Overflow as a refence as well.


def get_orf(DNA):
    myList = ["TAG", "TGA", "TAA"]
    n_DNA = range(0, len(DNA),3)
    for index in n_DNA:
        codon = DNA[index: index + 3]
        if codon in myList:
            answer = DNA[0:index]
            return answer      

def one_frame(DNA):
    Answer = []
    start = "ATG"
    n_DNA = range(0, len(DNA), 3)
    for index in n_DNA:
        if DNA[index:index + 3] == start:
            Answer.append(get_orf(DNA[index: len(DNA)]))
    return Answer

def find_all_orfs(DNA):
    answer_1 = one_frame(DNA[0:len(DNA)])
    answer_2 = one_frame(DNA[1:len(DNA)])
    answer_3 = one_frame(DNA[2:len(DNA)])
    '''removes none types if there are any from the list'''
    while None in answer_1:
        answer_1.remove(None)
    while None in answer_2:
        answer_2.remove(None)
    while None in answer_3:
        answer_3.remove(None)
    return answer_1 + answer_2 + answer_3

def gc_content(nucleotide):
    GC = 0
    for base in nucleotide:
        if base == "G" or base == "C" and None not in base:
            GC += 1
        GC_content = sum(base in "GC" for base in nucleotide) / len(nucleotide)
        return GC_content

def gene_finder(file_name, min_len, minGC):
    answer = []
    with open(file_name) as file:
        sequence = file.read()
        sequence = find_all_orfs(sequence)
        for orf in sequence:
            _len = len(orf)
            GC_total = gc_content(orf)
            if (_len >= min_len and GC_total >= minGC):
                answer.append([orf,_len, GC_total])
        return answer
        file.close()
       
#Best Gene found from the Salmonella sequence(X73525.1):
# ['ATGTCGCACCGCCGTCTTACGCTTCACGCGTTGGCGTCCGTGAACCGC', 48, 0.6458333333333334]
# Human Readable Form: 'ATGTCGCACCGCCGTCTTACGCTTCACGCGTTGGCGTCCGTGAACCGC'
# This gene has a GC content of 0.6458333333333334 and lenght of 48.
# I found about 12 genes in total, but I selected that gene because of it's-
# high enough GC content and good lenght. There were genes that had a high 
# lenght, but it had a low GC content. There were also genes with higher GC
# Content, but I didn't pick that because it wasn't long enough.

#Blastx:

# The likely function of my gene might be to find other organisms that have 
# similar genes. It can help find cure for similar diseases since the gene is 
# for salmonella.

#The name of the gene similar to my best gene sequence is:
# EscN/YscN/HrcN family type III secretion system ATPase [Salmonella enterica]
# it's lenght is: 431 and It has a GC content of 0.09048723897911833
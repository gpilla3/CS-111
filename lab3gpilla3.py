#Part 1: 
# Name: Pelargonium Worcesterae
# Accession ID: KU535510.1
# FASTA Link: https://www.ncbi.nlm.nih.gov/nuccore/KU535510.1?report=fasta
# The gene product that I selected is a Pelargonium Worcesterae,
# which is a a new species of a section of Ligularia from southeast
# of Worcester. It belongs to the Geraniaceae family and has white of 
# pale pink flowers with petals that are 15 - 20 mm long. Pelargonium 
# can also be shrubs, succulent and mostly evergreen. It's most suitable 
# for use in containers like window boxes. It should be grown in fertile
# well drained soil in front of the sun or with a partial shade, and can
# be grown outside in the summer.

# Answers: 

# Total lenght of the gene is 912

# There are 283 A's
# There are 183 C's
# There are 248 T's
# There are 198 G's

# %A = 31.0 %
# %C = 20.1 %
# %T = 27.2 %
# %G = 21.7 %

# Total number of Amino Acids produced: 304

#Part 2a:
        
def DNA(sequence):
    A = sequence.count('A')
    C = sequence.count('C')
    T = sequence.count('T')
    G = sequence.count('G')
    total = A + C + T + G
    print("Total lenght of the gene is", total)
    print()
    
#Part 2b:
    
    print("There are", A , "A's")
    print("There are", C , "C's")
    print("There are", T , "T's") 
    print("There are", G , "G's")
    print()
    
#Part 2c:
    
    print("%A =", round((A/total * 100),1), '%') 
    print("%C =", round((C/total * 100),1), '%') 
    print("%T =", round((T/total * 100),1), '%') 
    print("%G =", round((G/total * 100),1), '%')
    print()
    
#Part 2d:
    
    print("Total number of Amino Acids produced:", int(total//3))
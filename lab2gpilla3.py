# -*- coding: utf-8 -

#Run the program to execut the first part. 
# Call the function get_codon() to execute the second part.

#Part 1:
    
DNA_string = input('Enter a DNA String: ')

A = DNA_string.count('A')
C = DNA_string.count('C')
T = DNA_string.count('T')
G = DNA_string.count('G')

total_count = A + C + T + G
print("The total lenght of the DNA string is", total_count)

#Part 2:

def get_codon(DNA):
    print(DNA[0:3])
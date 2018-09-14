## Part 1:

def get_orf(DNA):
    n = 3
    y = [DNA[i:i+n] for i in range(0, len(DNA), n)] 
    '''Turns the input into a list'''
    for i in range(0, len(DNA), 3):
        if DNA[i:i+3] == "TAG":
            z = y.index("TAG")
            return ''.join(y[0:z])
        elif DNA[i:i+3] == "TAA":
            w = y.index("TAA")
            return ''.join(y[0:w])
        elif DNA[i:i+3] == "TGA":
            g = y.index("TGA")
            return ''.join(y[0:g])
        else:
            return ''.join(y)

def one_frame(DNA):
    List = []
    y = 0
    lenght = len(DNA)
    start = "ATG"
    while y < lenght:
        new_seq = DNA[y:y+3]
        if new_seq == start:
            List.append(get_orf(DNA[y:]))
            print(List)
            y += len(get_orf(DNA[y:]))
        else:
            y += 3
    return List

## Part 2:

def read_seq(file_name,num_sequence):
    file = open(file_name, 'r')
    Outputted_List = []
    for line in file:
        strip = line.strip()
        if not strip.startswith(">"):
            list_answer = [line.rstrip()]
            list_answer = ''.join(list_answer)
            print("'{}'".format(list_answer))
            print("")
            Outputted_List.append(len(list_answer))
    return Outputted_List[:num_sequence]
    file.close()
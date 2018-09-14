import random as rdm
import matplotlib.pyplot as plt

# Part 1:
def make_founders(blue,purple,red):
    '''Appends corresponding letter to a list for how ever many times entered for each allel'''
    ans = []
    for a in range(0,blue):
        ans.append('b')
    for b in range(0,purple):
        ans.append('p')
    for c in range(0,red):
        ans.append('r')
    rdm.shuffle(ans)
    return (ans)

# Part 2:
def mate_pair_once(a1,a2):
    fin = []
    if a1 == 'r' and a2 == 'r':
        return 'r'
    if a1 == 'b' and a2 == 'b':
        return 'b'
    if a1 == 'p' and a2 == 'p':
        return rdm.choice('rpb')
    if a1 == 'r' and a2 == 'b':
        return 'p'
    if a1 == 'b' and a2 == 'r':
        return 'p'
    if a1 != a2:
        fin = [a1,a2]
        return rdm.choice(fin)

# Part 3:
def mate_pair(a2,a3,gen):
    '''appends mate_pair_once into list for how ever many gen entered'''
    end = []
    for i in range(gen):
        end.append(mate_pair_once(a2,a3))
    return end

# Part 4:
def create_generation(myL, offspring):
    ans = []
    List = [l[0] for l in myL]
    rdm.shuffle(List)
    while List:
        if len(List) % 2 == 0: #Checks if the lenght of List is even
            while List: #Loop runs as long as there are contents within the List
                pop1 = List.pop(0)
                pop2 = List.pop(0)
                for num in range(offspring): #appends mate_pair_once into list for number of offsprings needed
                    ans.append(mate_pair_once(pop1,pop2))
            return ans
        else:
            List.pop() #pops the last item from the List
            continue #Goes back to the beginning of the loop once the list is even again

# Part 5:
def calc_freq(myL):
    '''Calculates the fraction of p's, b's, and r's in the list as a float'''
    p = myL.count('p')
    r = myL.count('r')
    b = myL.count('b')
    l = len(myL)
    return [r/l, p/l, b/l]

# Part 6:
def pop_sim(red, purple, blue, ofs, gen):
    ge = list(range(gen)) #creates a list for the range in the gen number entered
    p = []
    r = []
    b = []
    x = make_founders(blue,purple,red)
    for num in range(gen): #runs the loop for gen number entered
        ans = create_generation(x,ofs)
        x = ans
        freq = calc_freq(ans)
        r.append(freq[0]),p.append(freq[1]),b.append(freq[2])
        #print(freq)
    plt.plot(ge,r, color = 'r', label = 'red')
    plt.plot(ge,p, color = 'm', label = 'purple')
    plt.plot(ge,b, color = 'b', label = 'blue')
    plt.legend(loc = 'upper right')
    plt.ylim(ymin=0)
    plt.xlim(xmin=[0,gen])
    plt.xlabel('Generation')
    plt.ylabel('Frequency')
    plt.title("Population Frequency")
    plt.show()

# To see the frequency outputs when you run the program just activate line 80

# Frequency outputs of the sample graph included in the turned in project:
# In [6]: pop_sim(2,2,2,3,20)
# [0.3333333333333333, 0.2222222222222222, 0.4444444444444444]
# [0.0, 0.9166666666666666, 0.08333333333333333]
# [0.3333333333333333, 0.4444444444444444, 0.2222222222222222]
# [0.2222222222222222, 0.5925925925925926, 0.18518518518518517]
# [0.2564102564102564, 0.5384615384615384, 0.20512820512820512]
# [0.3508771929824561, 0.45614035087719296, 0.19298245614035087]
# [0.21428571428571427, 0.5952380952380952, 0.19047619047619047]
# [0.25396825396825395, 0.4126984126984127, 0.3333333333333333]
# [0.23809523809523808, 0.4603174603174603, 0.30158730158730157]
# [0.2553191489361702, 0.4219858156028369, 0.32269503546099293]
# [0.2293144208037825, 0.4397163120567376, 0.3309692671394799]
# [0.2527646129541864, 0.4344391785150079, 0.3127962085308057]
# [0.23523206751054854, 0.45358649789029537, 0.3111814345991561]
# [0.23347398030942335, 0.4578059071729958, 0.30872011251758086]
# [0.2203469292076887, 0.48851383028598216, 0.2911392405063291]
# [0.23983739837398374, 0.4549718574108818, 0.3051907442151345]
# [0.23410464873879508, 0.46612466124661245, 0.29977069001459244]
# [0.2349179872115652, 0.45843758687795383, 0.30664442591048097]
# [0.2346399777592438, 0.4589936057825966, 0.3063664164581596]
# [0.23286994130367625, 0.46617238183503246, 0.3009576768612913]
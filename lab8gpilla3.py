import matplotlib.pyplot as plt
import csv
import random

#Part 1:
    
def plot_data(data_file, x, y):
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []
    with open(data_file, 'r') as d:
        data = csv.reader(d)
        '''Adds a title to the x and y axis based on which column is chosen'''
        if x == 0:
            titlex = 'Sepal Length'
            plt.xlabel(titlex)
            plt.show()
        if x == 1:
            titlex = 'Sepal Width'
            plt.xlabel(titlex)
            plt.show()
        if x == 2:
            titlex = 'Petal Length'
            plt.xlabel(titlex)
            plt.show()
        if x == 3:
            titlex = 'Petal Width'
            plt.xlabel(titlex)
            plt.show()
        if y == 0:
            titley = 'Sepal Length'
            plt.ylabel(titley)
            plt.show()
        if y == 1:
            titley = 'Sepal Width'
            plt.ylabel(titley)
            plt.show()
        if y == 2:
            titley = 'Petal Length'
            plt.ylabel(titley)
            plt.show()
        if y == 3:
            titley = 'Petal Width'
            plt.ylabel(titley)
            plt.show()
        '''Adds points to a list depending on which species is being plotted'''
        for row in data:
            if row[4] == 'Iris-setosa':
                x1.append(float(row[x]))
                y1.append(float(row[y]))
            if row[4] == 'Iris-versicolor':
                x2.append(float(row[x]))
                y2.append(float(row[y]))
            if row[4] == 'Iris-virginica':
                x3.append(float(row[x]))
                y3.append(float(row[y]))
        '''plots the points of each species with it's corresponding name for the label'''
        plt.scatter(x1,y1, color='r', label= 'Iris-setosa')
        plt.scatter(x2,y2, color='g', label= 'Iris-versicolor') 
        plt.scatter(x3,y3, color='b', label= 'Iris-virginica')
        plt.title("Plot_data")
        plt.show()
        plt.legend()
        plt.show()

#Part 2:
    
def plot_random(fname, x4, y4, n):
    x5 = []
    y5 = []
    randx = []
    randy = []
    with open(fname, 'r') as f:
        data_2 = csv.reader(f)
        '''Adds points to a list'''
        for row in data_2:
            x5.append(float(row[x4]))
            y5.append(float(row[y4]))
            '''finds the max and min of the list'''
            minx = min(x5)
            maxx = max(x5)
            miny = min(y5)
            maxy = max(y5)
        '''plots random points based on the 'n' numbers chosen and adds it to a list'''
        for nums in range(n):
            randx.append(random.uniform(minx,maxx))
            randy.append(random.uniform(miny,maxy))
        '''plots the random x and y points'''
        plt.scatter(randx,randy, label='Random points')
        plt.title("Plot_random")
        plt.legend()

plot_data("bezdekIris.data.csv",0,1)
#plot_random("bezdekIris.data.csv",0,1,50)

## The graph looked qualitatively similar and that might be due to the fact 
## that the same columns were used in each row as the x and y points.
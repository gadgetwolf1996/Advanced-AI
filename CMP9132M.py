import csv
#1a
def probOfOne(value):
    disease = 1.0/float(value)
    #print("The probability of having the disease is " + str(disease))
    return disease

def calculatingT(value):
    return ((0.99*value)+((1-0.95)*(1-value)))

def probAnB(a, b):
    return a*b

def probAgivenB(a, b, ab = 0 ):
    return a * ab / b

def notAB(a, b):
    na = 1 - a
    nb = 1 - b
    return probAgivenB(na, nb)

def diseaseProbability():
    print("Please input the probability of the disease being true")
    d = input()
    d = probOfOne(d)
    t = calculatingT(d)
    td = 0.99
    ntnd = 0.95
    print("P(t) = " + str(t))
    print("P(t|d) = " + str(td))#probAgivenB(t, probOfOne(d))
    print("P(¬t|¬d) = " + str(ntnd))#notAB(t, probOfOne(d))

    print("P(d|t) = " + str(probAgivenB(d,t, td)))


#1b
class Node():
    def __init__(self, n, p, pa, ch):
        self.name = n
        self.prob = p
        self.parents = pa
        self.children = ch
    
def AgivenBandC(a,b,c):
    return 

def bayes(filename):
    table = ['n']
    with open(filename, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',') 
        line_count = 0      
        for row in csv_reader:
            line_count += 1
            for c in row:
                if(c == '0' or c == '1'):
                    if(table[0] == 'n'):
                        table[0] = c
                    else:
                        table.append(c)
        print(f'Processed {line_count} lines.')
    


    #use len() to work out the titles from the values.
    #group[0] = Node(csv_file["smoking"])

#main
def main():
    print("Which task do you want to run?")
    i = input()
    if i == "1a":
        diseaseProbability()
    elif i == "1b":
        print("Filename: ")
        bayes(input())
    elif i == "2":
        pass
    else:
        print("Input not valid, try again")
        main()

if __name__ == "__main__":
    main()
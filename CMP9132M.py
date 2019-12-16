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

#2
class Task2():
    def __init__(self):
        #self.on = [0.4,0.4,0.2]
        #self.off = [0.45,0.45,0.1]
        #self.switch = 0.3
        #self.transition = 0.0
        
        # Transition Probabilities
        self.stay = 0.7
        self.switch = 0.3
        # Initial Probabilities
        self.on = 7/10
        self.off = 3/10
        # Emission Probabilities
        self.onh = 0.4
        self.onw = 0.4
        self.onc = 0.2
        self.offh = 0.1
        self.offw = 0.45
        self.offc = 0.45

        self.sequence = ['C','W','H','W','C']
        self.probabilities = []
        self.temperature = []

    def initialise(self):
        if self.sequence[0] == 'H':
            self.probabilities.append((self.on*self.onh,self.off*self.offh))
        elif self.sequence[0] == 'W':
            self.probabilities.append((self.on*self.onw,self.off*self.offw))
        else:
            self.probabilities.append((self.on*self.onc,self.off*self.offc))
        
    def calculate(self):
        for i in range(1, len(self.sequence)):
            last_on, last_off = self.probabilities[-1]
            if self.sequence[i] == 'H':
                this_on = max(last_on*self.stay*self.onh, last_off*self.switch*self.onh)
                this_off = max(last_on*self.switch*self.offh, last_off*self.stay*self.offh)
                self.probabilities.append((this_on, this_off))
            elif self.sequence[i] == 'W':
                this_on = max(last_on*self.stay*self.onw, last_off*self.switch*self.onw)
                this_off = max(last_on*self.switch*self.offw, last_off*self.stay*self.offw)
                self.probabilities.append((this_on, this_off))
            else:
                this_on = max(last_on*self.stay*self.onc, last_off*self.switch*self.onc)
                this_off = max(last_on*self.switch*self.offc, last_off*self.stay*self.offc)
                self.probabilities.append((this_on, this_off))
        
        for p in self.probabilities:
            if p[0] > p[1]:
                self.temperature.append('On')
            else:
                self.temperature.append('Off')
    
    def output(self):
        print(self.probabilities)
            


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
        T2 = Task2()
        T2.initialise()
        T2.calculate()
        T2.output()
    else:
        print("Input not valid, try again")
        main()

if __name__ == "__main__":
    main()
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
    
def AgivenBandC(a,b,c, colno = 1):
    return ((a*b*c)+1)/((b*c)+colno)

def bayes():
    # Setup
    file = ['2']
    with open("lucas0_train.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',') 
        line_count = 0      
        for i in csv_reader:
            line_count += 1
            for c in i:
                if(c == '0' or c == '1'):
                    if(file[0] == '2'):
                        file[0] = c
                    else:
                        file.append(c)
        print(f'Processed {line_count} lines.')
    

    for i in range(0,len(file)):
        file[i] = int(file[i])

    row = [0]*12
    length = int(len(file)/12)
    table = [row]*length
    count = 0
    count2 = 1
    for f in range(0,len(file)):
        row[count] = file[f]
        if (f+1)%12 == 0:
            table[count2-1] = row.copy()
            count = 0
            count2 +=1
        else:
            count+=1

    #bayes network
    #smoking
    atemp = []
    btemp = []
    ctemp = []
    for x in range(0,1999):
        atemp.append(table[x][0])
        btemp.append(table[x][2])
        ctemp.append(table[x][3])
    a = sum(atemp)/len(atemp)
    b = sum(btemp)/len(atemp)
    c = sum(ctemp)/len(atemp)
    Smoking = AgivenBandC(a, b, c)
    print("Smoking: "+str(Smoking))

    #lung cancer
    atemp.clear()
    btemp.clear()
    ctemp.clear()
    for x in range(0,1999):
        atemp.append(table[x][11])
        ctemp.append(table[x][5])
    a = sum(atemp)/len(atemp)
    c = sum(ctemp)/len(atemp)
    LC = AgivenBandC(a, Smoking, c)
    print("Lung Cancer: "+str(LC))

    #Coughing
    atemp.clear()
    btemp.clear()
    ctemp.clear()
    for x in range(0,1999):
        atemp.append(table[x][10])
        btemp.append(table[x][9])
    a = sum(atemp)/len(atemp)
    b = sum(btemp)/len(atemp)
    Coughing = AgivenBandC(a, b, LC)
    print("Coughing: "+str(Coughing))

    #Fatigue
    atemp.clear()
    btemp.clear()
    ctemp.clear()
    for x in range(0,1999):
        atemp.append(table[x][8])
    a = sum(atemp)/len(atemp)

    Fatigue = AgivenBandC(a, Coughing, LC)
    print("Fatigue: "+str(Fatigue))
    LC2 = AgivenBandC(LC, Coughing, Fatigue,3)
    print("LC given Coughing and Fatigue: " + str(LC2))
    print("Smoking given Coughing and Fatigue: " + str((Smoking*LC2)/LC2))
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
        ##self.on = [0.4,0.4,0.2]
        ##self.off = [0.1,0.45,0.45]
        self.on = {"Hot": 0.4, "Warm": 0.4, "Cold": 0.2, "Stay": 0.7, "Switch": 0.3}
        self.off = {"Hot": 0.1, "Warm": 0.45, "Cold": 0.45, "Stay": 0.7, "Switch": 0.3}
        # Emission Probabilities
        # [on,off]
        self.em = [[0.4,0.1],[0.4,0.45],[0.2,0.45]]
        
        self.last_off = 0.0
        self.sequence = ["Cold","Warm","Hot","Warm","Cold"]
        self.memory = [[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]
        self.probabilities = [0.5,0.5]
        self.heat = [0.0,0.0]

    def calc(self):
        for s in self.sequence:
            #s = self.sequence[i]
            self.heat[0] = self.off[s] * ((self.off["Stay"]*self.probabilities[0])+(self.off["Switch"]*self.probabilities[1]))
            #temp1 = self.on[s]
            #temp2 = self.on["Switch"]
            #temp3 = self.probabilities[0]
            #temp4 = self.on["Stay"]
            #temp5 = self.probabilities[1]
            self.heat[1] = self.on[s] * ((self.on["Switch"]*self.probabilities[0])+(self.on["Stay"]*self.probabilities[1]))
            #self.heat[1] = temp1 * ((temp2*temp3)+(temp4*temp5))
            print(self.heat)
            self.probabilities = self.heat.copy()
            ##self.memory.append(self.probabilities.copy())
        #print(self.memory)
        print(self.probabilities[0] + self.probabilities[1])
            


    #def initialise(self):
        #self.probabilities.append((self.on*self.em[self.sequence[0]][0],self.off*self.em[self.sequence[0]][1]))

    def calculate(self):
        for i in range(1,len(self.sequence)-1):
            last_on, last_off = self.probabilities[i-1]

            this_on = self.stay*self.em[self.sequence[i]][1] + self.switch*self.em[self.sequence[i]][0]
            this_off = self.switch*self.em[self.sequence[i]][0] + self.stay*self.em[self.sequence[i]][1]

            this_off = last_off * this_off
            this_on = last_on * this_on



            self.probabilities.append((this_on, this_off))

            '''if self.sequence[i] == 'H':
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
                self.probabilities.append((this_on, this_off))'''
    
    def output(self):
        print(self.memory)
        print(self.probabilities[0] + self.probabilities[1])
            
#main
def main():
    print("Which task do you want to run?")
    i = input()
    if i == "1a":
        diseaseProbability()
    elif i == "1b":
        print("Filename: ")
        bayes()
    elif i == "2":
        T2 = Task2()
        T2.calc()
    else:
        print("Input not valid, try again")
        main()

if __name__ == "__main__":
    main()
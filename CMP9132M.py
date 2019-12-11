import csv
#1a
def probOfOne(value):
    disease = 1.0/float(value)
    #print("The probability of having the disease is " + str(disease))
    return disease

def probAnB(a, b):
    return a*b

def probAgivenB(a, b):
    return probAnB(a, b) / b

def notAB(a, b):
    na = 1 - a
    nb = 1 - b
    return probAgivenB(na, nb)

def diseaseProbability():
    print("Please input the probability of the disease being true")
    d = input()
    print("P(t|d) = " + str(probAgivenB(0.99, probOfOne(d))))
    print("P(¬t|¬d) = " + str(notAB(0.99, probOfOne(d))))


#1b
class Node():
    def __init__(self, n, p, pa, ch):
        self.name = n
        self.prob = p
        self.parents = pa
        self.children = ch
    


def bayes(filename):
    with open(filename, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',') 
        line_count = 0      
        for row in csv_reader:
            line_count += 1
        print(f'Processed {line_count} lines.')
    

    #use len() to work out the titles from the values.

    group = [0,0]
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
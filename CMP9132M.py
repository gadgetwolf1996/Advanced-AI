def probOfOne(value):
    disease = 1.0/float(value)
    print("The probability of having the disease is " + str(disease))
    return disease

def probAnB(a, b):
    return a*b

def probAgivenB(a, b):
    return probAnB(a, b) / b

def diseaseProbability():
    print("Please input the probability of the disease being true")
    d = input()
    print("P(t|d) = " + str(probAgivenB(0.99, probOfOne(d))))

def main():
    print("Which task do you want to run?")
    i = input()
    if i == "1a":
        diseaseProbability()
    elif i == "1b":
        pass
    elif i == "2":
        pass
    else:
        print("Input not valid, try again")
        main()

if __name__ == "__main__":
    main()
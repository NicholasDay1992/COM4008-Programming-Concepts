import sys, random

def main(argv):
    #print("Arguments:", argv)
    #if len(argv) > 1:
    #    print("First argument:", argv[1])
    i = 1
    numbers = []
    for x in range(1, len(argv)):
        #print(argv[i])
        numbers.append(argv[i])
        i+=1 
    random.shuffle(numbers)
    print(numbers)

if __name__ == "__main__":
    main(sys.argv)
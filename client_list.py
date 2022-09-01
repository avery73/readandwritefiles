def main():

    infile = open("clients.txt", "r") 

    i = 1

    for line in infile:
        print(str(i) + ".", line.rstrip('\n'))
        i = i + 1

main()
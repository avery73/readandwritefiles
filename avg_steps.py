import csv

def main():

    infile = open("steps.csv", "r")

    csvfile = csv.reader(infile,delimiter=',') # tells python how to separate columns (,)

    next(csvfile)   # this gets rid of the header, skips first line

    #for record in csvfile:
     #   print(record[0])

    #while line in csvfile < 13:

    total = 0
    count = 0

    for record in csvfile:
        if int(record[0]) == 1:
            print("yay")
            
    
    average = total / count
    print(average)


    infile.close()

main()

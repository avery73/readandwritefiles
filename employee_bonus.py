import csv

def main():

    infile = open("employeepay.csv", "r") 

    csvfile = csv.reader(infile,delimiter=',') # tells python how to separate columns (,)

    next(csvfile)   # this gets rid of the header, skips first line

    i = 1

    print()

    for record in csvfile:
        print("Employee ID:", record[0])
        print("Name:", record[1], record[2])
        print("Salary:", record[3])
        print("Bonus:", record[4])
        i = i + 1
        input()

    infile.close()

main()
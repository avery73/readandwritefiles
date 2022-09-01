import csv

def main():

    infile = open("customers.csv", "r")

    csvfile = csv.reader(infile,delimiter=',') # tells python how to separate columns (,)

    next(csvfile)   # this gets rid of the header, skips first line

    print("Press ENTER to move to the next entry")
    print()

    for record in csvfile:  # record is a list
        print("First Name:", record[1])
        print("Last Name:", record[2])
        print("Country:", record[4])
        print()
        input()

    infile.close()

main()
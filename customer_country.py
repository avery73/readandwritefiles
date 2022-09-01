import csv

def main():

    infile = open("customers.csv", "r")

    csvfile = csv.reader(infile,delimiter=',') # tells python how to separate columns (,)

    next(csvfile)   # this gets rid of the header, skips first line

    outfile = open("customer_country.csv", "w")

    outfile.write("Full Name, Country" + "\n" + "\n")

    for record in csvfile:
        outfile.write(record[1] + " " + record[2] + ", " + record[4] + "\n")
    
    infile.close()
    outfile.close()


main()
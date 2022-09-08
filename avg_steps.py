import csv

def main():

    jan = january()
    feb = febuary()
    mar = march()
    apr = april()
    may2 = may()
    june2 = june()
    july2 = july()
    aug = august()
    sep = september()
    octo = october()
    nov = november()
    dec = december()

    outfile = open("avg_steps.csv", "w")

    outfile.write(f'January Average: {jan}')
    #outfile.write(jan)
    outfile.write('\n')

    outfile.write(f'Febuary Average: {feb}')
    #outfile.write(feb)
    outfile.write('\n')

    outfile.write(f'March Average: {mar}')
    #outfile.write(mar)
    outfile.write('\n')

    outfile.write(f'April Average: {apr}')
    #outfile.write(apr)
    outfile.write('\n')

    outfile.write(f'May Average: {may2}')
    #outfile.write(may2)
    outfile.write('\n')

    outfile.write(f'June Average: {june2}') 
    #outfile.write(june2)
    outfile.write('\n')

    outfile.write(f'July Average: {july2}')
    #outfile.write(july2)
    outfile.write('\n')

    outfile.write(f'August Average: {aug}')
    #outfile.write(aug)
    outfile.write('\n')

    outfile.write(f'September Average: {sep}')
    #outfile.write(sep)
    outfile.write('\n')

    outfile.write(f'October Average: {octo}')
    #outfile.write(octo)
    outfile.write('\n')

    outfile.write(f'November Average: {nov}')
    #outfile.write(nov)
    outfile.write('\n')

    outfile.write(f'December Average: {dec}')
    #outfile.write(dec)
    outfile.write('\n')

    outfile.close()


def january():
    infile = open("steps.csv", "r")
    csvfile = csv.reader(infile,delimiter=',') # tells python how to separate columns (,)
    next(csvfile)   # this gets rid of the header, skips first line
    outfile = open("avg_steps.csv", "w")

    total = []
    count = 0

    for record in csvfile:
           if record[0] == "1":
            total.append(record[1])
            count = count + 1

    total = [float(x) for x in total]
    total = sum(total)
    #print("Total:", total)

    #print("Count:", count)

    jan = total / count
    jan = str(jan)
    return jan
    #outfile.write(f'January Average: {average}\n') # keep n???
    infile.close()

def febuary():
    infile = open("steps.csv", "r")
    csvfile = csv.reader(infile,delimiter=',') # tells python how to separate columns (,)
    next(csvfile)   # this gets rid of the header, skips first line
    outfile = open("avg_steps.csv", "w")

    total = []
    count = 0

    for record in csvfile:
           if record[0] == "2":
            total.append(record[1])
            count = count + 1

    total = [float(x) for x in total]
    total = sum(total)
    #print("Total:", total)

    #print("Count:", count)

    jan = total / count
    jan = str(jan)
    return jan
    #outfile.write(f'January Average: {average}\n') # keep n???
    infile.close()

def march():
    infile = open("steps.csv", "r")
    csvfile = csv.reader(infile,delimiter=',') # tells python how to separate columns (,)
    next(csvfile)   # this gets rid of the header, skips first line
    outfile = open("avg_steps.csv", "w")

    total = []
    count = 0

    for record in csvfile:
           if record[0] == "3":
            total.append(record[1])
            count = count + 1

    total = [float(x) for x in total]
    total = sum(total)
    #print("Total:", total)

    #print("Count:", count)

    jan = total / count
    jan = str(jan)
    return jan
    #outfile.write(f'January Average: {average}\n') # keep n???
    infile.close()

def april():
    infile = open("steps.csv", "r")
    csvfile = csv.reader(infile,delimiter=',') # tells python how to separate columns (,)
    next(csvfile)   # this gets rid of the header, skips first line
    outfile = open("avg_steps.csv", "w")

    total = []
    count = 0

    for record in csvfile:
           if record[0] == "4":
            total.append(record[1])
            count = count + 1

    total = [float(x) for x in total]
    total = sum(total)
    #print("Total:", total)

    #print("Count:", count)

    jan = total / count
    jan = str(jan)
    return jan
    #outfile.write(f'January Average: {average}\n') # keep n???
    infile.close()

def may():
    infile = open("steps.csv", "r")
    csvfile = csv.reader(infile,delimiter=',') # tells python how to separate columns (,)
    next(csvfile)   # this gets rid of the header, skips first line
    outfile = open("avg_steps.csv", "w")

    total = []
    count = 0

    for record in csvfile:
           if record[0] == "5":
            total.append(record[1])
            count = count + 1

    total = [float(x) for x in total]
    total = sum(total)
    #print("Total:", total)

    #print("Count:", count)

    jan = total / count
    jan = str(jan)
    return jan
    #outfile.write(f'January Average: {average}\n') # keep n???
    infile.close()

def june():
    infile = open("steps.csv", "r")
    csvfile = csv.reader(infile,delimiter=',') # tells python how to separate columns (,)
    next(csvfile)   # this gets rid of the header, skips first line
    outfile = open("avg_steps.csv", "w")

    total = []
    count = 0

    for record in csvfile:
           if record[0] == "6":
            total.append(record[1])
            count = count + 1

    total = [float(x) for x in total]
    total = sum(total)
    #print("Total:", total)

    #print("Count:", count)

    jan = total / count
    jan = str(jan)
    return jan
    #outfile.write(f'January Average: {average}\n') # keep n???
    infile.close()

def july():
    infile = open("steps.csv", "r")
    csvfile = csv.reader(infile,delimiter=',') # tells python how to separate columns (,)
    next(csvfile)   # this gets rid of the header, skips first line
    outfile = open("avg_steps.csv", "w")

    total = []
    count = 0

    for record in csvfile:
           if record[0] == "7":
            total.append(record[1])
            count = count + 1

    total = [float(x) for x in total]
    total = sum(total)
    #print("Total:", total)

    #print("Count:", count)

    jan = total / count
    jan = str(jan)
    return jan
    #outfile.write(f'January Average: {average}\n') # keep n???
    infile.close()

def august():
    infile = open("steps.csv", "r")
    csvfile = csv.reader(infile,delimiter=',') # tells python how to separate columns (,)
    next(csvfile)   # this gets rid of the header, skips first line
    outfile = open("avg_steps.csv", "w")

    total = []
    count = 0

    for record in csvfile:
           if record[0] == "8":
            total.append(record[1])
            count = count + 1

    total = [float(x) for x in total]
    total = sum(total)
    #print("Total:", total)

    #print("Count:", count)

    jan = total / count
    jan = str(jan)
    return jan
    #outfile.write(f'January Average: {average}\n') # keep n???
    infile.close()

def september():
    infile = open("steps.csv", "r")
    csvfile = csv.reader(infile,delimiter=',') # tells python how to separate columns (,)
    next(csvfile)   # this gets rid of the header, skips first line
    outfile = open("avg_steps.csv", "w")

    total = []
    count = 0

    for record in csvfile:
           if record[0] == "9":
            total.append(record[1])
            count = count + 1

    total = [float(x) for x in total]
    total = sum(total)
    #print("Total:", total)

    #print("Count:", count)

    jan = total / count
    jan = str(jan)
    return jan
    #outfile.write(f'January Average: {average}\n') # keep n???
    infile.close()

def october():
    infile = open("steps.csv", "r")
    csvfile = csv.reader(infile,delimiter=',') # tells python how to separate columns (,)
    next(csvfile)   # this gets rid of the header, skips first line
    outfile = open("avg_steps.csv", "w")

    total = []
    count = 0

    for record in csvfile:
           if record[0] == "10":
            total.append(record[1])
            count = count + 1

    total = [float(x) for x in total]
    total = sum(total)
    #print("Total:", total)

    #print("Count:", count)

    jan = total / count
    jan = str(jan)
    return jan
    #outfile.write(f'January Average: {average}\n') # keep n???
    infile.close()

def november():
    infile = open("steps.csv", "r")
    csvfile = csv.reader(infile,delimiter=',') # tells python how to separate columns (,)
    next(csvfile)   # this gets rid of the header, skips first line
    outfile = open("avg_steps.csv", "w")

    total = []
    count = 0

    for record in csvfile:
           if record[0] == "11":
            total.append(record[1])
            count = count + 1

    total = [float(x) for x in total]
    total = sum(total)
    #print("Total:", total)

    #print("Count:", count)

    jan = total / count
    jan = str(jan)
    return jan
    #outfile.write(f'January Average: {average}\n') # keep n???
    infile.close()

def december():
    infile = open("steps.csv", "r")
    csvfile = csv.reader(infile,delimiter=',') # tells python how to separate columns (,)
    next(csvfile)   # this gets rid of the header, skips first line
    outfile = open("avg_steps.csv", "w")

    total = []
    count = 0

    for record in csvfile:
           if record[0] == "12":
            total.append(record[1])
            count = count + 1

    total = [float(x) for x in total]
    total = sum(total)
    #print("Total:", total)

    #print("Count:", count)

    jan = total / count
    jan = str(jan)
    return jan
    #outfile.write(f'January Average: {average}\n') # keep n???
    infile.close()

main()
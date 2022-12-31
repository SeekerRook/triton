#! /usr/bin/python3
def show(): 
    import matplotlib.pyplot as plt
    import os
    import csv
    infile = os.path.expanduser("~/Triton/log.csv")
    values = {}
    with open(infile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if(row[1] != ''): 
                values[row[0]] = float(row[1])
        csv_file.close()

    # print (values)
    timeline = sorted(values.items(),reverse = False)
    # print(timeline)


    x,y = zip(*timeline)
    # print(x)
    # print(y)
    plt.plot(x,y)

    plt.show()

if __name__ == "__main__":
    show()
import os, csv

filename = os.path.join(os.getcwd(),"grid.csv")
def sum_grid():
    _sum = 0
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            for i in row:
                _sum += int(i)
    return _sum

def transpose():
    matrix = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            row.reverse()
            matrix.append(row)
            matrix.reverse()
    with open("flipgrid.csv", 'w') as f:
        writer = csv.writer(f)
        for row in matrix:
            writer.writerow(row)

transpose()

# print(list(map(reverse(),zip(*matrix))))
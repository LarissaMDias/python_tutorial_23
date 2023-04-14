from mysci.readdata import read_data
from mysci.printing import print_comparison
from mysci.computation import compute_heatindex

#Column names and column indices
columns = {'date': 0, 'time': 1, 'tempout': 2, 'humout': 5, 'heatindex': 13}

#Data types for each column (if non-string)
types = {'tempout': float, 'humout': float, 'heatindex': float}

# Initialize my data variable
data = {}
for column in columns:
    data[column] = []

# Read the data file
filename = "data/wxobs20170821.txt"

with open(filename, 'r') as datafile:
    for _ in range(3):
        datafile.readline()

    for line in datafile:
        datum = line.split()
        for column in columns:
            i = columns[column]
            t = types.get(column, str)
            value = t(datum[i])
            data[column].append(value)

def estimate_windchill(t, v):
    wci = t - 0.7 * v
    return wci

#Commpute heat index
heatindex = [compute_heatindex(t, h) for t, h in zip(data['tempout'], data['humout'])]

# Output comparison of data
print_comparison('HEAT IDX', data['date'], data['time'], data['heatindex'], heatindex)

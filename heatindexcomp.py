from readdata import read_data
from printing import print_comparison

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
def compute_heatindex(t, hum):
    a = -42.379
    b = 2.04901523
    c = 10.14333127
    d = -0.22475541
    e = -0.00683783
    f = -0.05481717
    g = 0.00122874
    h = 0.00085282
    i = -0.00000199

    rh = hum/100

    hi = (a + (b * t) + (c * rh) + (d * t * rh) + \
          (e * t**2) + (f * rh**2) + (g * t**2 * rh) + \
          (h * t * rh**2) + (i * t**2 * rh**2))

    return hi

heatindex = []
for temp, hum in zip(data['tempout'], data['humout']):
    heatindex.append(compute_heatindex(temp, hum))

# Output comparison of data
print_comparison('HEAT IDX', data['date'], data['time'], data['heatindex'], heatindex)

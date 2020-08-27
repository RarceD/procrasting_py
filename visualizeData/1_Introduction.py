import pandas as pd  # module for
from matplotlib import pyplot as plt
plt.style.use('seaborn-dark')

x = [1961, 1993, 2015]
y = [133, 653, 343]
z = [133, 453, 743]

plt.plot(x, y, color='#444444', linestyle='--', marker='.', label='nop')
# plt.plot(x,z)

plt.title("insane graphics:")
plt.xlabel('adios')
plt.ylabel('hola')


sample_data = pd.read_csv('sample_data.csv')
# get one colom: sample_data.column_c
# get one value: sample_data.column_c.iloc[0]
# plt.plot(sample_data.column_a,sample_data.column_b, 'o')
# plt.plot(sample_data.column_a,sample_data.column_c)

data = pd.read_csv('countries.csv')
# First isolate the data, in this case US and China:


def plot_population(city):
    # I filter comparing with the column i want
    country = data[data.country == city]
    x = country.year
    y = country.population/10**6
    plt.plot(x, y, label=city)


plot_population('China')
plot_population('United States')
plot_population('Spain')
plt.legend()
plt.grid(True)  # show the grid

plt.savefig('plot.png')
plt.show()

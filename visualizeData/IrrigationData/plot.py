import matplotlib.pyplot as plt
from datetime import datetime
import json

x = []
y_temperature = []
y_wind_speed = []
y_solar_irradiance = []

json_file_path = "data2.json"
data = {};
with open(json_file_path, "r") as json_file:
    data = json.load(json_file)

for d in data:
    ts = int(d)
    posix_time = datetime.utcfromtimestamp(ts).strftime('%m/%d %H')
    temperature = data[d]['T']
    wind_speed = data[d]['FF']
    solar_irradiation = data[d]['SSI']

    x.append(posix_time)
    y_temperature.append(temperature)
    y_wind_speed.append(wind_speed)
    y_solar_irradiance.append(int(solar_irradiation)/15)


font_properties = {
    'family': 'serif',  
    'size': 12,         
    'weight': 'normal', 
    'style': 'italic'  
}


plt.plot(x, y_temperature, label='Temperature')
plt.plot(x, y_wind_speed, label='Wind Speed')
plt.plot(x, y_solar_irradiance, label='Solar Irradiance')

plt.xlabel('Time', fontdict=font_properties)
plt.ylabel('Y-axis Label')
plt.title('Weenat Sensor Data')
plt.xticks(x, x, rotation=90)
# plt.legend()
plt.legend()


plt.show()

"""
"""
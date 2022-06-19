import psutil

def get_temperature():
    temp_raw_data = psutil.sensors_temperatures(fahrenheit=False)["cpu_thermal"]
    
    return temp_raw_data[0][1]


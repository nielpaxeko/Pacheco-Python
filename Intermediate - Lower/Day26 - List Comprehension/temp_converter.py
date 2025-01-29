weather_c = {
    "Monday": 12, 
    "Tuesday": 14, 
    "Wednesday": 15, 
    "Thursday": 14, 
    "Friday": 21, 
    "Saturday": 22, 
    "Sunday": 24
}


def convert(celcius):
  return (celcius * (9/5)) + 32 

weather_f = {day:convert(temp) for (day, temp) in weather_c.items()}

print(weather_f)
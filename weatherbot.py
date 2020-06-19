#import pyowm
#owm = pyowm.OWM('8da2b3ede21aa15168a6c2c916548272')

#place = input("Место: ")
#observation = owm.weather_at_place(place)
#w = observation.weather
#print(w)          



from pyowm import OWM

owm = OWM('8da2b3ede21aa15168a6c2c916548272')  # You MUST provide a valid API key

# Search for current weather in Krasnodar
mgr = owm.weather_manager()
place = input("Введите город: ")
observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')['temp']

print("В " +place + "е сейчас: "+ str(temp))
#print(w)                  # <Weather - reference time=2013-12-18 09:20, status=Clouds>
#print(temp) 
# Weather details
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

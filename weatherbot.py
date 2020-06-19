from pyowm import OWM
owm = OWM('8da2b3ede21aa15168a6c2c916548272')  # API key
# Language settings 
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
# Search for current weather in place
mgr = owm.weather_manager()
place = input("Введите город: ")
observation = mgr.weather_at_place(place)

w = observation.weather
temp = w.temperature('celsius')['temp']
status = w.detailed_status

def endings(x):

    if x == 11:
        return " градусов"
    elif x%10 == 1:
        return " градус"
    elif x in (12,13,14):
        return " градусов" 
    elif x%10 in (2,3,4):
        return " градуса"
    elif x%10 in (5,6,7,8,9,0):
        return " градусов"
    
if temp > 0:
    print("В " +place + "е сейчас: +"+ str(round(temp)) + endings(temp) + " и " +status)
else:
    print("В " +place + "е сейчас: "+ str(round(temp)) + endings(temp) + " и " +status)


#print(w)                  # <Weather - reference time=2013-12-18 09:20, status=Clouds>
#print(temp) 
# Weather details
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}


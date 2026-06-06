city =input("Enter your city name: ")
temp =float(input("Enter today's temperature in c: "))
if temp > 15:
    print("warning, it is very hot today!")
if temp >25:
    print("Great day to go outside today!")
else:
    print("It is cold outside today, grab a jacket!")
if temp > 25:
    print("Weather: it is scorching hot")
elif temp > 25:
    print("temp: warm and sunny")
elif temp >15: 
    print("temp: cool and breezy")
else:
    print("weather: freezing cold-stay warm!")
import datetime
import calendar
now = datetime.datetime.now()
print("City:", city )
print("Time now:",now)
print(calendar.calendar(now.year))
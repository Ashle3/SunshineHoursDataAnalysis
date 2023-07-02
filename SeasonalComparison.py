#This file answers the question: 'Which city has the highest number and which has the lowest
#number of daylight hours depending on the season

import pandas as pd

#read the file into a variable
daylight = pd.read_csv("Sunshine hours for cities in the world.csv")

#add the country name column into a list
country = daylight["Country"]

country_list = []

for x in country:
    country_list.append(x)

#add the city name column into a list
city = daylight["City"]

city_list = []

for x in city:
    city_list.append(x)


#Spring Daylight Analysis
#We will be referencing March since it contains the Spring Equinox

#access the Mar column
spring = daylight["Mar"]

#define an empty list
spring_hours = []

#add each value in the March column to the list
for x in spring:
    spring_hours.append(x)

# print(spring_hours)

#find the highest value in the list
spring_high = max(spring_hours)
#get the row number that value was on, and convert it to a list
#(this is the only way it works)
sh_index = daylight[daylight["Mar"] == spring_high].index.tolist()
#retrieve the one list item, which is the row number the max value is on
#this turns the number into an int we can use
sh_index1 = sh_index[0]
#return the country name of the index we just extracted
sh_country = country_list[sh_index1]

#return the city name
sh_city = city_list[sh_index1]

print()
print("---SPRING---")
print(f"HIGH: {sh_city}, {sh_country} ({spring_high} hrs)")

#find the lowest value in the list
spring_low = min(spring_hours)
#find the index
sl_index = daylight[daylight["Mar"] == spring_low].index.tolist()
#retrieve the list item
sl_index1 = sl_index[0]
#return the country name
sl_country = country_list[sl_index1]
#return the city name
sl_city = city_list[sl_index1]

print(f"LOW: {sl_city}, {sl_country} ({spring_low} hrs)")
print()


#SUMMER

#access the Jun column
summer = daylight["Jun"]

#define an empty list
summer_hours = []

#add each value in the June column to the list
for x in summer:
    summer_hours.append(x)

#find the highest value in the list
summer_high = max(summer_hours)
#get the row number that value was on, and convert it to a list
#(this is the only way it works)
suh_index = daylight[daylight["Jun"] == summer_high].index.tolist()
#retrieve the one list item, which is the row number the max value is on
#this turns the number into an int we can use
suh_index1 = suh_index[0]
#return the country name of the index we just extracted
suh_country = country_list[suh_index1]

#return the city name
suh_city = city_list[suh_index1]

print()
print("---SUMMER---")
print(f"HIGH: {suh_city}, {suh_country} ({summer_high} hrs)")

#find the lowest value in the list
summer_low = min(summer_hours)
#find the index
sul_index = daylight[daylight["Jun"] == summer_low].index.tolist()
#retrieve the list item
sul_index1 = sul_index[0]
#return the country name
sul_country = country_list[sul_index1]
#return the city name
sul_city = city_list[sul_index1]

print(f"LOW: {sul_city}, {sul_country} ({summer_low} hrs)")
print()


#FALL

#access the Sep column
fall = daylight["Sep"]

#define an empty list
fall_hours = []

#add each value in the Sep column to the list
for x in fall:
    fall_hours.append(x)

#find the highest value in the list
fall_high = max(fall_hours)
#get the row number that value was on, and convert it to a list
#(this is the only way it works)
fh_index = daylight[daylight["Sep"] == fall_high].index.tolist()
#retrieve the one list item, which is the row number the max value is on
#this turns the number into an int we can use
fh_index1 = fh_index[0]
#return the country name of the index we just extracted
fh_country = country_list[fh_index1]

#return the city name
fh_city = city_list[fh_index1]

print()
print("---FALL---")
print(f"HIGH: {fh_city}, {fh_country} ({fall_high} hrs)")

#find the lowest value in the list
fall_low = min(fall_hours)
#find the index
fl_index = daylight[daylight["Sep"] == fall_low].index.tolist()
#retrieve the list item
fl_index1 = fl_index[0]
#return the country name
fl_country = country_list[fl_index1]
#return the city name
fl_city = city_list[fl_index1]

print(f"LOW: {fl_city}, {fl_country} ({fall_low} hrs)")
print()


#WINTER

#access the Dec column
winter = daylight["Dec"]

#define an empty list
winter_hours = []

#add each value in the Dec column to the list
for x in winter:
    winter_hours.append(x)

#find the highest value in the list
winter_high = max(winter_hours)
#get the row number that value was on, and convert it to a list
#(this is the only way it works)
wh_index = daylight[daylight["Dec"] == winter_high].index.tolist()
#retrieve the one list item, which is the row number the max value is on
#this turns the number into an int we can use
wh_index1 = wh_index[0]
#return the country name of the index we just extracted
wh_country = country_list[wh_index1]

#return the city name
wh_city = city_list[wh_index1]

print()
print("---WINTER---")
print(f"HIGH: {wh_city}, {wh_country} ({winter_high} hrs)")

#find the lowest value in the list
winter_low = min(winter_hours)
#find the index
wl_index = daylight[daylight["Dec"] == winter_low].index.tolist()
#retrieve the list item
wl_index1 = wl_index[0]
#return the country name
wl_country = country_list[wl_index1]
#return the city name
wl_city = city_list[wl_index1]

print(f"LOW: {wl_city}, {wl_country} ({winter_low} hrs)")
print()

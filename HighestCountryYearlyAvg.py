#This file answers these questions:
#Which country has the highest average number of daylight hours each year?
#Which country has the lowest?

import pandas as pd

#read the csv file into a variable
daylight = pd.read_csv("Sunshine hours for cities in the world.csv")

#print data based on a country
ivory_coast = daylight[daylight["Country"] == "Ivory Coast"]
yearly_avg = ivory_coast["Year"].mean()
#print(yearly_avg)

#This function takes lines 11-13 and turns them into a function that can be reused
def calculate_avg(country_name):
    country = daylight[daylight["Country"] == country_name]
    avg = round(country["Year"].mean())
    #print(f"The average number of daylight hours for {country_name} is {avg}")
    return avg

#define an empty dictionary
sun_dict = {}

#pass in each country in the data frame
sun_dict["Ivory Coast"] = calculate_avg("Ivory Coast")
sun_dict["Benin"] = calculate_avg("Benin")
sun_dict["Togo"] = calculate_avg("Togo")
sun_dict["Ghana"] = calculate_avg("Ghana")
sun_dict["Cameroon"]= calculate_avg("Cameroon")
sun_dict["Gabon"] = calculate_avg("Gabon")
sun_dict["Nigeria"] = calculate_avg("Nigeria")
sun_dict["Sudan"] = calculate_avg("Sudan")
sun_dict["Eritrea"] = calculate_avg("Eritrea")
sun_dict["Burkina Faso"] = calculate_avg("Burkina Faso")
sun_dict["Niger"] = calculate_avg("Niger")
sun_dict["Chad"] = calculate_avg("Chad")
sun_dict["Gambia"] = calculate_avg("Gambia")
sun_dict["Senegal"] = calculate_avg("Senegal")
sun_dict["Somalia"] = calculate_avg("Somalia")
sun_dict["Djibouti"] = calculate_avg("Djibouti")
sun_dict["Mali"] = calculate_avg("Mali")
sun_dict["Algeria"] = calculate_avg("Algeria")
sun_dict["Tunisia"] = calculate_avg("Tunisia")
sun_dict["Morocco"] = calculate_avg("Morocco")
sun_dict["Egypt"] = calculate_avg("Egypt")
sun_dict["Libya"] = calculate_avg("Libya")
sun_dict["Kenya"] = calculate_avg("Kenya")
sun_dict["Angola"] = calculate_avg("Angola")
sun_dict["South Sudan"] = calculate_avg("South Sudan")
sun_dict["Tanzania"] = calculate_avg("Tanzania")
sun_dict["Ethiopia"] = calculate_avg("Ethiopia")
sun_dict["Congo"] = calculate_avg("Congo")
sun_dict["Democratic Republic of the Congo"] = calculate_avg("Democratic Republic of the Congo")
sun_dict["Mauritania"] = calculate_avg("Mauritania")
sun_dict["South Africa"] = calculate_avg("South Africa")
sun_dict["Botswana"] = calculate_avg("Botswana")
sun_dict["Zambia"] = calculate_avg("Zambia")
sun_dict["Zimbabwe"] = calculate_avg("Zimbabwe")
sun_dict["Malawi"] = calculate_avg("Malawi")
sun_dict["Madagascar"] = calculate_avg("Madagascar")
sun_dict["Mozambique"] = calculate_avg("Mozambique")
sun_dict["Central African Republic"] = calculate_avg("Central African Republic")
sun_dict["Uganda"] = calculate_avg("Uganda")
sun_dict["Burundi"] = calculate_avg("Burundi")
sun_dict["Guinea"] = calculate_avg("Guinea")
sun_dict["Guinea-Bissau"] = calculate_avg("Guinea-Bissau")
sun_dict["Equatorial Guinea"] = calculate_avg("Equatorial Guinea")
sun_dict["Namibia"] = calculate_avg("Namibia")

sun_dict["Afghanistan"] = calculate_avg("Afghanistan")
sun_dict["Azerbaijan"] = calculate_avg("Azerbaijan")
sun_dict["Lebanon"] = calculate_avg("Lebanon")
sun_dict["Bangladesh"] = calculate_avg("Bangladesh")

sun_dict["China"] = calculate_avg("China")
sun_dict["India"] = calculate_avg("India")
sun_dict["Indonesia"] = calculate_avg("Indonesia")
sun_dict["Iran"] = calculate_avg("Iran")
sun_dict["Iraq"] = calculate_avg("Iraq")
sun_dict["Israel"] = calculate_avg("Israel")
sun_dict["Japan"] = calculate_avg("Japan")
sun_dict["Kazakhstan"] = calculate_avg("Kazakhstan")
sun_dict["Mongolia"] = calculate_avg("Mongolia")
sun_dict["North Korea"] = calculate_avg("North Korea")
sun_dict["Oman"] = calculate_avg("Oman")
sun_dict["Pakistan"] = calculate_avg("Pakistan")
sun_dict["Philippines"] = calculate_avg("Philippines")
sun_dict["Russia"] = calculate_avg("Russia")
sun_dict["Saudi Arabia"] = calculate_avg("Saudi Arabia")
sun_dict["Singapore"] = calculate_avg("Singapore")
sun_dict["South Korea"] = calculate_avg("South Korea")
sun_dict["Taiwan"] = calculate_avg("Taiwan")
sun_dict["Thailand"] = calculate_avg("Thailand")
sun_dict["Turkey"] = calculate_avg("Turkey")
sun_dict["United ArabEmirates"] = calculate_avg("United ArabEmirates")
sun_dict["Uzbekistan"] = calculate_avg("Uzbekistan")
sun_dict["Vietnam"] = calculate_avg("Vietnam")

sun_dict["Albania"] = calculate_avg("Albania")
sun_dict["Armenia"] = calculate_avg("Armenia")
sun_dict["Austria"] = calculate_avg("Austria")
sun_dict["Belarus"] = calculate_avg("Belarus")
sun_dict["Belgium"] = calculate_avg("Belgium")
sun_dict["Bosnia and Herzegovina"] = calculate_avg("Bosnia and Herzegovina")
sun_dict["Bulgaria"] = calculate_avg("Bulgaria")
sun_dict["Croatia"] = calculate_avg("Croatia")
sun_dict["Czech Republic"] = calculate_avg("Czech Republic")
sun_dict["Cyprus"] = calculate_avg("Cyprus")
sun_dict["Denmark"] = calculate_avg("Denmark")
sun_dict["Estonia"] = calculate_avg("Estonia")
sun_dict["Faroe Islands"] = calculate_avg("Faroe Islands")
sun_dict["Finland"] = calculate_avg("Finland")
sun_dict["France"] = calculate_avg("France")
sun_dict["Georgia"] = calculate_avg("Georgia")
sun_dict["Germany"] = calculate_avg("Germany")
sun_dict["Greece"] = calculate_avg("Greece")
sun_dict["Hungary"] = calculate_avg("Hungary")
sun_dict["Iceland"] = calculate_avg("Iceland")
sun_dict["Ireland"] = calculate_avg("Ireland")
sun_dict["Italy"] = calculate_avg("Italy")
sun_dict["Latvia"] = calculate_avg("Latvia")
sun_dict["Lithuania"] = calculate_avg("Lithuania")
sun_dict["Luxembourg"] = calculate_avg("Luxembourg")
sun_dict["Malta"] = calculate_avg("Malta")
sun_dict["Moldova"] = calculate_avg("Moldova")
sun_dict["Monaco"] = calculate_avg("Monaco")
sun_dict["Montenegro"] = calculate_avg("Montenegro")
sun_dict["Netherlands"] = calculate_avg("Netherlands")
sun_dict["North Macedonia"] = calculate_avg("North Macedonia")
sun_dict["Norway"] = calculate_avg("Norway")
sun_dict["Poland"] = calculate_avg("Poland")
sun_dict["Portugal"] = calculate_avg("Portugal")
sun_dict["Romania"] = calculate_avg("Romania")
sun_dict["Serbia"] = calculate_avg("Serbia")
sun_dict["Slovakia"] = calculate_avg("Slovakia")
sun_dict["Slovenia"] = calculate_avg("Slovenia")
sun_dict["Spain"] = calculate_avg("Spain")
sun_dict["Sweden"] = calculate_avg("Sweden")
sun_dict["Switzerland"] = calculate_avg("Switzerland")
sun_dict["Ukraine"] = calculate_avg("Ukraine")
sun_dict["United Kingdom"] = calculate_avg("United Kingdom")

sun_dict["Canada"] = calculate_avg("Canada")
sun_dict["Honduras"] = calculate_avg("Honduras")
sun_dict["Mexico"] = calculate_avg("Mexico")
sun_dict["Nicaragua"] = calculate_avg("Nicaragua")
sun_dict["Panama"] = calculate_avg("Panama")
sun_dict["Puerto Rico"] = calculate_avg("Puerto Rico")
sun_dict["El Salvador"] = calculate_avg("El Salvador")
sun_dict["Saint Pierreand Miquelon"] = calculate_avg("Saint Pierreand Miquelon")
sun_dict["United States"] = calculate_avg("United States")

sun_dict["Argentina"] = calculate_avg("Argentina")
sun_dict["Bolivia"] = calculate_avg("Bolivia")
sun_dict["Brazil"] = calculate_avg("Brazil")
sun_dict["Chile"] = calculate_avg("Chile")
sun_dict["Colombia"] = calculate_avg("Colombia")
sun_dict["Ecuador"] = calculate_avg("Ecuador")
sun_dict["Falkland Islands"] = calculate_avg("Falkland Islands")
sun_dict["French Guiana"] = calculate_avg("French Guiana")
sun_dict["Guyana"] = calculate_avg("Guyana")
sun_dict["Paraguay"] = calculate_avg("Paraguay")
sun_dict["Peru"] = calculate_avg("Peru")
sun_dict["Uruguay"] = calculate_avg("Uruguay")
sun_dict["Venezuela"] = calculate_avg("Venezuela")

sun_dict["Australia"] = calculate_avg("Australia")
sun_dict["Papua New Guinea"] = calculate_avg("Papua New Guinea")
sun_dict["Solomon Islands"] = calculate_avg("Solomon Islands")
sun_dict["New Zealand"] = calculate_avg("New Zealand")
sun_dict["Fiji"] = calculate_avg("Fiji")

#print(sun_dict)

#sorts the dictionary by value from greatest to least
sorted_greatest_to_least = sorted(sun_dict.items(), key = lambda x:x[1], reverse=True)

#print out the list to where each country gets its own line
for x in sorted_greatest_to_least:
    print(x)

#helps me find the highest value among the keys in the dictionary
y = sun_dict.values()

#returns the country name with the highest avg
country_name = [country for country, number in sun_dict.items() if number == max(y)]
#returns the country name with the lowest avg
country_name_small = [country for country, number in sun_dict.items() if number == min(y)]

#print out the results
print()
print(f"The country with the HIGHEST average number of daylight hours is \n{country_name} with {max(y)} hours.")
print()
print(f"The country with the LOWEST average number of daylight hours is \n{country_name_small} with {min(y)} hours.")
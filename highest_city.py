import pandas as pd

daylight = pd.read_csv("Sunshine hours for cities in the world.csv")

ivory_coast = daylight[daylight["Country"] == "Ivory Coast"]
print(ivory_coast)
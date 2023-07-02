# SunshineHoursDataAnalysis

# Overview

Data analysis is an area of computer science that interests me. This repository teaches me more about how to perform an analysis on pre-existing data, by letting me practice analyzing a simple data set. The knowledge that I gain from this practice will benefit my future software career, by letting me gain more valuable experience with data analysis.  

The data set I am analyzing, lists the number of sunlight hours certain cities across the globe receive each year. Each row in the data set lists the country name, the city name, how many sunlight hours the city receives each month, and the total number of hours that city receives each year (each of the months added up).

Here is the link to the data set I found on Kaggle.com:
https://www.kaggle.com/datasets/bilalwaseer/sunshine-hours-for-cities-around-the-world 

Besides practicing my data analysis skills, my main purpose for writing this software was to analyze how sunlight changes in global cities throughout the year. I was really interested in seeing how the amount of sunlight hours a city receives changes based off of its position on the Earth, and the season. 

Software Demo Video https://www.youtube.com/watch?v=EPCKv3D-Qw4

# Data Analysis Results

## Question #1
Which month of the year has the highest average of sunlight hours throughout the world?

Answer: July

[Solution](HighestMonthAvg.r)

## Question #2
Which COUNTRY has the highest average of sunlight hours each year? Which country has the lowest?

Highest: Namibia with 3738 hours

Lowest: Faroe Islands with 840 hours

[Solution](HighestCountryYearlyAvg.py)

## Question #3
Which CITIES had the most and least amount of sunlight hours during: 

The SPRING Equinox (March)
- Highest: Yuma, Arizona, United States (335.5 hrs)
- Lowest: Hanoi, Vietnam (47 hrs)

The SUMMER Solstice (June)
- Highest: Sacramento, California, United States (419.5 hrs)
- Lowest: Valdivia, Chile (45 hrs)

The FALL Equinox (September)
- Highest: Sacramento, California, United States (347.8 hrs)
- Lowest: Lima, Peru (37.3 hrs)

The WINTER Solstice (December)
- Highest: Upington, South Africa (367 hrs)
- Lowest: Dikson, Russia (0 hrs)

[Solution](SeasonalComparison.py)

# Development Environment

I used VSCode to write and edit my code. I used GitHub to upload my code to a public repository.

For one file, I used the R programming language, so that I could draw a bar graph. The rest of the repository is written in Python. I also used the pandas library from Python for most of my data analysis.

# Useful Websites

Kaggle https://www.kaggle.com/datasets/bilalwaseer/sunshine-hours-for-cities-around-the-world 

W3Schools https://www.w3schools.com/r/r_stat_data_set.asp 

Overview of Pandas https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html

Geeks For Geeks taught me how to install pandas
https://www.geeksforgeeks.org/how-to-install-python-pandas-on-windows-and-linux/ 

Tutorialspoint helped me know if pandas was installed correctly
https://www.tutorialspoint.com/how-do-i-know-if-python-has-pandas-installed 

This YouTube video taught me how to find the key based off of the value in a dictionary
https://www.youtube.com/watch?v=QLEmEl7H1Ks 

Free Code Camp taught me how to sort a dictionary by value
https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/

This Stackoverflow forum taught me how to convert an index into an integer
https://stackoverflow.com/questions/34421024/transforming-type-int64index-into-an-integer-index-in-python

# Future Work

* I could definitely create some more graphs, so we can see the information visually.
* I was planning on making a greatest average daylight hours dictionary specifically for the US.
* I could create a graph for each country, listing each cities' average daylight hours.
* I could also create a graph for each region/continent's average daylight hours


#This file calculates which month of the year has the highest average amount of daylight hours
#across all cities in the data frame
#The answer is July

#save the file to a variable
file <- "Sunshine hours for cities in the world.csv"
#read the file
info <- read.csv(file)

# city_names <- list(info[2])
# country_names <- list(info[1])

# col_names <- colnames(info)

# # overview <- summary(info)
# # print(overview)


#create function that calculates the average number of daylight hours of each month
#passes in the month column and the data frame
avg_per_month <- function(month, data) {
    month_avg <- mean(month)
    month_rounded <- as.integer(month_avg)
    return(month_rounded)
}

#create a vector containing the avg number of daylight hours per month
#to be used in bar graph
monthly_avg <- c(avg_per_month(info$Jan, info),
avg_per_month(info$Feb, info),
avg_per_month(info$Mar, info),
avg_per_month(info$Apr, info),
avg_per_month(info$May, info),
avg_per_month(info$Jun, info),
avg_per_month(info$Jul, info),
avg_per_month(info$Aug, info),
avg_per_month(info$Sep, info),
avg_per_month(info$Oct, info),
avg_per_month(info$Nov, info),
avg_per_month(info$Dec, info))

#create a vector containing the names of each month of the year
#to be used in bar graph
month_name <- c("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

#create bar graph
barplot(monthly_avg, names.arg = month_name, col = "gold")
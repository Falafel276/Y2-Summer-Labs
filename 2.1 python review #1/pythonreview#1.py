import random as rnd

temperatures = []

for i in range(7):
    temperatures.append(rnd.randint(26, 40))

days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

good_days_count = 0
num_of_even_days = 0

highest_temp = temperatures[0]
highest_temp_day = None

lowest_temp = temperatures[0]
lowest_temp_day = None

sum_of_week_temp = 0

above_avg = []

for i in range(7):
    sum_of_week_temp += temperatures[i]

    if temperatures[i] > highest_temp:
        highest_temp = temperatures[i]
        highest_temp_day = days_of_the_week[i]

    if temperatures[i] < lowest_temp:
        lowest_temp = temperatures[i]
        lowest_temp_day = days_of_the_week[i]

    if temperatures[i] % 2 == 0:
        num_of_even_days += 1

    print(days_of_the_week[i], temperatures[i])

avgWeekTemp = sum_of_week_temp / 7

for a in range(7):
    if temperatures[a] > avgWeekTemp:
        above_avg.append(days_of_the_week[a])

print("\nShelly has", num_of_even_days, "even days.\n The hottest temperature was", highest_temp, "on", highest_temp_day,"The lowest temperature was", lowest_temp, "on", lowest_temp_day,"\nThe average temprature was:",avgWeekTemp,"The days with above average tempratures were:",above_avg)
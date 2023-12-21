# with open("day24/weather_data.csv","r") as file:
#     data = file.readlines()
#     # print(data)

# import csv
# with open("day24/weather_data.csv","r") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         # print(row)
#         if row[1] != "temp":
#             temperatures.append(eval(row[1]))
#     # print(temperatures)

import pandas
data = pandas.read_csv("day24/weather_data.csv")
# # print(data)
# # print(data["temp"])
# data_dict = data.to_dict()
# # print(data_dict)
# temp_list = data["temp"].to_list()
# avg = data["temp"].mean()
# max = data["temp"].max()
# print(avg)
# print(max)
# print(data.condition)
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])
monday = data[data.day == "Monday"]
print(monday.temp)
temp_in_f = (monday.temp*1.8) + 32
print(temp_in_f)
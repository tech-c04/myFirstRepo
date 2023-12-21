import pandas
data = pandas.read_csv("day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231210.csv")
print(data["Primary Fur Color"].value_counts())
# fur_colour = data["Primary Fur Color"]
# fur_gray = data["Primary Fur Color"].count()
# print(fur_gray)

# count_gray = fur_gray.count()
# print(count_gray)
# # print(fur_colour)
# # count = fur_colour.count()
# # print(count)

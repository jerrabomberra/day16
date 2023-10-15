# hello this is the oop chapter 16 for 100 days of python
# pascal case - first letter work capitalised
# object = class()

# from turtle import Turtle, Screen

# timmy = Turtle()

# my_screen = Screen()

# # timmy.shape("turtle")
# # timmy.forward(200)
# # timmy.left(90)
# # timmy.forward(200)
# # timmy.left(90)
# # timmy.forward(200)
# # timmy.left(90)
# # timmy.forward(200)
# # timmy.left(90)

# # timmy.home()
# # for default shape 
  
# # for circle shape 
# timmy.color("red")
# timmy.shape("circle") 
# timmy.pensize(2)
# timmy.turtlesize(1)
# for i in range(6):
#     timmy.forward(100)
#     timmy.right(60) 
    
# my_screen.exitonclick()
# from prettytable import PrettyTable
# PrettyTable = PrettyTable()

# x.field_names = ["City name", "State","Area", "Population", "Annual Rainfall"]
# x.add_rows(
#     [
#         ["Adelaide", "SA",1295, 1158259, 600.5],
#         ["Brisbane", "Qld",5905, 1857594, 1146.4],
#         ["Canberra", "ACT", 697,425321,389.2],
#         ["Darwin", "NT",112, 120900, 1714.7],
#         ["Hobart", "Tas.",1357, 205556, 619.5],
#         ["Sydney", "NSW", 2058, 4336374, 1214.8],
#         ["Melbourne", "Vic.",1566, 4806092, 646.9],
#         ["Perth", "WA", 5386, 1554769, 869.4],
#     ]
# )
# x.align="r"
# # print(x.get_string(fields=["City name", "Population"]))

# # print(x.get_string(fields=["City name", "Population"],start=1, end=4))
# print(x.get_string(sortby="Population", reversesort=True))

from prettytable import PrettyTable
table = PrettyTable()
print(table)

table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
    ["Pikachu","Electric"],
    ["Squirtle","Water"],
    ["Charmander", "Fire"]
    ]
)
table.align="l"
print(table)

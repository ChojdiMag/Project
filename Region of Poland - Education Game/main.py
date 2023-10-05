import turtle
from typing import List

import pandas

screen = turtle.Screen()
screen.title("Region of Poland")
image = "map_of_poland_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("name_of_regions.csv")
all_regions = data.region.to_list()
guessed_region = []

while len(guessed_region) < 17:
    answer = screen.textinput(title=f"{len(guessed_region)}/17 Region of Poland", prompt="What's another region's "
                                                                                         "name").title()

    if answer == "Exit":
        missing_region = []
        for region in all_regions:
            if region not in guessed_region:
                missing_region.append(region)
        new_data = pandas.DataFrame(missing_region)
        new_data.to_csv("region_to_learn.csv")
        break
    if answer in all_regions:
        guessed_region.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        region_data = data[data.region == answer]
        t.goto(int(region_data.x), int(region_data.y))
        t.write(arg=answer, font=("Arial", 12, "normal"))

screen.exitonclick()

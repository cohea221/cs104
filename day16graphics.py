from graphics import *
win = GraphWin('Day 16 - Graphics', 500, 250)

radius = win.width / 10
print(radius)

point_blue = Point((win.width / 2) - (2 * radius), win.height / 2)
point_black = Point(win.width / 2, win.height / 2)
point_red = Point((win.width / 2) + (2 * radius), win.height / 2)
point_yellow = Point((win.width / 2) - radius, (win.height / 2) - radius)
point_green = Point((win.width / 2) + radius, (win.height / 2) - radius)

# blue
circle_blue = Circle(point_blue, radius)
circle_blue.setOutline('blue')
circle_blue.draw(win)

# black
circle_black = Circle(point_black, radius)
circle_black.draw(win)

# red
circle_red = Circle(point_red, radius)
circle_red.setOutline('red')
circle_red.draw(win)

# yellow
circle_yellow = Circle(point_yellow, radius)
circle_yellow.setOutline('yellow')
circle_yellow.draw(win)

# green
circle_green = Circle(point_green, radius)
circle_green.setOutline('green')
circle_green.draw(win)

#circles = [circle_blue, circle_black, circle_red, circle_yellow, circle_green]

#for circle in circles:
#    circle.draw(win)

while(True):
    win.getKey()
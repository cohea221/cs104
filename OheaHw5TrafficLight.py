# Chris O'Hea

from graphics import *

# Naming Conventions:
# r - Rect, c - Circle
# p1, p2

win = GraphWin('O\'Hea Traffic Light HW5', 400, 900)

# Set radius and 
radius = win.height / 8
win_center = Point(win.width / 2, win.height / 2)

# Create Rectangle Points
rp1 = Point(win_center.getX() - radius, win_center.getY() - (3 * radius))
rp2 = Point(win_center.getX() + radius, win_center.getY() + (3 * radius))

# Create and Draw Rectangle
rect = Rectangle(rp1, rp2)
rect.setFill('grey')
rect.draw(win)

# Create Circle Centers
cpr = Point(win_center.getX(), win_center.getY() - (2 * radius))
cpy = win_center
cpg = Point(win_center.getX(), win_center.getY() + (2 * radius))

# Create Circle Objects
circ_red = Circle(cpr, radius)
circ_yellow = Circle(cpy, radius)
circ_green = Circle(cpg, radius)

# Draw Circles
circ_red.draw(win).setFill('red')
circ_yellow.draw(win).setFill('yellow')
circ_green.draw(win).setFill('green')


# Keep Open
while(True):
    if(win.isOpen()):
        win.getKey()

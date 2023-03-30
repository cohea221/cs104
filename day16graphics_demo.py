from graphics import *

win = GraphWin('Chevrolet Logo - CS104', 800, 600)

sqpt1 = Point(250, 75)
sqpt2 = Point(550, 375)


square = Rectangle(sqpt1, sqpt2)
square.setFill('gold')
square.setOutline('gold')
square.draw(win)
sqcenter = square.getCenter()
sqcenter.draw(win)

# X-offset small = 120
# X-offset lg = 130
# Y-offset = 110

# Top Left
ppt1 = Point(sqcenter.x - (150 + 110), sqcenter.y - 100)
# Top Right
ppt2 = Point(sqcenter.x + (150 + 150), sqcenter.y - 100)
# Bottom Right
ppt3 = Point(sqcenter.x + (150 + 110), sqcenter.y + 100)
# Bottom Left
ppt4 = Point(sqcenter.x - (150 + 150), sqcenter.y + 100)

poly = Polygon(ppt1, ppt2, ppt3, ppt4)
poly.setFill('gold')
poly.setOutline('gold')
poly.draw(win)

text = Text(Point(400, sqcenter.y + 180), 'Chevrolet')
text.setStyle('bold')
text.setSize(30)
text.draw(win)
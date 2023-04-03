###################################################################################
#This section draws the window and all labels and entry boxes
#Modify lines 8, 11, 15, 21 to display appropriate wording

# Chris O'Hea

import graphics

# create the window - MODIFY THE TITLE DISPLAYED
win = graphics.GraphWin("Baseball Statistics", 600, 600)

# draw the heading at the top  - MODIFY THE TEXT DISPLAYED
top_text=graphics.Text(graphics.Point(300,100), "Win Percentage")
top_text.draw(win)

# draw the first number Entry box and text - MODIFY THE TEXT DISPLAYED
text1 = graphics.Text(graphics.Point(150,200), "Games Won:")
text1.draw(win)
input_entry1 = graphics.Entry(graphics.Point(350,200), 10)
input_entry1.draw(win)

# draw the second number Entry box and text - MODIFY THE TEXT DISPLAYED
text2 = graphics.Text(graphics.Point(150,300), "Games Lost:")
text2.draw(win)
input_entry2 = graphics.Entry(graphics.Point(350,300), 10)
input_entry2.draw(win)

# draw the answer text. Leave it blank to start
text3 = graphics.Text(graphics.Point(150,400), "Win %:")
text3.draw(win)
output_text = graphics.Text(graphics.Point(350,400),"")
output_text.draw(win)

# draw the instructions at the bottom
instruction_text = graphics.Text(graphics.Point(300,500),"Click anywhere to display answer")
instruction_text.draw(win)

###################################################################################
# Add code in the below section 

#################################
# wait for a mouse click
#################################

win.getMouse()

#################################
# get input from the entry boxes.  Be sure to convert it if needed
#################################

if input_entry1.getText() != '':
    wins = float(input_entry1.getText())
else:
     wins = 0
        
if input_entry2.getText() != '':
    losses = float(input_entry2.getText())
else:
     losses = 0


#################################
# do the processing
#################################
# Calculation is: Wins / Total
# Multiply by 100 to get decimal -> percent

percent = (wins / (wins + losses)) * 100

#################################
# display output 
#################################
# EC: Limit to 2 decimal places
output_text.setText(f'{percent:.2f}')

#################################
# update the instructions at the bottom to tell them to click to exit
#################################

instruction_text.setText('Click anywhere to close')

#################################
# wait for click and then close the window
#################################

win.getMouse()
win.close()

###################################################################################
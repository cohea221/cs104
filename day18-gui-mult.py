###################################################################################
#This section draws the window and all labels and entry boxes
#Modify lines 8, 11, 15, 21 to display appropriate wording

import graphics

# create the window - MODIFY THE TITLE DISPLAYED
win = graphics.GraphWin("Multiplication Tables", 600, 600)

# draw the heading at the top  - MODIFY THE TEXT DISPLAYED
top_text=graphics.Text(graphics.Point(300,100), "Multiplication")
top_text.draw(win)

# draw the first number Entry box and text - MODIFY THE TEXT DISPLAYED
text1 = graphics.Text(graphics.Point(150,200), "First Number:")
text1.draw(win)
input_entry1 = graphics.Entry(graphics.Point(350,200), 10)
input_entry1.draw(win)

# draw the second number Entry box and text - MODIFY THE TEXT DISPLAYED
text2 = graphics.Text(graphics.Point(150,300), "Second Number:")
text2.draw(win)
input_entry2 = graphics.Entry(graphics.Point(350,300), 10)
input_entry2.draw(win)

# draw the answer text. Leave it blank to start
text3 = graphics.Text(graphics.Point(150,400), "Answer:")
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

num1 = int(input_entry1.getText())
num2 = int(input_entry2.getText())

#################################
# do the processing
#################################

ans = num1 * num2

#################################
# display output 
#################################

output_text.setText(ans)

#################################
#update the instructions at the bottom to tell them to click to exit
#################################

instruction_text.setText('Click anywhere to close')

#################################
# wait for click and then close the window
#################################

win.getMouse()
win.close()

###################################################################################
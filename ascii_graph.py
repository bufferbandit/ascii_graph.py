# -*- coding: utf-8 -*-
# 
# author: bufferbandit
#

height  = 15
width   = 100


start_axis = 1

heights = [  
    1,2,3,4,5,6,7,6,5,4,3,2,1,0,0,0,0,
    1,2,3,4,5,6,7,6,5,4,3,2,1,0,0,0,0,
    1,2,3,4,5,6,7,6,5,4,3,2,1,0,0,0,0,
    1,2,3,4,5,6,7,6,5,4,3,2,1,0,0,0,0,
    1,2,3,4,5,6,7,6,5,4,3,2,1,0,0,0,0,
    1,2,3,4,5,6,7,6,5,4,3,2,1]



graph  = "▉"
x_axis = "─"
y_axis = "│"
corner_char = "└"
empty  =" "


lines1 = []
lines2 = []


for _height in range(height):
    
    line_buffer = "" 
    line_buffer += " "
    wbuff=""

    for width_index,_width in enumerate(range(width)):
        
        try:
            max_height = heights[_width]
        except IndexError:
            break
            
        if _height < max_height:
            line_buffer += graph
        else:
            line_buffer += empty

    lines1.append(line_buffer)

for line_nr,line in enumerate(lines1,start=start_axis):
    line_buffer = ""
    y_axis_nr_max_len = len(str(len(lines1)))
    y_axis_nr = len(str(line_nr)) 
    y_axis_buffer = ""
    y_axis_buffer += str(line_nr)
    y_axis_buffer += " " * (y_axis_nr_max_len - y_axis_nr)
    y_axis_buffer += " " + y_axis
    line_buffer += y_axis_buffer
    line_buffer += line
    lines2.append(line_buffer)

lines2 = lines2[::-1]

buffer2=""
y_axis_len = len(str(len(lines2)))
buffer2 += " " * ( y_axis_len + 1 )
buffer2 += corner_char
buffer2 += x_axis * (width + 5)
lines2.append(buffer2)


for lines in lines2:
    print(lines)


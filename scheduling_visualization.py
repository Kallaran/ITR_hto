import svgwrite


LIST_FUNC = { "navigation" , "Detection_contact" , "Detection_distance"}

dwg = svgwrite.Drawing('test.svg', profile='tiny')



x_start_rect = 0
y_start_rect = 0
rect_color = 'grey'
y_task_name = 50

for fun in LIST_FUNC:
	dwg.add(dwg.rect((x_start_rect,y_start_rect), (100, 100), fill=rect_color))

	y_start_rect=y_start_rect+100

	if rect_color == 'grey':
		rect_color = 'white'
	else : 
		rect_color = 'grey'

	dwg.add(dwg.text(fun,
    insert=(10,y_task_name),
    stroke='none',
    fill='#900',
    font_size='8px',
    font_weight="bold",
    font_family="Arial")
	)

	y_task_name = y_task_name + 100





#dwg.add(dwg.line((0, 0), (10, 0), stroke='black'))

#dwg.add(dwg.line((0, 50), (10, 50), stroke='black'))


dwg.save()
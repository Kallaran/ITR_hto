import svgwrite

from ppcm import ppcm



def display_tasks_names(dwg, LIST_FUNC):
	## display background color
	x_start_rect = 0
	y_start_rect = 0
	rect_color = 'grey'

	##display task name
	y_task_name = 50



	for fun in LIST_FUNC:
	    #display background color for task name and display task name 

	    ## display background color for task name
	    dwg.add(dwg.rect((x_start_rect,y_start_rect), (100, 100), fill=rect_color))

	    y_start_rect=y_start_rect+100

	    if rect_color == 'grey':
	        rect_color = 'white'
	    else : 
	        rect_color = 'grey'


	    ##display task name
	    dwg.add(dwg.text(fun,
	        insert=(10,y_task_name),
	        stroke='none',
	        fill='#900',
	        font_size='8px',
	        font_weight="bold",
	        font_family="Arial")
	    )

	    y_task_name = y_task_name + 100

def display_graduated_lines(dwg, LIST_FUNC, Pi):
	## display background color
	x_start_rect = 100


	##display line
	x_start_line = 100
	x_end_line = 120

	##display times
	x_times = 100
	hyper_periode = ppcm(*Pi) 

	for times in range(hyper_periode+1):

	    #rect
	    y_start_rect = 0
	    rect_color = 'grey'

	    #line
	    hauteur_line = 65

	    #time
	    y_times = 80



	    for fun in LIST_FUNC:
	        #
	        ## display background color for task name
	        dwg.add(dwg.rect((x_start_rect,y_start_rect), (20, 100), fill=rect_color))

	        y_start_rect=y_start_rect+100

	        if rect_color == 'grey':
	            rect_color = 'white'
	        else : 
	            rect_color = 'grey'

	        ##display line
	        dwg.add(dwg.line((x_start_line, hauteur_line), (x_end_line, hauteur_line), stroke='black'))
	        ##display small line
	        dwg.add(dwg.line((x_start_line, hauteur_line), (x_start_line, hauteur_line+5), stroke='black'))

	        hauteur_line = hauteur_line + 100



	        ##display times
	        dwg.add(dwg.text(times,
	                insert=(x_times,y_times),
	                stroke='none',
	                fill='black',
	                font_size='8px',
	                font_weight="bold",
	                font_family="Arial")
	        )

	        y_times = y_times + 100


	    #rect
	    x_start_rect = x_start_rect + 20

	    #line
	    x_start_line = x_start_line + 20
	    x_end_line = x_end_line + 20

	    #time
	    x_times = x_times + 20













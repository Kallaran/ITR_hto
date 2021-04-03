import svgwrite

from scheduling_visualization import display_tasks_names, display_graduated_lines, display_tasks_arrival, display_tasks_deadlines

LIST_FUNC = ["navigation" , "Detection_contact" , "Detection_distance"]
FirstArrival = [0, 0, 0]
Pi = [20, 5, 15]
Di = [12, 5, 7]




dwg = svgwrite.Drawing('test.svg', profile='tiny')

display_tasks_names(dwg, LIST_FUNC)
display_graduated_lines(dwg, LIST_FUNC, Pi)
display_tasks_arrival(dwg, LIST_FUNC, Pi, FirstArrival)
display_tasks_deadlines(dwg, LIST_FUNC, Pi, FirstArrival, Di)



dwg.save()
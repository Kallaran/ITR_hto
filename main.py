import svgwrite

from scheduling_visualization import display_tasks_names, display_graduated_lines

LIST_FUNC = { "navigation" , "Detection_contact" , "Detection_distance"}
Pi = [10, 5, 20]
FirstArrival = [0, 0, 0]



dwg = svgwrite.Drawing('test.svg', profile='tiny')

display_tasks_names(dwg, LIST_FUNC)
display_graduated_lines(dwg, LIST_FUNC, Pi)


dwg.save()
import svgwrite

from scheduling_visualization import display_tasks_names, display_graduated_lines, display_tasks_arrival, display_tasks_deadlines
from schedulers import rateMonotonic, earliestDeadlineFirst

LIST_FUNC = ["navigation" , "Detection_contact" , "Detection_distance"]
FirstArrival = [0, 0, 0]
Pi = [20, 5, 10]
Ci = [1, 2, 4]
Di = [8, 4, 10]




dwg = svgwrite.Drawing('test.svg', profile='tiny')

display_tasks_names(dwg, LIST_FUNC)
display_graduated_lines(dwg, LIST_FUNC, Pi)

#rateMonotonic(dwg, LIST_FUNC, Pi, FirstArrival, Ci, Di)
earliestDeadlineFirst(dwg, LIST_FUNC, Pi, FirstArrival, Ci, Di)

display_tasks_arrival(dwg, LIST_FUNC, Pi, FirstArrival)
display_tasks_deadlines(dwg, LIST_FUNC, Pi, FirstArrival, Di)


dwg.save()
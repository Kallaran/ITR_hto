import svgwrite

from scheduling_visualization import display_tasks_names, display_graduated_lines, display_tasks_arrival, display_tasks_deadlines
from schedulers import rateMonotonic, earliestDeadlineFirst

LIST_FUNC = ["navigation" , "Detection_contact" , "Detection_distance"]
FirstArrival = [0, 0, 0]

# Valeur Réél
Di = [20,10,30] 
Ci = [3,3,3]
Pi = [20,10,30]



# # Valeur du cours pour EDF
# Pi = [20, 5, 10]
# Ci = [1, 2, 4]
# Di = [8, 4, 10]

"""
# Valeur du cours pour RM
Pi = [20, 5, 10]
Ci = [3, 2, 2]
Di = [20, 5, 10]
"""




dwg = svgwrite.Drawing('edfTrue.svg', profile='tiny')

display_tasks_names(dwg, LIST_FUNC)
display_graduated_lines(dwg, LIST_FUNC, Pi)

rateMonotonic(dwg, LIST_FUNC, Pi, FirstArrival, Ci, Di)
#earliestDeadlineFirst(dwg, LIST_FUNC, Pi, FirstArrival, Ci, Di)

display_tasks_arrival(dwg, LIST_FUNC, Pi, FirstArrival)
display_tasks_deadlines(dwg, LIST_FUNC, Pi, FirstArrival, Di)


dwg.save()
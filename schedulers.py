

from ppcm import ppcm


def shorterPeriod(Pi):
    shorterPeriod = -1
    for p in Pi:
        if p != -1:
            shorterPeriod = p

    for p in Pi:
        if shorterPeriod > p and p != -1:
            shorterPeriod = p

    return shorterPeriod




#Tasks with shorter periods will have highter priorities
#In case of identical period, the deterministic tie-breaking rule is to give higher priority to the first elements of LIST_FUNC
def rateMonotonic(dwg, LIST_FUNC, Pi, FirstArrival, Ci, Di):

    hyper_periode = ppcm(*Pi)
    new_FirstArrival = FirstArrival[:]
    new_Ci = Ci[:]
    new_Pi = Pi[:]
    new_Di = Di[:]
    
    #to set each element of new_Ci to 0, we will fill it with each task arrival
    for count, e in enumerate(new_Ci):
        new_Ci[count] = 0



    x_start_rect = 100.5

    for times in range(hyper_periode):
        
        #boolean to know if we have already added a square (1) or not yet(0)
        square = 0

        #we iterate one time to update if needed
        for count, fun in enumerate(LIST_FUNC):
            
            #check if a deadline is outdated
            if new_Di[count] == times and new_Ci[count] != 0:
                    print( LIST_FUNC[count] , "misses its deadline at : ", times )
            
            #if this times there is a new task arrival then reset reset new_Pi[count], update new_Ci[count] and update new_FirstArrival[count]
            if new_FirstArrival[count] == times:
                new_Pi[count] = Pi[count]
                new_Ci[count] = new_Ci[count] + Ci[count] #nomber of late squares + addition of squares 
                new_Di[count] = new_FirstArrival[count] + Di[count]
                new_FirstArrival[count] = new_FirstArrival[count] + Pi[count]
                
                

        for count, fun in enumerate(LIST_FUNC):

            y_start_rect = 45

            if new_Pi[count] == shorterPeriod(new_Pi) and new_Ci[count] != 0 and square == 0:

                y_start_rect = y_start_rect + (count * 100) 
                dwg.add(dwg.rect((x_start_rect,y_start_rect), (19.5, 19.5), 2, 2, fill='yellow'))
                
                dwg.add(dwg.text(times,
                    insert=(x_start_rect + 5, y_start_rect + 10),
                    stroke='none',
                    fill='black',
                    font_size='8px',
                    font_weight="bold",
                    font_family="Arial")
                )


                new_Ci[count] = new_Ci[count] - 1 #a square has been placed, we reduce the number of squares that remain to be placed
                if new_Ci[count] == 0:        #if for a task all of its squares have been placed then it is prevented from being selected again 
                    new_Pi[count] = -1

                square = 1

            

        x_start_rect = x_start_rect + 20



def earlierAbsoluteDeadline(Di):
    earlierAbsoluteDeadline = -1

    for d in Di:
        if d != -1:
            earlierAbsoluteDeadline = d

    for d in Di:
        if earlierAbsoluteDeadline > d and d != -1:
            earlierAbsoluteDeadline = d

    return earlierAbsoluteDeadline




#Tasks with earlier absolute deadlines will be executed at higher
#priorities (deterministic tie-breaking rule in case of equality)
def earliestDeadlineFirst(dwg, LIST_FUNC, Pi, FirstArrival, Ci, Di):


    hyper_periode = ppcm(*Pi)
    new_FirstArrival = FirstArrival[:]
    new_Ci = Ci[:]
    new_Di = Di[:]
    
    #to set each element of new_Ci to 0, we will fill it with each task arrival
    for count, e in enumerate(new_Ci):
        new_Ci[count] = 0



    x_start_rect = 100.5

    for times in range(hyper_periode):
        
        #boolean to know if we have already added a square (1) or not yet(0)
        square = 0

        #we iterate one time to update if needed
        for count, fun in enumerate(LIST_FUNC):
            
            #check if a deadline is outdated
            if new_Di[count] == times and new_Ci[count] != 0:
                    print( LIST_FUNC[count] , "misses its deadline at : ", times )
            
            #if this times there is a new task arrival then reset reset new_Pi[count], update new_Ci[count] and update new_FirstArrival[count]
            if new_FirstArrival[count] == times:
                new_Ci[count] = new_Ci[count] + Ci[count] #nomber of late squares + addition of squares 
                new_Di[count] = new_FirstArrival[count] + Di[count]
                new_FirstArrival[count] = new_FirstArrival[count] + Pi[count]
                
                

        for count, fun in enumerate(LIST_FUNC):

            y_start_rect = 45


            if new_Di[count] == earlierAbsoluteDeadline(new_Di) and new_Ci[count] != 0 and square == 0:

                y_start_rect = y_start_rect + (count * 100) 
                dwg.add(dwg.rect((x_start_rect,y_start_rect), (19.5, 19.5), 2, 2, fill='yellow'))
                
                dwg.add(dwg.text(times,
                    insert=(x_start_rect + 5, y_start_rect + 10),
                    stroke='none',
                    fill='black',
                    font_size='8px',
                    font_weight="bold",
                    font_family="Arial")
                )


                new_Ci[count] = new_Ci[count] - 1     #a square has been placed, we reduce the number of squares that remain to be placed


                if new_Ci[count] == 0:        #if for a task all of its squares have been placed then it is prevented from being selected again 
                    new_Di[count] = -1


                square = 1

            

        x_start_rect = x_start_rect + 20






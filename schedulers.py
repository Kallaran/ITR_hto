

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





def rateMonotonic(dwg, LIST_FUNC, Pi, FirstArrival, Ci):

    hyper_periode = ppcm(*Pi)
    new_FirstArrival = FirstArrival[:]
    new_Ci = Ci[:]
    new_Pi = Pi[:]



    x_start_rect = 100.5

    for times in range(hyper_periode):

        square = 0


        for count, fun in enumerate(LIST_FUNC):

            if new_FirstArrival[count] == times:
                new_Pi[count] = Pi[count]
                new_Ci[count] = Ci[count]
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


                new_Ci[count] = new_Ci[count] - 1
                if new_Ci[count] == 0:
                    new_Pi[count] = -1

                square = 1

            

        x_start_rect = x_start_rect + 20







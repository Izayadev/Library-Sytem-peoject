# DATE File
from datetime import datetime

dmyDate = datetime.today().strftime('%d-%m-%Y')
dmDate = datetime.today().strftime('%d-%m')

def afterDays(plus):

    date = str(dmDate)
    print(date)
    day = ""
    month = ""


    # GET
    count = 0
    for d in date:
        if count != 2:
            day += d
            count +=1

    # GET month
    count = 0
    for m in date:
        if m=="-":
            count+=1
            continue

        if  count == 1 :
            month += m 

    # CONVERT
    day = int(day)

    # PROSSES
    day+=plus

    if day > 30 :
        day-=30


    # RETURN
    return str(day)+"-"+month
    
    
    


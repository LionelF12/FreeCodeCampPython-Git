def add_time(start,dur,day = True):
    #day dictionary
    numdaydict = {1:'monday',2:'tuesday',3:'wednesday',4:'thursday', 5:'friday', 6:'saturday',7:'sunday'}
    
    #retrieve day's number in the week
    def dateretriever(day):
        for k,v in numdaydict.items():
            if day.lower() == v:
                return k

    #breakdown start & dur
    starthour = int(start.split(':')[0])
    startmin = int(start.split(':')[1].split()[0])
    startampm = str(start.split(':')[1].split()[1])
    durhour = int(dur.split(':')[0])
    durmin = int(dur.split(':')[1])

    #add hours and minutes + change ampm if > 12 hour + count days
    finhour = starthour + durhour
    finmin = startmin + durmin
    finampm = startampm
    daycount = 0

    #converting extra minutes > 60 into hours
    while finmin > 60:
        finmin -= 60
        finhour +=1

    #converting extra hours > 12 into AMPM change, and any PM > AM change adds to a day count
    while finhour > 12:
        finhour -= 12
        if finampm == 'AM':
            finampm = 'PM'
        else: 
            finampm = 'AM'
            daycount += 1

    #catching the sneaky 11am/pm to 12am/pm changes
    if finhour == 12:
        if finampm == 'AM':
            finampm = 'PM'
        else: 
            finampm = 'AM'
            daycount += 1

    #ensuring minutes have 2 digits
    if len(str(finmin)) == 1:
        finmin = '0' + str(finmin)

    #next day / X days later
    if daycount == 1:
        datetrack = ' (next day)'
    elif daycount > 1:
        datetrack = ' (' + str(daycount) + ' days later' +')'
    else:
        datetrack = ''
    
    #optional day of the week
    if day != True:
        daycount += dateretriever(day)
        while daycount > 7:
            daycount -= 7
        findate = numdaydict[daycount]
        return (str(finhour) + ':' + str(finmin) + ' ' + finampm + ', ' + findate.capitalize() + datetrack)

    else: 
        return (str(finhour) + ':' + str(finmin) + ' ' + finampm + datetrack)

print(add_time("11:55 AM", "3:12"))
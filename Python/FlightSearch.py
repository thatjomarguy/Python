import webbrowser
import datetime
def flightSearch():
    airportNames = {'Austin':'AUS',
                    'Dallas':'DFW',
                    'San Antonio':'SAT',
                    'Chicago':'ORD',
                    'New York':'JFK',
                    'San Francisco':'SFO',
                    'Los Angeles':'LAX',
                    'Miami':'MIA',
                    'Detroit':'DTW',
                    'Houston':'HOU'}

    for key,value in airportNames.items():
        print(key,end=", ")
    while True:
        start = input('\n'+"What city are you flying from?\n")
        if start in airportNames:
            break
        else:
             print("Invalid city.")

    while True:
        end = input('\n'+"What city do you want to fly to?\n")
        if end in airportNames:
            break
        else:
             print("Invalid city.")

    while True:
        departDate = input('\n'+"Departure Date? Format:YYYY-MM-DD\n")
        try:
            datetime.datetime.strptime(departDate, '%Y-%m-%d')
            break
        except ValueError:
             print("Invalid date.")

    while True:
        returnDate = input('\n'+"Return Date? Format:YYYY-MM-DD\n")
        try:
            datetime.datetime.strptime(returnDate, '%Y-%m-%d')
            break
        except ValueError:
             print("Invalid date.")

    url = 'http://www.google.com/flights/#search;'
    url=url+"f="+airportNames.get(start)+";t="+airportNames.get(end)+";d="+departDate+";r="+returnDate
    print(url)
    webbrowser.open_new_tab(url)

if __name__ == '__main__':
    flightSearch()
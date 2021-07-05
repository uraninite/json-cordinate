
import os
token = input ("")
while 1:
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')
    cordinates = input ("")
    cls()
    cordinates = cordinates.split(",")
    firstCordinate = cordinates[0]
    secondCordinate = cordinates[1]
    end = """{"token": "%s","lat": %s,"lng": %s,"timedOut": false\n}""" % (token, firstCordinate, secondCordinate)
    print(end)

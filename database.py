# coding: utf-8

# In[ ]:

import sqlite3

class database(object):

    def createDatabase(self, name):

        self.databaseName = name

        conn = sqlite3.connect(name + '.sqlite')
        cur = conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS Locations (MotorBus_ID TEXT, locatiton_X TEXT, locatiton_Y TEXT)''')

        return print ('You just created a database named: ' + name)

    def saveBusLocation(js):

        busLocation = js['vs']

        for bus in busLocation:

            busID = (bus['p'])

            locatitonX = (bus['px'])
            locatitonY = (bus['py'])

            cur.execute('''INSERT INTO Locations (MotorBus_ID,  locatiton_X, locatiton_Y)
            VALUES ( ?, ?, ? )''', (busID, locatitonX, locatitonY) )

            conn.commit()

        return print ('You just saved {0} in {0} database'.format(str(len(busLocation)), self.databaseName)

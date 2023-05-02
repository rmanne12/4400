import mysql.connector
from mysql.connector import Error


#Stored Procedures 
def add_airplane_function(airlineID, tail_num, seat_capacity, speed, locationID, 
                            plane_type, skids, propellers, jet_engines):

    if airlineID == '':
        airlineID = None
    if tail_num == '':
        tail_num = None
    if seat_capacity == '':
        seat_capacity = None
    else:
        seat_capacity = int(seat_capacity)
    if speed == '':
        speed = None
    else:
        speed = int(speed)
    if locationID == '':
        locationID = None
    if plane_type == '':
        plane_type = None
    if skids == '':
        skids = None
    else:
        skids = skids.lower() == 'true'
    if propellers == '':
        propellers = None
    if jet_engines == '':
        jet_engines = None


    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('add_airplane', args=(airlineID, tail_num, seat_capacity, 
                                                    speed, locationID, plane_type, skids, propellers, 
                                                    jet_engines))
        for result in cursor.stored_results():
            print(result.fetchall())        
    except Error as e:
        print("Error occured", e)
    finally:
        if (connection.is_connected()):
            connection.commit()
            cursor.close()
            connection.close()
            print("connection closed")

def add_airport_function(airportID, airport_name, city, state, locationID):
    if airportID == '':
        airportID = None
    if airport_name == '':
        airport_name = None
    if city == '':
        city = None
    if state == '':
        state = None
    if locationID == '':
        locationID = None

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('add_airport', args=(airportID, airport_name, city, state, locationID))
        for result in cursor.stored_results():
            print(result.fetchall())        
    except Error as e:
        print("Error occured", e)
    finally:
        if (connection.is_connected()):
            connection.commit()
            cursor.close()
            connection.close()
            print("connection closed")


    

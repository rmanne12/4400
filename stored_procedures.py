import mysql.connector
from mysql.connector import Error


#Stored Procedures 

#1
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

#2
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

#3
def add_person_function(personID, first_name, last_name, locationID, taxID, experience, flying_airline, flying_tail, miles):
    if personID == '':
        personID = None
    if first_name == '':
        first_name = None
    if last_name == '':
        last_name = None
    if locationID == '':
        locationID = None
    if taxID == '':
        taxID = None
    if experience == '':
        experience = None
    else:
        experience = int(experience)
    if flying_airline == '':
        flying_airline = None
    if flying_tail == '':
        flying_tail = None
    if miles == '':
        miles = None
    else: 
        miles = int(miles)
    

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('add_person', args=(personID, first_name, last_name, locationID, taxID, experience, flying_airline, flying_tail, miles))
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

#4
def grant_pilot_license_function(personID, license):
    if personID == '':
        personID = None
    if license == '':
        license = None

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('grant_pilot_license', args=(personID, license))
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

#5
def offer_flight_function(flightID, routeID, support_airline, support_tail, progress, airplane_status, next_time):
    if flightID == '':
        flightID = None
    if routeID == '':
        routeID = None
    if support_airline == '':
        support_airline = None
    if support_tail == '':
        support_tail = None
    if progress == '':
        progress = None
    else: 
        progress = int(progress)
    if airplane_status == '':
        airplane_status = None
    #need to check what the data type is for time; currently just set to string
    if next_time == '': 
        next_time = None

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('offer_flight', args=(flightID, routeID, support_airline, support_tail, progress, airplane_status, next_time))
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

#6
def purchase_ticket_and_seat_function(ticketID, cost, carrier, customer, deplane_at, seat_number):
    if ticketID == '':
        ticketID = None
    if cost == '':
        cost = None
    else: 
        cost = int(cost)
    if carrier == '':
        carrier = None
    if customer == '':
        customer = None
    if deplane_at == '':
        deplane_at = None
    if seat_number == '':
        seat_number = None

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('purchase_ticket_and_seat', args=(ticketID, cost, carrier, customer, deplane_at, seat_number))
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

#7
def add_update_leg_function(legID, distance, departure, arrival):
    if legID == '':
        legID = None
    if distance == '':
        distance = None
    else: 
        distance = int(distance)
    if departure == '':
        departure = None
    if arrival == '':
        arrival = None

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('add_update_leg', args=(legID, distance, departure, arrival))
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

#8
def start_route_function(routeID, legID):
    if routeID == '':
        routeID = None
    if legID == '':
        legID = None

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('start_route', args=(routeID, legID))
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

#9
def extend_route_function(routeID, legID):
    if routeID == '':
        routeID = None
    if legID == '':
        legID = None

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('extend_route', args=(routeID, legID))
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

#10
def flight_landing_function(flightID):
    if flightID == '':
        flightID = None

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('flight_landing', args=(flightID))
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

#11
def flight_takeoff_function(flightID):
    if flightID == '':
        flightID = None

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('flight_takeoff', args=(flightID))
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

#12
def passengers_board_function(flightID):
    if flightID == '':
        flightID = None

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('passengers_board', args=(flightID))
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

#13
def passengers_disembark_function(flightID):
    if flightID == '':
        flightID = None

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('passengers_disembark', args=(flightID))
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

#14
def assign_pilot_function(flightID, personID):
    if flightID == '':
        flightID = None
    if personID == '':
        personID = None

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('assign_pilot', args=(flightID, personID))
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

#15
def recycle_crew_function(flightID):
    if flightID == '':
        flightID = None

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('recycle_crew', args=(flightID))
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

#16
def retire_flight_function(flightID):
    if flightID == '':
        flightID = None

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('retire_flight', args=(flightID))
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

#17
def remove_passenger_role_function(personID):
    if personID == '':
        personID = None

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('remove_passenger_role', args=(personID))
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

#18
def remove_pilot_role_function(personID):
    if personID == '':
        personID = None

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('remove_pilot_role', args=(personID))
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

#19
def flights_in_the_air_function(departing_from, arriving_at, num_flights, flight_list, earliest_arrival, latest_arrival, airplane_list):
    if departing_from == '':
        departing_from = None
    if arriving_at == '':
        arriving_at = None
    if num_flights == '':
        num_flights = None
    else: 
        num_flights = int(num_flights)
    if flight_list == '':
        flight_list = None
    if earliest_arrival == '':
        earliest_arrival = None
    if latest_arrival == '':
        latest_arrival = None
    if airplane_list == '':
        airplane_list = None

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('flights_in_the_air', args=(departing_from, arriving_at, num_flights, flight_list, earliest_arrival, latest_arrival, airplane_list))
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

#20
def flights_on_the_ground_function(departing_from, num_flights, flight_list, earliest_arrival, latest_arrival, airplane_list):
    if departing_from == '':
        departing_from = None
    if num_flights == '':
        num_flights = None
    else: 
        num_flights = int(num_flights)
    if flight_list == '':
        flight_list = None
    if earliest_arrival == '':
        earliest_arrival = None
    if latest_arrival == '':
        latest_arrival = None
    if airplane_list == '':
        airplane_list = None

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('flights_on_the_ground', args=(departing_from, num_flights, flight_list, earliest_arrival, latest_arrival, airplane_list))
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

#21
def people_in_the_air_function(departing_from, arriving_at, num_airplanes, airplane_list, flight_list, earliest_arrival, latest_arrival, num_pilots, num_passengers, joint_pilots_passengers, person_list):
    if departing_from == '':
        departing_from = None
    if arriving_at == '':
        arriving_at = None
    if num_airplanes == '':
        num_airplanes = None
    else: 
        num_airplanes = int(num_airplanes)
    if airplane_list == '':
        airplane_list = None
    if flight_list == '':
        flight_list = None
    if earliest_arrival == '':
        earliest_arrival = None
    if latest_arrival == '':
        latest_arrival = None
    if num_pilots == '':
        num_pilots = None
    else: 
        num_pilots = int(num_pilots)
    if num_passengers == '':
         num_passengers = None
    else: 
        num_passengers = int(num_passengers)
    if joint_pilots_passengers == '':
        joint_pilots_passengers = None
    if person_list == '':
        person_list = None
    

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('people_in_the_air', args=(departing_from, arriving_at, num_airplanes, airplane_list, flight_list, earliest_arrival, latest_arrival, num_pilots, num_passengers, joint_pilots_passengers, person_list))
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

#22
def people_on_the_ground_function(departing_from, airport, airport_name, city, state, num_pilots, num_passengers, joint_pilots_passengers, person_list):
    if departing_from == '':
        departing_from = None
    if airport == '':
        airport = None
    if airport_name == '':
        airport_name = None
    if city == '':
        city = None
    if state == '':
        state = None
    if num_pilots == '':
        num_pilots = None
    else: 
        num_pilots = int(num_pilots)
    if num_passengers == '':
         num_passengers = None
    else: 
        num_passengers = int(num_passengers)
    if joint_pilots_passengers == '':
        joint_pilots_passengers = None
    if person_list == '':
        person_list = None
    

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('people_on_the_ground', args=(departing_from, airport, airport_name, city, state, num_pilots, num_passengers, joint_pilots_passengers, person_list))
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

#23
def route_summary_function(route, num_legs, leg_sequence, route_length, num_flights, flight_list, airport_sequence):
    if route == '':
        route = None
    if num_legs == '':
        num_legs = None
    else:
        num_legs = int(num_legs)
    if leg_sequence == '':
        leg_sequence = None
    if route_length == '':
        route_length = None
    else:
        route_length = int(route_length)
    if num_flights == '':
        num_flights = None
    else: 
        num_flights = int(num_flights)
    if flight_list == '':
        flight_list = None
    if airport_sequence == '':
        airport_sequence = None
    

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('route_summary', args=(route, num_legs, leg_sequence, route_length, num_flights, flight_list, airport_sequence))
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

#24
def alternative_airports_function(city, state, num_airports, airport_code_list, airport_name_list):
    if city == '':
        city = None
    if state == '':
        state = None
    if num_airports == '':
        num_airports = None
    else:
        num_airports = int(num_airports)
    if airport_code_list == '':
        airport_code_list = None
    if airport_name_list == '':
        airport_name_list = None
    

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure
        cursor.callproc('alternative_airports', args=(city, state, num_airports, airport_code_list, airport_name_list))
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

#25
def simulation_cycle_function():
    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the stored procedure with no arguments
        cursor.callproc('simulation_cycle') 
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
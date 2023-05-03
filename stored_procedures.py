import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
import datetime
from tkinter import ttk
import tkinter as tk



#Stored Procedures 

#1
def add_airplane_function(airlineID, tail_num, seat_capacity, speed, locationID, 
                            plane_type, skids, propellers, jet_engines):




    try: 


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
        messagebox.showerror("Error", "This is an error message.")
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
        messagebox.showerror("Error", "This is an error message.")
        print("Error occured", e)
    finally:
        if (connection.is_connected()):
            connection.commit()
            cursor.close()
            connection.close()
            print("connection closed")

#3
def add_person_function(personID, first_name, last_name, locationID, taxID, experience, flying_airline, flying_tail, miles):
    
    

    try: 
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
        messagebox.showerror("Error", "This is an error message.")
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
        messagebox.showerror("Error", "This is an error message.")
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
        messagebox.showerror("Error", "This is an error message.")
        print("Error occured", e)
    finally:
        if (connection.is_connected()):
            connection.commit()
            cursor.close()
            connection.close()
            print("connection closed")

#6
def purchase_ticket_and_seat_function(ticketID, cost, carrier, customer, deplane_at, seat_number):
    

    try: 
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
        messagebox.showerror("Error", "This is an error message.")
        print("Error occured", e)
    finally:
        if (connection.is_connected()):
            connection.commit()
            cursor.close()
            connection.close()
            print("connection closed")

#7
def add_update_leg_function(legID, distance, departure, arrival):

    try: 
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
        messagebox.showerror("Error", "This is an error message.")
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
        messagebox.showerror("Error", "This is an error message.")
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
        messagebox.showerror("Error", "This is an error message.")
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
        messagebox.showerror("Error", "This is an error message.")
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
        messagebox.showerror("Error", "This is an error message.")
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
        messagebox.showerror("Error", "This is an error message.")
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
        messagebox.showerror("Error", "This is an error message.")
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
        messagebox.showerror("Error", "This is an error message.")
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
        messagebox.showerror("Error", "This is an error message.")
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
        messagebox.showerror("Error", "This is an error message.")
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
        messagebox.showerror("Error", "This is an error message.")
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
        messagebox.showerror("Error", "This is an error message.")
        print("Error occured", e)
    finally:
        if (connection.is_connected()):
            connection.commit()
            cursor.close()
            connection.close()
            print("connection closed")

#19
def flights_in_the_air_function(frame):
    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the view
        cursor.execute("SELECT * FROM flights_in_the_air")

        # fetch all rows from the result set
        rows = cursor.fetchall()

        columns = ("departing_from", "arriving_at", "num_flights", "flight_list", "earliest_arrival", "latest_arrival", "airplane_list")
        tree = ttk.Treeview(frame, columns=columns, show="headings")
        tree.heading("departing_from", text="departing_from")
        tree.heading("arriving_at", text="arriving_at")
        tree.heading("num_flights", text="num_flights")
        tree.heading("flight_list", text="flight_list")
        tree.heading("earliest_arrival", text="earliest_arrival")
        tree.heading("latest_arrival", text="latest_arrival")
        tree.heading("airplane_list", text="airplane_list")

        # Set font size
        tree.column("departing_from", width=100, minwidth=100, stretch=tk.NO)
        tree.column("arriving_at", width=100, minwidth=100, stretch=tk.NO)
        tree.column("num_flights", width=100, minwidth=100, stretch=tk.NO)
        tree.column("flight_list", width=100, minwidth=100, stretch=tk.NO)
        tree.column("earliest_arrival", width=100, minwidth=100, stretch=tk.NO)
        tree.column("latest_arrival", width=100, minwidth=100, stretch=tk.NO)
        tree.column("airplane_list", width=100, minwidth=100, stretch=tk.NO)

        # Set row height
        style = ttk.Style()
        style.configure("Treeview", rowheight=20, font=("Arial", 8))


        for row in rows:
            tree.insert("", "end", values=row)

        return tree

    except Error as e:
        messagebox.showerror("Error", "This is an error message.")
        print("Error occured", e)
    finally:
        if (connection.is_connected()):
            connection.commit()
            cursor.close()
            connection.close()
            print("connection closed")


#20
def flights_on_the_ground_function(frame):

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        # call the view 
        cursor.execute("SELECT * FROM flights_on_the_ground")

        # fetch all rows from the result set
        rows = cursor.fetchall()

        columns = ("departing_from", "num_flights", "flight_list", "earliest_arrival", "latest_arrival", "airplane_list")
        tree = ttk.Treeview(frame, columns=columns, show="headings")
        tree.heading("departing_from", text="departing_from")
        tree.heading("num_flights", text="num_flights")
        tree.heading("flight_list", text="flight_list")
        tree.heading("earliest_arrival", text="earliest_arrival")
        tree.heading("latest_arrival", text="latest_arrival")
        tree.heading("airplane_list", text="airplane_list")

        # Set font size
        tree.column("departing_from", width=100, minwidth=100, stretch=tk.NO)
        tree.column("num_flights", width=100, minwidth=100, stretch=tk.NO)
        tree.column("flight_list", width=100, minwidth=100, stretch=tk.NO)
        tree.column("earliest_arrival", width=100, minwidth=100, stretch=tk.NO)
        tree.column("latest_arrival", width=100, minwidth=100, stretch=tk.NO)
        tree.column("airplane_list", width=100, minwidth=100, stretch=tk.NO)

        # Set row height
        style = ttk.Style()
        style.configure("Treeview", rowheight=20, font=("Arial", 8))


        for row in rows:
            tree.insert("", "end", values=row)

        return tree

    except Error as e:
        messagebox.showerror("Error", "This is an error message.")
        print("Error occured", e)
    finally:
        if (connection.is_connected()):
            connection.commit()
            cursor.close()
            connection.close()
            print("connection closed")

#21
def people_in_the_air_function(frame):
    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()

        # call the view 
        cursor.execute("SELECT * FROM people_in_the_air")

        # fetch all rows from the result set
        rows = cursor.fetchall()

        columns = ("departing_from", "arriving_at", "num_airplanes", "airplane_list", "flight_list", "earliest_arrival", "latest_arrival", "num_pilots", "num_passengers", "joint_pilots_passengers", "person_list")
        tree = ttk.Treeview(frame, columns=columns, show="headings")
        tree.heading("departing_from", text="departing_from")
        tree.heading("arriving_at", text="arriving_at")
        tree.heading("num_airplanes", text="num_airplanes")
        tree.heading("airplane_list", text="airplane_list")
        tree.heading("flight_list", text="flight_list")
        tree.heading("earliest_arrival", text="earliest_arrival")
        tree.heading("latest_arrival", text="latest_arrival")
        tree.heading("num_pilots", text="num_pilots")
        tree.heading("num_passengers", text="num_passengers")
        tree.heading("joint_pilots_passengers", text="joint_pilots_passengers")
        tree.heading("person_list", text="person_list")

        # Set font size
        tree.column("departing_from", width=100, minwidth=100, stretch=tk.NO)
        tree.column("arriving_at", width=100, minwidth=100, stretch=tk.NO)
        tree.column("num_airplanes", width=100, minwidth=100, stretch=tk.NO)
        tree.column("airplane_list", width=100, minwidth=100, stretch=tk.NO)
        tree.column("flight_list", width=100, minwidth=100, stretch=tk.NO)
        tree.column("earliest_arrival", width=100, minwidth=100, stretch=tk.NO)
        tree.column("latest_arrival", width=100, minwidth=100, stretch=tk.NO)
        tree.column("num_pilots", width=100, minwidth=100, stretch=tk.NO)
        tree.column("num_passengers", width=100, minwidth=100, stretch=tk.NO)
        tree.column("joint_pilots_passengers", width=100, minwidth=100, stretch=tk.NO)
        tree.column("person_list", width=100, minwidth=100, stretch=tk.NO)

        # Set row height
        style = ttk.Style()
        style.configure("Treeview", rowheight=20, font=("Arial", 8))

        for row in rows:
            tree.insert("", "end", values=row)

        return tree

    except Error as e:
        messagebox.showerror("Error", "This is an error message.")
        print("Error occured", e)
    finally:
        if (connection.is_connected()):
            connection.commit()
            cursor.close()
            connection.close()
            print("connection closed")

            






#22
def people_on_the_ground_function(frame):

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()

        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()

        # call the view 
        cursor.execute("SELECT * FROM people_on_the_ground")

        # fetch all rows from the result set
        rows = cursor.fetchall()

        
        columns = ("departing_from", "airport", "airport_name", "city", "state", "num_pilots", "num_passengers", "joint_pilots_passengers", "person_list")
        tree = ttk.Treeview(frame, columns=columns, show="headings")
        tree.heading("departing_from", text="departing_from")
        tree.heading("airport", text="airport")
        tree.heading("airport_name", text="airport_name")
        tree.heading("city", text="city")
        tree.heading("state", text="state")
        tree.heading("num_pilots", text="num_pilots")
        tree.heading("num_passengers", text="num_passengers")
        tree.heading("joint_pilots_passengers", text="joint_pilots_passengers")
        tree.heading("person_list", text="person_list")

        # Set font size
        tree.column("departing_from", width=100, minwidth=100, stretch=tk.NO)
        tree.column("airport", width=100, minwidth=100, stretch=tk.NO)
        tree.column("airport_name", width=100, minwidth=100, stretch=tk.NO)
        tree.column("city", width=100, minwidth=100, stretch=tk.NO)
        tree.column("state", width=100, minwidth=100, stretch=tk.NO)
        tree.column("num_pilots", width=100, minwidth=100, stretch=tk.NO)
        tree.column("num_passengers", width=100, minwidth=100, stretch=tk.NO)
        tree.column("joint_pilots_passengers", width=100, minwidth=100, stretch=tk.NO)
        tree.column("person_list", width=100, minwidth=100, stretch=tk.NO)

        # Set row height
        style = ttk.Style()
        style.configure("Treeview", rowheight=20, font=("Arial", 8))

        for row in rows:
            tree.insert("", "end", values=row)

        return tree


    except Error as e:
        messagebox.showerror("Error", "This is an error message.")
        print("Error occured", e)
    finally:
        if (connection.is_connected()):
            connection.commit()
            cursor.close()
            connection.close()
            print("connection closed")

#23
def route_summary_function(frame):
    

    try: 
        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()
        
        # call the view 
        cursor.execute("SELECT * FROM route_summary")

        # fetch all rows from the result set
        rows = cursor.fetchall()

        
        columns = ("route", "num_legs", "leg_sequence", "route_length", "num_flights", "flight_list", "airport_sequence")
        tree = ttk.Treeview(frame, columns=columns, show="headings")
        tree.heading("route", text="route")
        tree.heading("num_legs", text="num_legs")
        tree.heading("leg_sequence", text="leg_sequence")
        tree.heading("route_length", text="route_length")
        tree.heading("num_flights", text="num_flights")
        tree.heading("flight_list", text="flight_list")
        tree.heading("airport_sequence", text="airport_sequence")

        # Set font size
        tree.column("route", width=100, minwidth=100, stretch=tk.NO)
        tree.column("num_legs", width=100, minwidth=100, stretch=tk.NO)
        tree.column("leg_sequence", width=100, minwidth=100, stretch=tk.NO)
        tree.column("route_length", width=100, minwidth=100, stretch=tk.NO)
        tree.column("num_flights", width=100, minwidth=100, stretch=tk.NO)
        tree.column("flight_list", width=100, minwidth=100, stretch=tk.NO)
        tree.column("airport_sequence", width=100, minwidth=100, stretch=tk.NO)

        # Set row height
        style = ttk.Style()
        style.configure("Treeview", rowheight=20, font=("Arial", 8))

        for row in rows:
            tree.insert("", "end", values=row)

        return tree



    except Error as e:
        messagebox.showerror("Error", "This is an error message.")
        print("Error occured", e)
    finally:
        if (connection.is_connected()):
            connection.commit()
            cursor.close()
            connection.close()
            print("connection closed")

#24
def alternative_airports_function(frame):
    
    try: 

        # establish database connection
        connection = mysql.connector.connect(user='root', password='Deb@tersql2003',
                                    host='localhost', database='flight_management')
        # create a cursor object
        cursor = connection.cursor()

        # call the view 
        cursor.execute("SELECT * FROM route_summary")

        # fetch all rows from the result set
        rows = cursor.fetchall()

        
        columns = ("city", "state", "num_airports", "airport_code_list", "airport_name_list")
        tree = ttk.Treeview(frame, columns=columns, show="headings")
        tree.heading("city", text="city")
        tree.heading("state", text="state")
        tree.heading("num_airports", text="num_airports")
        tree.heading("airport_code_list", text="airport_code_list")
        tree.heading("airport_name_list", text="airport_name_list")

        # Set font size
        tree.column("city", width=100, minwidth=100, stretch=tk.NO)
        tree.column("state", width=100, minwidth=100, stretch=tk.NO)
        tree.column("num_airports", width=100, minwidth=100, stretch=tk.NO)
        tree.column("airport_code_list", width=100, minwidth=100, stretch=tk.NO)
        tree.column("airport_name_list", width=100, minwidth=100, stretch=tk.NO)

        # Set row height
        style = ttk.Style()
        style.configure("Treeview", rowheight=20, font=("Arial", 8))

        for row in rows:
            tree.insert("", "end", values=row)

        return tree

    except Error as e:
        messagebox.showerror("Error", "This is an error message.")
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
        messagebox.showerror("Error", "This is an error message.")
        print("Error occured", e)
    finally:
        if (connection.is_connected()):
            connection.commit()
            cursor.close()
            connection.close()
            print("connection closed")

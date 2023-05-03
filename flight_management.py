import tkinter as tk
from tkinter import *
from stored_procedures import *

window = tk.Tk()
window.title("Flight Management System")
window.geometry("650x800")

#Create Frames 
front_page = Frame(window)
airplane_page = Frame(window)
pilots_page = Frame(window)
people_page = Frame(window)
flights_page = Frame(window)
routes_page = Frame(window)
tickets_page = Frame(window)
airports_page = Frame(window)
views_simulation_page = Frame(window)


front_page.grid(row=0, column=0, sticky="nsew")
airplane_page.grid(row=0, column=0, sticky="nsew")
pilots_page.grid(row=0, column=0, sticky="nsew")
people_page.grid(row=0, column=0, sticky="nsew")
flights_page.grid(row=0, column=0, sticky="nsew")
routes_page.grid(row=0, column=0, sticky="nsew")
tickets_page.grid(row=0, column=0, sticky="nsew")
airports_page.grid(row=0, column=0, sticky="nsew")
views_simulation_page.grid(row=0, column=0, sticky="nsew")

#Create Frames for Stored Procedures and views

#Stored Procedure Frame for Airplane
add_airplane_frame = Frame(window) 
add_airplane_frame.grid(row=0, column=0, sticky="nsew")

#Stored Procedure Frames for People
add_person_frame = Frame(window) 
add_person_frame.grid(row=0, column=0, sticky="nsew")

add_person_frame = Frame(window) 
add_person_frame.grid(row=0, column=0, sticky="nsew")

passengers_board_frame = Frame(window)
passengers_board_frame.grid(row=0, column=0, sticky="nsew")

passengers_disembark_frame = Frame(window)
passengers_disembark_frame.grid(row=0, column=0, sticky="nsew")

remove_passenger_role_frame = Frame(window)
remove_passenger_role_frame.grid(row=0, column=0, sticky="nsew")

#Stored Procedure Frames for Pilots 
grant_pilot_license_frame = Frame(window)
grant_pilot_license_frame.grid(row=0, column=0, sticky="nsew")

assign_pilot_frame = Frame(window)
assign_pilot_frame.grid(row=0, column=0, sticky="nsew")


recycle_crew_frame = Frame(window)
recycle_crew_frame.grid(row=0, column=0, sticky="nsew")

remove_pilot_role_frame = Frame(window)
remove_pilot_role_frame.grid(row=0, column=0, sticky="nsew")

#Stored Procedure Frames for Flights
offer_flight_frame = Frame(window)
offer_flight_frame.grid(row=0, column=0, sticky="nsew")

flight_landing_frame = Frame(window)
flight_landing_frame.grid(row=0, column=0, sticky="nsew")

flight_takeoff_frame = Frame(window)
flight_takeoff_frame.grid(row=0, column=0, sticky="nsew")

retire_flight_frame = Frame(window)
retire_flight_frame.grid(row=0, column=0, sticky="nsew")

#Stored Procedure Frames for Routes
add_update_leg_frame = Frame(window)
add_update_leg_frame.grid(row=0, column=0, sticky="nsew")

start_route_frame = Frame(window)
start_route_frame.grid(row=0, column=0, sticky="nsew")

extend_route_frame = Frame(window)
extend_route_frame.grid(row=0, column=0, sticky="nsew")

#Stored Procedure Frame for Routes
purchase_ticket_and_seat_frame = Frame(window)
purchase_ticket_and_seat_frame.grid(row=0, column=0, sticky="nsew")


#Stored Procedure Frame for Airports
add_airport_frame = Frame(window)
add_airport_frame.grid(row=0, column=0, sticky="nsew")

#Stored Procedure Frame for Views and Simulation Cycle 

flights_in_the_air_frame = Frame(window)
flights_in_the_air_frame.grid(row=0, column=0, sticky="nsew")

flights_on_the_ground_frame = Frame(window)
flights_on_the_ground_frame.grid(row=0, column=0, sticky="nsew")

people_in_the_air_frame = Frame(window)
people_in_the_air_frame.grid(row=0, column=0, sticky="nsew")

people_on_the_ground_frame = Frame(window)
people_on_the_ground_frame.grid(row=0, column=0, sticky="nsew")

route_summary_frame = Frame(window)
route_summary_frame.grid(row=0, column=0, sticky="nsew")

alternative_airports_frame = Frame(window)
alternative_airports_frame.grid(row=0, column=0, sticky="nsew")

simulation_cycle_frame = Frame(window)
simulation_cycle_frame.grid(row=0, column=0, sticky="nsew")


# Create the buttons and add them to the grid
btn1 = tk.Button(front_page, text="Airplanes", command=lambda: airplane_page.tkraise(), width=30, height=10)
btn1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

btn2 = tk.Button(front_page, text="Pilots", command=lambda: pilots_page.tkraise(), width=30, height=10)
btn2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

btn3 = tk.Button(front_page, text="People", command=lambda: people_page.tkraise(), width=30, height=10)
btn3.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

btn4 = tk.Button(front_page, text="Flights", command=lambda: flights_page.tkraise(), width=30, height=10)
btn4.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

btn5 = tk.Button(front_page, text="Routes", command=lambda: routes_page.tkraise(), width=30, height=10)
btn5.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

btn6 = tk.Button(front_page, text="Tickets", command=lambda: tickets_page.tkraise(), width=30, height=10)
btn6.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

btn7 = tk.Button(front_page, text="Airports", command=lambda: airports_page.tkraise(), width=30, height=10)
btn7.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

btn8 = tk.Button(front_page, text="Views and Simulation Cycle", command=lambda: views_simulation_page.tkraise(), width=30, height=10)
btn8.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")


# Airplane -> 1

airplane_page_title = Label(airplane_page, text='Airplanes Page')
airplane_page_title.pack(pady=20)
goto_add_airplane = tk.Button(airplane_page, text="add_airplane()", command=lambda: add_airplane_frame.tkraise(), width=15, height=5)
goto_add_airplane.pack()
airplane_back_button = tk.Button(airplane_page, text="Back", command=lambda: front_page.tkraise(), width=15, height=5)
airplane_back_button.pack()


add_airplane_title = Label(add_airplane_frame, text='add_airplane()')
add_airplane_title.grid(row=0, column=2)

# create labels and entry boxes for airlineID, tail_num, seat_capacity, speed, and location_id
add_airplane_airlineID_label = tk.Label(add_airplane_frame, text="airlineID")
add_airplane_airlineID_label.grid(row=1, column=0)

add_airplane_airlineID_entry = tk.Entry(add_airplane_frame)
add_airplane_airlineID_entry.grid(row=1, column=1)

add_airplane_tail_num_label = tk.Label(add_airplane_frame, text="tail_num")
add_airplane_tail_num_label.grid(row=2, column=0)

add_airplane_tail_num_entry = tk.Entry(add_airplane_frame)
add_airplane_tail_num_entry.grid(row=2, column=1)

add_airplane_seat_capacity_label = tk.Label(add_airplane_frame, text="seat_capacity")
add_airplane_seat_capacity_label.grid(row=3, column=0)
add_airplane_seat_capacity_entry = tk.Entry(add_airplane_frame)
add_airplane_seat_capacity_entry.grid(row=3, column=1)

add_airplane_speed_label = tk.Label(add_airplane_frame, text="speed")
add_airplane_speed_label.grid(row=4, column=0)
add_airplane_speed_entry = tk.Entry(add_airplane_frame)
add_airplane_speed_entry.grid(row=4, column=1)

add_airplane_location_id_label = tk.Label(add_airplane_frame, text="location_id")
add_airplane_location_id_label.grid(row=5, column=0)
add_airplane_location_id_entry = tk.Entry(add_airplane_frame)
add_airplane_location_id_entry.grid(row=5, column=1)

# create labels and entry boxes for skids, plane_type, propeller, and jet_engines
add_airplane_skids_label = tk.Label(add_airplane_frame, text="skids")
add_airplane_skids_label.grid(row=1, column=2)
add_airplane_skids_entry = tk.Entry(add_airplane_frame)
add_airplane_skids_entry.grid(row=1, column=3)

add_airplane_plane_type_label = tk.Label(add_airplane_frame, text="plane_type")
add_airplane_plane_type_label.grid(row=2, column=2)
add_airplane_plane_type_entry = tk.Entry(add_airplane_frame)
add_airplane_plane_type_entry.grid(row=2, column=3)

add_airplane_propeller_label = tk.Label(add_airplane_frame, text="propeller")
add_airplane_propeller_label.grid(row=3, column=2)
add_airplane_propeller_entry = tk.Entry(add_airplane_frame)
add_airplane_propeller_entry.grid(row=3, column=3)

add_airplane_jet_engines_label = tk.Label(add_airplane_frame, text="jet_engines")
add_airplane_jet_engines_label.grid(row=4, column=2)
add_airplane_jet_engines_entry = tk.Entry(add_airplane_frame)
add_airplane_jet_engines_entry.grid(row=4, column=3)

add_airplane_back_button = tk.Button(add_airplane_frame, text="Back", command=lambda: airplane_page.tkraise(), width=15, height=5)
add_airplane_back_button.grid(row=6, column=1)                                 

add_airplane_btn = tk.Button(add_airplane_frame, text="Commit", command=lambda: add_airplane_function(
    add_airplane_airlineID_entry.get(), add_airplane_tail_num_entry.get(), add_airplane_seat_capacity_entry.get(), add_airplane_speed_entry.get(),
    add_airplane_location_id_entry.get(), add_airplane_plane_type_entry.get(), add_airplane_skids_entry.get(), add_airplane_propeller_entry.get(), 
    add_airplane_jet_engines_entry.get()), width=15, height=5)
add_airplane_btn.grid(row=6, column=2)




# Pilots -> 4, 14, 15, 18 ------------------------------------------------------------------------------------------------
pilots_page_title = Label(pilots_page, text='Pilots Page')
pilots_page_title.pack(pady=20)

goto_grant_pilot_license = tk.Button(pilots_page, text="grant_pilot_license()", command=lambda: grant_pilot_license_frame.tkraise(), width=15, height=5)
goto_grant_pilot_license.pack(pady=20)

########################################################################   Grant_Pilot_License 
grant_pilot_license_frame_title = tk.Label(grant_pilot_license_frame, text="grant_pilot_license()")
grant_pilot_license_frame_title.grid(row=0, column=2)

grant_pilot_license_personID_label = tk.Label(grant_pilot_license_frame, text="personID")
grant_pilot_license_personID_label.grid(row=1, column=0)
grant_pilot_license_personID_entry = tk.Entry(grant_pilot_license_frame)
grant_pilot_license_personID_entry.grid(row=1, column=1)

grant_pilot_license_license_label = tk.Label(grant_pilot_license_frame, text="license")
grant_pilot_license_license_label.grid(row=2, column=0)
grant_pilot_license_license_entry = tk.Entry(grant_pilot_license_frame)
grant_pilot_license_license_entry.grid(row=2, column=1)

grant_pilot_license_frame_back_btn = tk.Button(grant_pilot_license_frame, text="Back", command=lambda: pilots_page.tkraise(), width=15, height=5)
grant_pilot_license_frame_back_btn.grid(row=3, column=1)  

grant_pilot_license_frame_btn = tk.Button(grant_pilot_license_frame, text="Commit", command=lambda: grant_pilot_license_function(grant_pilot_license_personID_entry.get(),
grant_pilot_license_license_entry.get()), width=15, height=5)
grant_pilot_license_frame_btn.grid(row=3, column=2) 
########################################################################




########################################################################   assign_pilot

goto_assign_pilot = tk.Button(pilots_page, text="assign_pilot()", command=lambda: assign_pilot_frame.tkraise(), width=15, height=5)
goto_assign_pilot.pack(pady=20)

assign_pilot_frame_title = tk.Label(assign_pilot_frame, text="assign_pilot()")
assign_pilot_frame_title.grid(row=0, column=2)

assign_pilot_flightID_label = tk.Label(assign_pilot_frame, text="flightID")
assign_pilot_flightID_label.grid(row=1, column=0)
assign_pilot_flightID_entry = tk.Entry(assign_pilot_frame)
assign_pilot_flightID_entry.grid(row=1, column=1)

assign_pilot_personID_label = tk.Label(assign_pilot_frame, text="personID")
assign_pilot_personID_label.grid(row=2, column=0)
assign_pilot_personID_entry = tk.Entry(assign_pilot_frame)
assign_pilot_personID_entry.grid(row=2, column=1)

grant_pilot_license_frame_back_btn = tk.Button(assign_pilot_frame, text="Back", command=lambda: pilots_page.tkraise(), width=15, height=5)
grant_pilot_license_frame_back_btn.grid(row=3, column=1)  

grant_pilot_license_frame_btn = tk.Button(assign_pilot_frame, text="Commit", command=lambda: assign_pilot_function(
    assign_pilot_flightID_entry.get(), assign_pilot_personID_entry.get()
), width=15, height=5)
grant_pilot_license_frame_btn.grid(row=3, column=2) 
########################################################################



########################################################################  recycle_crew
goto_recycle_crew = tk.Button(pilots_page, text="recycle_crew()", command=lambda: recycle_crew_frame.tkraise(), width=15, height=5)
goto_recycle_crew.pack(pady=20)

recycle_crew_frame_title = tk.Label(recycle_crew_frame, text="recycle_crew()")
recycle_crew_frame_title.grid(row=0, column=2)

recycle_crew_flightID_label = tk.Label(recycle_crew_frame, text="flightID")
recycle_crew_flightID_label.grid(row=1, column=0)
recycle_crew_flightID_entry = tk.Entry(recycle_crew_frame)
recycle_crew_flightID_entry.grid(row=1, column=1)

grant_pilot_license_frame_back_btn = tk.Button(recycle_crew_frame, text="Back", command=lambda: pilots_page.tkraise(), width=15, height=5)
grant_pilot_license_frame_back_btn.grid(row=2, column=1)  

recycle_crew_frame_btn = tk.Button(recycle_crew_frame, text="Commit", command=lambda: recycle_crew_function(
    recycle_crew_flightID_entry.get()
), width=15, height=5)
recycle_crew_frame_btn.grid(row=2, column=2) 
########################################################################



########################################################################  remove_pilot_role
goto_remove_pilot_role = tk.Button(pilots_page, text="remove_pilot_role()", command=lambda: remove_pilot_role_frame.tkraise(), width=15, height=5)
goto_remove_pilot_role.pack(pady=20)

remove_pilot_role_frame_title = tk.Label(remove_pilot_role_frame, text="remove_pilot_role()")
remove_pilot_role_frame_title.grid(row=0, column=2)

remove_pilot_role_personID_label = tk.Label(remove_pilot_role_frame, text="personID")
remove_pilot_role_personID_label.grid(row=1, column=0)
remove_pilot_role_personID_entry = tk.Entry(remove_pilot_role_frame)
remove_pilot_role_personID_entry.grid(row=1, column=1)

remove_pilot_role_frame_back_btn = tk.Button(remove_pilot_role_frame, text="Back", command=lambda: pilots_page.tkraise(), width=15, height=5)
remove_pilot_role_frame_back_btn.grid(row=2, column=1)  

remove_pilot_role_frame_btn = tk.Button(remove_pilot_role_frame, text="Commit", command=lambda: remove_pilot_role_function(
    remove_pilot_role_personID_entry.get()
), width=15, height=5)
remove_pilot_role_frame_btn.grid(row=2, column=2)
########################################################################

pilots_back_button = tk.Button(pilots_page, text="Back", command=lambda: front_page.tkraise(), width=15, height=5)
pilots_back_button.pack(pady=20)
# --------------------------------------------------------------------------------------------------------------------------------






# People Page -> 3, 12?, 13?, 17 ------------------------------------------------------------------------------------------------
people_page_title = Label(people_page, text='People Page')
people_page_title.pack(pady=20)

######################################################################## add_person()
goto_add_person = tk.Button(people_page, text="add_person()", command=lambda: add_person_frame.tkraise(), width=15, height=5)
goto_add_person.pack(pady=20)

add_airplane_title = Label(add_person_frame, text='add_person()')
add_airplane_title.grid(row=0, column=2)

# create labels and entry boxes for airlineID, tail_num, seat_capacity, speed, and location_id
add_person_personID_label = tk.Label(add_person_frame, text="personID")
add_person_personID_label.grid(row=1, column=0)
add_person_personID_entry = tk.Entry(add_person_frame)
add_person_personID_entry.grid(row=1, column=1)

add_person_first_name_label = tk.Label(add_person_frame, text="first_name")
add_person_first_name_label.grid(row=2, column=0)
add_person_first_name_entry = tk.Entry(add_person_frame)
add_person_first_name_entry.grid(row=2, column=1)

add_person_last_name_label = tk.Label(add_person_frame, text="last_name")
add_person_last_name_label.grid(row=3, column=0)
add_person_last_name_entry = tk.Entry(add_person_frame)
add_person_last_name_entry.grid(row=3, column=1)

add_person_locationID_label = tk.Label(add_person_frame, text="locationID")
add_person_locationID_label.grid(row=4, column=0)
add_person_locationID_entry = tk.Entry(add_person_frame)
add_person_locationID_entry.grid(row=4, column=1)

add_person_taxID_label = tk.Label(add_person_frame, text="taxID")
add_person_taxID_label.grid(row=5, column=0)
add_person_taxID_entry = tk.Entry(add_person_frame)
add_person_taxID_entry.grid(row=5, column=1)

add_person_experience_label = tk.Label(add_person_frame, text="experience")
add_person_experience_label.grid(row=1, column=2)
add_person_experience_entry = tk.Entry(add_person_frame)
add_person_experience_entry.grid(row=1, column=3)

add_person_flying_airline_label = tk.Label(add_person_frame, text="flying_airline")
add_person_flying_airline_label.grid(row=2, column=2)
add_person_flying_airline_entry = tk.Entry(add_person_frame)
add_person_flying_airline_entry.grid(row=2, column=3)

add_person_flying_tail_label = tk.Label(add_person_frame, text="flying_tail")
add_person_flying_tail_label.grid(row=3, column=2)
add_person_flying_tail_entry = tk.Entry(add_person_frame)
add_person_flying_tail_entry.grid(row=3, column=3)

add_person_miles_label = tk.Label(add_person_frame, text="miles")
add_person_miles_label.grid(row=4, column=2)
add_person_miles_entry = tk.Entry(add_person_frame)
add_person_miles_entry.grid(row=4, column=3)

add_airplane_back_button = tk.Button(add_person_frame, text="Back", command=lambda: people_page.tkraise(), width=15, height=5)
add_airplane_back_button.grid(row=6, column=1)                                 

add_person_frame_btn = tk.Button(add_person_frame, text="Commit", command=lambda: add_person_function(
    add_person_personID_entry.get(), add_person_first_name_entry.get(), add_person_last_name_entry.get(),
    add_person_locationID_entry.get(), add_person_taxID_entry.get(), add_person_experience_entry.get(),
    add_person_flying_airline_entry.get(), add_person_flying_tail_entry.get(), add_person_miles_entry.get()
), width=15, height=5)
add_person_frame_btn.grid(row=6, column=2)
########################################################################




######################################################################## passengers_board
goto_passengers_board = tk.Button(people_page, text="passengers_board()", command=lambda: passengers_board_frame.tkraise(), width=15, height=5)
goto_passengers_board.pack(pady=20)

passengers_board_frame_title = tk.Label(passengers_board_frame, text="passengers_board()")
passengers_board_frame_title.grid(row=0, column=2)

passengers_board_flightID_label = tk.Label(passengers_board_frame, text="flightID")
passengers_board_flightID_label.grid(row=1, column=0)
passengers_board_flightID_entry = tk.Entry(passengers_board_frame)
passengers_board_flightID_entry.grid(row=1, column=1)

passengers_board_frame_back_btn = tk.Button(passengers_board_frame, text="Back", command=lambda: people_page.tkraise(), width=15, height=5)
passengers_board_frame_back_btn.grid(row=2, column=1)  

passengers_board_frame_btn = tk.Button(passengers_board_frame, text="Commit", command=lambda: passengers_board_function(
    passengers_board_flightID_entry.get()
), width=15, height=5)
passengers_board_frame_btn.grid(row=2, column=2)

########################################################################


######################################################################## passengers_disembark
goto_passengers_disembark = tk.Button(people_page, text="passengers_disembark()", command=lambda: passengers_disembark_frame.tkraise(), width=15, height=5)
goto_passengers_disembark.pack(pady=20)

passengers_disembark_frame_title = tk.Label(passengers_disembark_frame, text="passengers_disembark()")
passengers_disembark_frame_title.grid(row=0, column=2)

passengers_disembark_flightID_label = tk.Label(passengers_disembark_frame, text="flightID")
passengers_disembark_flightID_label.grid(row=1, column=0)
passengers_disembark_flightID_entry = tk.Entry(passengers_disembark_frame)
passengers_disembark_flightID_entry.grid(row=1, column=1)

passengers_disembark_frame_back_btn = tk.Button(passengers_disembark_frame, text="Back", command=lambda: people_page.tkraise(), width=15, height=5)
passengers_disembark_frame_back_btn.grid(row=2, column=1)  

passengers_disembark_frame_btn = tk.Button(passengers_disembark_frame, text="Commit",command=lambda: passengers_disembark_function(
    passengers_disembark_flightID_entry.get()
), width=15, height=5)
passengers_disembark_frame_btn.grid(row=2, column=2)
########################################################################


######################################################################## remove_passenger_role
goto_remove_passenger_role = tk.Button(people_page, text="remove_passenger_role()", command=lambda: remove_passenger_role_frame.tkraise(), width=15, height=5)
goto_remove_passenger_role.pack(pady=20)

remove_passenger_role_frame_title = tk.Label(remove_passenger_role_frame, text="remove_passenger_role()")
remove_passenger_role_frame_title.grid(row=0, column=2)

remove_passenger_role_personID_label = tk.Label(remove_passenger_role_frame, text="personID")
remove_passenger_role_personID_label.grid(row=1, column=0)
remove_passenger_role_personID_entry = tk.Entry(remove_passenger_role_frame)
remove_passenger_role_personID_entry.grid(row=1, column=1)

remove_passenger_role_frame_back_btn = tk.Button(remove_passenger_role_frame, text="Back", command=lambda: people_page.tkraise(), width=15, height=5)
remove_passenger_role_frame_back_btn.grid(row=2, column=1)  

remove_passenger_role_frame_btn = tk.Button(remove_passenger_role_frame, text="Commit", command=lambda: remove_passenger_role_function(
    remove_passenger_role_personID_entry.get()
), width=15, height=5)
remove_passenger_role_frame_btn.grid(row=2, column=2)
########################################################################



people_back_button = tk.Button(people_page, text="Back", command=lambda: front_page.tkraise(), width=15, height=5)
people_back_button.pack(pady=20)
#--------------------------------------------------------------------------------------------------------------------




# Flights -> 5, 10, 11, 16 ------------------------------------------------------------------------------------------------
flights_page_title = Label(flights_page, text='Flights Page')
flights_page_title.pack(pady=20)

######################################################################## offer_flight
goto_offer_flight = tk.Button(flights_page, text="offer_flight()", command=lambda: offer_flight_frame.tkraise(), width=15, height=5)
goto_offer_flight.pack(pady=20)

offer_flight_frame_title = Label(offer_flight_frame, text='offer_flight()')
offer_flight_frame_title.grid(row=0, column=2)

# create labels and entry boxes for airlineID, tail_num, seat_capacity, speed, and location_id
offer_flight_flightID_label = tk.Label(offer_flight_frame, text="flightID")
offer_flight_flightID_label.grid(row=1, column=0)
offer_flight_flightID_entry = tk.Entry(offer_flight_frame)
offer_flight_flightID_entry.grid(row=1, column=1)

offer_flight_routeID_label = tk.Label(offer_flight_frame, text="routeID")
offer_flight_routeID_label.grid(row=2, column=0)
offer_flight_routeID_entry = tk.Entry(offer_flight_frame)
offer_flight_routeID_entry.grid(row=2, column=1)

offer_flight_support_airline_label = tk.Label(offer_flight_frame, text="support_airline")
offer_flight_support_airline_label.grid(row=3, column=0)
offer_flight_support_airline_entry = tk.Entry(offer_flight_frame)
offer_flight_support_airline_entry.grid(row=3, column=1)

offer_flight_support_tail_label = tk.Label(offer_flight_frame, text="support_tail")
offer_flight_support_tail_label.grid(row=4, column=0)
offer_flight_support_tail_entry = tk.Entry(offer_flight_frame)
offer_flight_support_tail_entry.grid(row=4, column=1)

offer_flight_progress_label = tk.Label(offer_flight_frame, text="progress")
offer_flight_progress_label.grid(row=1, column=2)
offer_flight_progress_entry = tk.Entry(offer_flight_frame)
offer_flight_progress_entry.grid(row=1, column=3)

offer_flight_airplane_status_label = tk.Label(offer_flight_frame, text="airplane_status")
offer_flight_airplane_status_label.grid(row=2, column=2)
offer_flight_airplane_status_entry = tk.Entry(offer_flight_frame)
offer_flight_airplane_status_entry.grid(row=2, column=3)

offer_flight_next_time_label = tk.Label(offer_flight_frame, text="next_time")
offer_flight_next_time_label.grid(row=3, column=2)
offer_flight_next_time_entry = tk.Entry(offer_flight_frame)
offer_flight_next_time_entry.grid(row=3, column=3)

offer_flight_back_button = tk.Button(offer_flight_frame, text="Back", command=lambda: flights_page.tkraise(), width=15, height=5)
offer_flight_back_button.grid(row=5, column=1)                                 

offer_flight_frame_btn = tk.Button(offer_flight_frame, text="Commit", command=lambda: offer_flight_function(
    offer_flight_flightID_entry.get(), offer_flight_routeID_entry.get(), offer_flight_support_airline_entry.get(),
    offer_flight_support_tail_entry.get(), offer_flight_progress_entry.get(), offer_flight_airplane_status_entry.get(), 
    offer_flight_next_time_entry.get()
), width=15, height=5)
offer_flight_frame_btn.grid(row=5, column=2)
########################################################################



######################################################################## flight_landing
goto_flight_landing = tk.Button(flights_page, text="flight_landing()", command=lambda: flight_landing_frame.tkraise(), width=15, height=5)
goto_flight_landing.pack(pady=20)

flight_landing_frame_frame_title = tk.Label(flight_landing_frame, text="flight_landing()")
flight_landing_frame_frame_title.grid(row=0, column=2)

flight_landing_flightID_label = tk.Label(flight_landing_frame, text="flightID")
flight_landing_flightID_label.grid(row=1, column=0)
flight_landing_flightID_entry = tk.Entry(flight_landing_frame)
flight_landing_flightID_entry.grid(row=1, column=1)

flight_landing_frame_back_btn = tk.Button(flight_landing_frame, text="Back", command=lambda: flights_page.tkraise(), width=15, height=5)
flight_landing_frame_back_btn.grid(row=2, column=1)  

flight_landing_frame_btn = tk.Button(flight_landing_frame, text="Commit", command=lambda: flight_landing_function(
    flight_landing_flightID_entry.get()
), width=15, height=5)
flight_landing_frame_btn.grid(row=2, column=2)
########################################################################



######################################################################## flight_takeoff
goto_flight_takeoff = tk.Button(flights_page, text="flight_takeoff()", command=lambda: flight_takeoff_frame.tkraise(), width=15, height=5)
goto_flight_takeoff.pack(pady=20)

flight_takeoff_frame_title = tk.Label(flight_takeoff_frame, text="flight_takeoff()")
flight_takeoff_frame_title.grid(row=0, column=2)

flight_takeoff_flightID_label = tk.Label(flight_takeoff_frame, text="flightID")
flight_takeoff_flightID_label.grid(row=1, column=0)
flight_takeoff_flightID_entry = tk.Entry(flight_takeoff_frame)
flight_takeoff_flightID_entry.grid(row=1, column=1)

flight_takeoff_frame_back_btn = tk.Button(flight_takeoff_frame, text="Back", command=lambda: flights_page.tkraise(), width=15, height=5)
flight_takeoff_frame_back_btn.grid(row=2, column=1)  

flight_takeoff_frame_btn = tk.Button(flight_takeoff_frame, text="Commit", command=lambda: flight_takeoff_function(
    flight_takeoff_flightID_entry.get()
), width=15, height=5)
flight_takeoff_frame_btn.grid(row=2, column=2)
########################################################################



######################################################################## retire_flight
goto_retire_flight = tk.Button(flights_page, text="retire_flight()", command=lambda: retire_flight_frame.tkraise(), width=15, height=5)
goto_retire_flight.pack(pady=20)

retire_flight_frame_title = tk.Label(retire_flight_frame, text="flight_takeoff()")
retire_flight_frame_title.grid(row=0, column=2)

retire_flight_flightID_label = tk.Label(retire_flight_frame, text="flightID")
retire_flight_flightID_label.grid(row=1, column=0)
retire_flight_flightID_entry = tk.Entry(retire_flight_frame)
retire_flight_flightID_entry.grid(row=1, column=1)

retire_flight_frame_back_btn = tk.Button(retire_flight_frame, text="Back", command=lambda: flights_page.tkraise(), width=15, height=5)
retire_flight_frame_back_btn.grid(row=2, column=1)  

retire_flight_frame_btn = tk.Button(retire_flight_frame, text="Commit", command=lambda: retire_flight_function(
    retire_flight_flightID_entry.get()
), width=15, height=5)
retire_flight_frame_btn.grid(row=2, column=2)
########################################################################

flights_back_button = tk.Button(flights_page, text="Back", command=lambda: front_page.tkraise(), width=15, height=5)
flights_back_button.pack(pady=20)
# --------------------------------------------------------------------------------------------------------------------------


# Routes -> 7, 8, 9 ------------------------------------------------------------------------------------------------------------
routes_page_title = Label(routes_page, text='Routes Page')
routes_page_title.pack(pady=20)


######################################################################## add_update_leg
goto_add_update_leg = tk.Button(routes_page, text="add_update_leg()", command=lambda: add_update_leg_frame.tkraise(), width=15, height=5)
goto_add_update_leg.pack(pady=20)

add_update_leg_frame_title = tk.Label(add_update_leg_frame, text="add_update_leg()")
add_update_leg_frame_title.grid(row=0, column=2)

add_update_leg_legID_label = tk.Label(add_update_leg_frame, text="legID")
add_update_leg_legID_label.grid(row=1, column=0)
add_update_leg_legID_entry = tk.Entry(add_update_leg_frame)
add_update_leg_legID_entry.grid(row=1, column=1)

add_update_leg_distance_label = tk.Label(add_update_leg_frame, text="distance")
add_update_leg_distance_label.grid(row=2, column=0)
add_update_leg_distance_entry = tk.Entry(add_update_leg_frame)
add_update_leg_distance_entry.grid(row=2, column=1)

add_update_leg_departure_label = tk.Label(add_update_leg_frame, text="departure")
add_update_leg_departure_label.grid(row=1, column=2)
add_update_leg_departure_entry = tk.Entry(add_update_leg_frame)
add_update_leg_departure_entry.grid(row=1, column=3)

add_update_leg_arrival_label = tk.Label(add_update_leg_frame, text="arrival")
add_update_leg_arrival_label.grid(row=2, column=2)
add_update_leg_arrival_entry = tk.Entry(add_update_leg_frame)
add_update_leg_arrival_entry.grid(row=2, column=3)

add_update_leg_frame_back_btn = tk.Button(add_update_leg_frame, text="Back", command=lambda: routes_page.tkraise(), width=15, height=5)
add_update_leg_frame_back_btn.grid(row=3, column=1)  

add_update_leg_frame_btn = tk.Button(add_update_leg_frame, text="Commit", command=lambda: add_update_leg_function(
    add_update_leg_legID_entry.get(), add_update_leg_distance_entry.get(), add_update_leg_departure_entry.get(),
    add_update_leg_arrival_entry.get()
), width=15, height=5)
add_update_leg_frame_btn.grid(row=3, column=2)
########################################################################
 

######################################################################## start_route
goto_start_route = tk.Button(routes_page, text="start_route()", command=lambda: start_route_frame.tkraise(), width=15, height=5)
goto_start_route.pack(pady=20)

start_route_frame_title = tk.Label(start_route_frame, text="start_route()")
start_route_frame_title.grid(row=0, column=2)

start_route_frame_routeID_label = tk.Label(start_route_frame, text="routeID")
start_route_frame_routeID_label.grid(row=1, column=0)
start_route_frame_routeID_entry = tk.Entry(start_route_frame)
start_route_frame_routeID_entry.grid(row=1, column=1)

start_route_frame_legID_label = tk.Label(start_route_frame, text="legID")
start_route_frame_legID_label.grid(row=2, column=0)
start_route_frame_legID_entry = tk.Entry(start_route_frame)
start_route_frame_legID_entry.grid(row=2, column=1)

add_update_leg_frame_back_btn = tk.Button(start_route_frame, text="Back", command=lambda: routes_page.tkraise(), width=15, height=5)
add_update_leg_frame_back_btn.grid(row=3, column=1)  

add_update_leg_frame_btn = tk.Button(start_route_frame, text="Commit", command=lambda:  start_route_function(start_route_frame_routeID_entry.get(), start_route_frame_legID_entry.get()), width=15, height=5)
add_update_leg_frame_btn.grid(row=3, column=2)
########################################################################



######################################################################## extend_route
goto_extend_route = tk.Button(routes_page, text="extend_route()", command=lambda: extend_route_frame.tkraise(), width=15, height=5)
goto_extend_route.pack(pady=20)

extend_route_frame_title = tk.Label(extend_route_frame, text="extend_route()")
extend_route_frame_title.grid(row=0, column=2)

extend_route_frame_routeID_label = tk.Label(extend_route_frame, text="routeID")
extend_route_frame_routeID_label.grid(row=1, column=0)
extend_route_frame_routeID_entry = tk.Entry(extend_route_frame)
extend_route_frame_routeID_entry.grid(row=1, column=1)

extend_route_frame_legID_label = tk.Label(extend_route_frame, text="legID")
extend_route_frame_legID_label.grid(row=2, column=0)
extend_route_frame_legID_entry = tk.Entry(extend_route_frame)
extend_route_frame_legID_entry.grid(row=2, column=1)

extend_route_frame_back_btn = tk.Button(extend_route_frame, text="Back", command=lambda: routes_page.tkraise(), width=15, height=5)
extend_route_frame_back_btn.grid(row=3, column=1)  

extend_route_frame_btn = tk.Button(extend_route_frame, text="Commit", command=lambda: extend_route_function(extend_route_frame_routeID_entry.get(), extend_route_frame_legID_entry.get()), width=15, height=5)
extend_route_frame_btn.grid(row=3, column=2)

########################################################################

routes_back_button = tk.Button(routes_page, text="Back", command=lambda: front_page.tkraise(), width=15, height=5)
routes_back_button.pack(pady=20)
# --------------------------------------------------------------------------------------------------------------------------







# Tickets -> 6 ------------------------------------------------------------------------------------------------------------
tickets_page_title = Label(tickets_page, text='Tickets Page')
tickets_page_title.pack(pady=20)


######################################################################## purchase_ticket_and_seat
goto_purchase_ticket_and_seat = tk.Button(tickets_page, text="purchase_ticket_and_seat()", command=lambda: purchase_ticket_and_seat_frame.tkraise(), width=17, height=5)
goto_purchase_ticket_and_seat.pack(pady=20)

purchase_ticket_and_seat_frame_title = Label(purchase_ticket_and_seat_frame, text='purchase_ticket_and_seat()')
purchase_ticket_and_seat_frame_title.grid(row=0, column=2)

purchase_ticket_and_seat_frame_ticketID_label = tk.Label(purchase_ticket_and_seat_frame, text="ticketID")
purchase_ticket_and_seat_frame_ticketID_label.grid(row=1, column=0)
purchase_ticket_and_seat_frame_ticketID_entry = tk.Entry(purchase_ticket_and_seat_frame)
purchase_ticket_and_seat_frame_ticketID_entry.grid(row=1, column=1)

purchase_ticket_and_seat_frame_cost_label = tk.Label(purchase_ticket_and_seat_frame, text="cost")
purchase_ticket_and_seat_frame_cost_label.grid(row=2, column=0)
purchase_ticket_and_seat_frame_cost_entry = tk.Entry(purchase_ticket_and_seat_frame)
purchase_ticket_and_seat_frame_cost_entry.grid(row=2, column=1)

purchase_ticket_and_seat_frame_carrier_label = tk.Label(purchase_ticket_and_seat_frame, text="carrier")
purchase_ticket_and_seat_frame_carrier_label.grid(row=3, column=0)
purchase_ticket_and_seat_frame_carrier_entry = tk.Entry(purchase_ticket_and_seat_frame)
purchase_ticket_and_seat_frame_carrier_entry.grid(row=3, column=1)

purchase_ticket_and_seat_frame_customer_label = tk.Label(purchase_ticket_and_seat_frame, text="customer")
purchase_ticket_and_seat_frame_customer_label.grid(row=1, column=2)
purchase_ticket_and_seat_frame_customer_entry = tk.Entry(purchase_ticket_and_seat_frame)
purchase_ticket_and_seat_frame_customer_entry.grid(row=1, column=3)

purchase_ticket_and_seat_frame_deplane_at_label = tk.Label(purchase_ticket_and_seat_frame, text="deplane_at")
purchase_ticket_and_seat_frame_deplane_at_label.grid(row=2, column=2)
purchase_ticket_and_seat_frame_deplane_at_entry = tk.Entry(purchase_ticket_and_seat_frame)
purchase_ticket_and_seat_frame_deplane_at_entry.grid(row=2, column=3)

purchase_ticket_and_seat_frame_seat_number_label = tk.Label(purchase_ticket_and_seat_frame, text="seat_number")
purchase_ticket_and_seat_frame_seat_number_label.grid(row=3, column=2)
purchase_ticket_and_seat_frame_seat_number_entry = tk.Entry(purchase_ticket_and_seat_frame)
purchase_ticket_and_seat_frame_seat_number_entry.grid(row=3, column=3)


purchase_ticket_and_seat_frame_back_button = tk.Button(purchase_ticket_and_seat_frame, text="Back", command=lambda: tickets_page.tkraise(), width=15, height=5)
purchase_ticket_and_seat_frame_back_button.grid(row=4, column=1)                                 

purchase_ticket_and_seat_frame_btn = tk.Button(purchase_ticket_and_seat_frame, text="Commit", command=lambda: purchase_ticket_and_seat_function(purchase_ticket_and_seat_frame_ticketID_entry.get(), purchase_ticket_and_seat_frame_cost_entry.get(), purchase_ticket_and_seat_frame_carrier_entry.get(), purchase_ticket_and_seat_frame_customer_entry.get(),purchase_ticket_and_seat_frame_deplane_at_entry.get(), purchase_ticket_and_seat_frame_seat_number_entry.get()), width=15, height=5)
purchase_ticket_and_seat_frame_btn.grid(row=4, column=2)

########################################################################

tickets_back_button = tk.Button(tickets_page, text="Back", command=lambda: front_page.tkraise(), width=17, height=5)
tickets_back_button.pack(pady=20)
# --------------------------------------------------------------------------------------------------------------------------



# Airports -> 2 ------------------------------------------------------------------------------------------------------------
airports_page_title = Label(airports_page, text='Airports Page')
airports_page_title.pack(pady=15)

######################################################################## add_airport
goto_add_airport = tk.Button(airports_page, text="add_airport()", command=lambda: add_airport_frame.tkraise(), width=15, height=5)
goto_add_airport.pack(pady=15)

add_airport_frame_title = Label(add_airport_frame, text='add_airport()')
add_airport_frame_title.grid(row=0, column=2)

add_airport_airportID_label = tk.Label(add_airport_frame, text="airportID")
add_airport_airportID_label.grid(row=1, column=0)
add_airport_airportID_entry = tk.Entry(add_airport_frame)
add_airport_airportID_entry.grid(row=1, column=1)

add_airport_airport_name_label = tk.Label(add_airport_frame, text="airport_name")
add_airport_airport_name_label.grid(row=2, column=0)
add_airport_airport_name_entry = tk.Entry(add_airport_frame)
add_airport_airport_name_entry.grid(row=2, column=1)

add_airport_city_label = tk.Label(add_airport_frame, text="city")
add_airport_city_label.grid(row=3, column=0)
add_airport_city_entry = tk.Entry(add_airport_frame)
add_airport_city_entry.grid(row=3, column=1)

add_airport_state_label = tk.Label(add_airport_frame, text="state")
add_airport_state_label.grid(row=1, column=2)
add_airport_state_entry = tk.Entry(add_airport_frame)
add_airport_state_entry.grid(row=1, column=3)

add_airport_locationID_label = tk.Label(add_airport_frame, text="locationID")
add_airport_locationID_label.grid(row=2, column=2)
add_airport_locationID_entry = tk.Entry(add_airport_frame)
add_airport_locationID_entry.grid(row=2, column=3)

add_airport_frame_back_button = tk.Button(add_airport_frame, text="Back", command=lambda: airports_page.tkraise(), width=15, height=5)
add_airport_frame_back_button.grid(row=4, column=1)                                 

add_airport_frame_btn = tk.Button(add_airport_frame, text="Commit", command=lambda: add_airport_function(add_airport_airportID_entry.get(), add_airport_airport_name_entry.get(), add_airport_city_entry.get(), add_airport_state_entry.get(),add_airport_locationID_entry.get()), width=15, height=5)
add_airport_frame_btn.grid(row=4, column=2)
########################################################################

tickets_back_button = tk.Button(airports_page, text="Back", command=lambda: front_page.tkraise(), width=17, height=5)
tickets_back_button.pack(pady=15)
# --------------------------------------------------------------------------------------------------------------------------


# Views and Simulation Cycle -> 19-25 ------------------------------------------------------------------------------------------
views_simulation_page_title = Label(views_simulation_page, text='Views and Simulation Cycle Page')
views_simulation_page_title.grid(row=0, column=0, columnspan=2, pady=15)

def remove_table_result(table):
    if table is not None:
        table.grid_forget()
    views_simulation_page.tkraise()

######################################################################## flights_in_the_air
goto_flights_in_the_air = tk.Button(views_simulation_page, text="flights_in_the_air()", command=lambda: flights_in_the_air_frame.tkraise(), width=15, height=5)
goto_flights_in_the_air.grid(row=1, column=0, padx=10, pady=10)

flights_in_the_air_result = None

def set_result_flights_in_the_air(frame):
    global flights_in_the_air_result
    flights_in_the_air_result = flights_in_the_air_function(frame)
    flights_in_the_air_result.grid(row=2, column=2, pady=15)


flights_in_the_air_frame_title = Label(flights_in_the_air_frame, text='flights_in_the_air()')
flights_in_the_air_frame_title.grid(row=0, column=2)

flights_in_the_air_frame_back_button = tk.Button(flights_in_the_air_frame, text="Back", command=lambda: remove_table_result(flights_in_the_air_result), width=15, height=5)
flights_in_the_air_frame_back_button.grid(row=1, column=1, pady=15)                                 

flights_in_the_air_frame_btn = tk.Button(flights_in_the_air_frame, text="View", command=lambda: set_result_flights_in_the_air(flights_in_the_air_frame), width=15, height=5)
flights_in_the_air_frame_btn.grid(row=1, column=2, pady=15)
########################################################################


######################################################################## flights_on_the_ground
goto_flights_on_the_ground = tk.Button(views_simulation_page, text="flights_on_the_ground()", command=lambda: flights_on_the_ground_frame.tkraise(), width=15, height=5)
goto_flights_on_the_ground.grid(row=2, column=0, padx=10, pady=10)

flights_on_the_ground_result = None

def set_result_flights_on_the_ground(frame):
    global flights_on_the_ground_result
    flights_on_the_ground_result = flights_on_the_ground_function(frame)
    flights_on_the_ground_result.grid(row=2, column=2, pady=15)

flights_on_the_ground_frame_title = Label(flights_on_the_ground_frame, text='flights_on_the_ground()')
flights_on_the_ground_frame_title.grid(row=0, column=2)

flights_on_the_ground_frame_back_button = tk.Button(flights_on_the_ground_frame, text="Back", command=lambda: remove_table_result(flights_on_the_ground_result), width=15, height=5)
flights_on_the_ground_frame_back_button.grid(row=1, column=1, pady=15)                                 

flights_on_the_ground_frame_btn = tk.Button(flights_on_the_ground_frame, text="View", command=lambda: set_result_flights_on_the_ground(flights_on_the_ground_frame), width=15, height=5)
flights_on_the_ground_frame_btn.grid(row=1, column=2, pady=15)
########################################################################


######################################################################## people_in_the_air
goto_people_in_the_air = tk.Button(views_simulation_page, text="people_in_the_air()", command=lambda: people_in_the_air_frame.tkraise(), width=15, height=5)
goto_people_in_the_air.grid(row=3, column=0, padx=10, pady=10)

people_in_the_air_result = None

def set_result_people_in_air(frame):
    global people_in_the_air_result
    people_in_the_air_result = people_in_the_air_function(frame)
    people_in_the_air_result.grid(row=2, column=2, pady=15)

people_in_the_air_frame_title = Label(people_in_the_air_frame, text='people_in_the_air()')
people_in_the_air_frame_title.grid(row=0, column=2)

people_in_the_air_frame_back_button = tk.Button(people_in_the_air_frame, text="Back", command=lambda: remove_table_result(people_in_the_air_result), width=15, height=5)
people_in_the_air_frame_back_button.grid(row=1, column=1, pady=15)                                 

people_in_the_air_frame_btn = tk.Button(people_in_the_air_frame, text="View", command=lambda: set_result_people_in_air(people_in_the_air_frame), width=15, height=5)
people_in_the_air_frame_btn.grid(row=1, column=2, pady=15)
########################################################################



######################################################################## people_on_the_ground
goto_people_on_the_ground = tk.Button(views_simulation_page, text="people_on_the_ground()", command=lambda: people_on_the_ground_frame.tkraise(), width=15, height=5)
goto_people_on_the_ground.grid(row=4, column=0, padx=10, pady=10)

people_on_the_ground_result = None

def set_result_people_on_the_ground(frame):
    global people_on_the_ground_result
    people_on_the_ground_result = people_on_the_ground_function(frame)
    people_on_the_ground_result.grid(row=2, column=2, pady=15)

people_on_the_ground_frame_title = Label(people_on_the_ground_frame, text='people_on_the_ground()')
people_on_the_ground_frame_title.grid(row=0, column=2)

people_on_the_ground_back_button = tk.Button(people_on_the_ground_frame, text="Back", command=lambda: remove_table_result(people_on_the_ground_result), width=15, height=5)
people_on_the_ground_back_button.grid(row=1, column=1, pady=15)                                 

people_on_the_ground_frame_btn = tk.Button(people_on_the_ground_frame, text="View", command=lambda: set_result_people_on_the_ground(people_on_the_ground_frame), width=15, height=5)
people_on_the_ground_frame_btn.grid(row=1, column=2, pady=15)
########################################################################



######################################################################## route_summary
goto_route_summary = tk.Button(views_simulation_page, text="route_summary()", command=lambda: route_summary_frame.tkraise(), width=15, height=5)
goto_route_summary.grid(row=1, column=1, padx=10, pady=10)

route_summary_result = None

def set_result_route_summary(frame):
    global route_summary_result
    route_summary_result = route_summary_function(frame)
    route_summary_result.grid(row=2, column=2, pady=15)

route_summary_frame_title = Label(route_summary_frame, text='route_summary()')
route_summary_frame_title.grid(row=0, column=2)

route_summary_back_button = tk.Button(route_summary_frame, text="Back", command=lambda: remove_table_result(route_summary_result), width=15, height=5)
route_summary_back_button.grid(row=1, column=1, pady=15)                                 

route_summary_frame_btn = tk.Button(route_summary_frame, text="View", command=lambda: set_result_route_summary(route_summary_frame), width=15, height=5)
route_summary_frame_btn.grid(row=1, column=2, pady=15)





########################################################################



######################################################################## alternative_airports
goto_alternative_airports = tk.Button(views_simulation_page, text="alternative_airports()", command=lambda: alternative_airports_frame.tkraise(), width=15, height=5)
goto_alternative_airports.grid(row=2, column=1, padx=10, pady=10)


alternative_airports_result = None

def set_result_route_summary(frame):
    global alternative_airports_result
    alternative_airports_result = alternative_airports_function(frame)
    alternative_airports_result.grid(row=2, column=2, pady=15)

alternative_airports_frame_title = Label(alternative_airports_frame, text='alternative_airports()')
alternative_airports_frame_title.grid(row=0, column=2)

alternative_airports_back_button = tk.Button(alternative_airports_frame, text="Back", command=lambda: remove_table_result(alternative_airports_result), width=15, height=5)
alternative_airports_back_button.grid(row=1, column=1, pady=15)                                 

alternative_airports_frame_btn = tk.Button(alternative_airports_frame, text="View", command=lambda: set_result_route_summary(alternative_airports_frame), width=15, height=5)
alternative_airports_frame_btn.grid(row=1, column=2, pady=15)
########################################################################



######################################################################## simulation_cycle
goto_simulation_cycle = tk.Button(views_simulation_page, text="simulation_cycle()", command=lambda: simulation_cycle_frame.tkraise(), width=15, height=5)
goto_simulation_cycle.grid(row=3, column=1, padx=10, pady=10)

simulation_cycle_frame_title = Label(simulation_cycle_frame, text='simulation_cycle()')
simulation_cycle_frame_title.grid(row=0, column=2)

simulation_cycle_frame_back_button = tk.Button(simulation_cycle_frame, text="Back", command=lambda: views_simulation_page.tkraise(), width=15, height=5)
simulation_cycle_frame_back_button.grid(row=1, column=1)                                 

simulation_cycle_frame_btn = tk.Button(simulation_cycle_frame, text="Commit", command=lambda: simulation_cycle_function(), width=15, height=5)
simulation_cycle_frame_btn.grid(row=1, column=2)




########################################################################



views_simulation_back_button = tk.Button(views_simulation_page, text="Back", command=lambda: front_page.tkraise(), width=15, height=5)
views_simulation_back_button.grid(row=5, column=1, columnspan=2, pady=15)
# --------------------------------------------------------------------------------------------------------------------------


#Start with front page 
front_page.tkraise()

# Configure row and column weights to make the buttons expand to fill the window
window.rowconfigure([0,1,2,3], weight=1)
window.columnconfigure([0,1], weight=1)

window.mainloop()
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
add_airplane_frame = Frame(window) 
add_airplane_frame.grid(row=0, column=0, sticky="nsew")



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


airplane_page_title = Label(airplane_page, text='Airplanes Page')
airplane_page_title.pack(pady=20)
goto_add_airplane = tk.Button(airplane_page, text="add_airplane()", command=lambda: add_airplane_frame.tkraise(), width=30, height=10)
goto_add_airplane.pack()
airplane_back_button = tk.Button(airplane_page, text="Back", command=lambda: front_page.tkraise(), width=30, height=10)
airplane_back_button.pack()


add_airplane_title = Label(add_airplane_frame, text='add_airplane()')
add_airplane_title.grid(row=0, column=2)

# create labels and entry boxes for airlineID, tail_num, seat_capacity, speed, and location_id
airlineID_label = tk.Label(add_airplane_frame, text="airlineID")
airlineID_label.grid(row=1, column=0)

airlineID_entry = tk.Entry(add_airplane_frame)
airlineID_entry.grid(row=1, column=1)

tail_num_label = tk.Label(add_airplane_frame, text="tail_num")
tail_num_label.grid(row=2, column=0)

tail_num_entry = tk.Entry(add_airplane_frame)
tail_num_entry.grid(row=2, column=1)

seat_capacity_label = tk.Label(add_airplane_frame, text="seat_capacity")
seat_capacity_label.grid(row=3, column=0)
seat_capacity_entry = tk.Entry(add_airplane_frame)
seat_capacity_entry.grid(row=3, column=1)

speed_label = tk.Label(add_airplane_frame, text="speed")
speed_label.grid(row=4, column=0)
speed_entry = tk.Entry(add_airplane_frame)
speed_entry.grid(row=4, column=1)

location_id_label = tk.Label(add_airplane_frame, text="location_id")
location_id_label.grid(row=5, column=0)
location_id_entry = tk.Entry(add_airplane_frame)
location_id_entry.grid(row=5, column=1)

# create labels and entry boxes for skids, plane_type, propeller, and jet_engines
skids_label = tk.Label(add_airplane_frame, text="skids")
skids_label.grid(row=1, column=2)
skids_entry = tk.Entry(add_airplane_frame)
skids_entry.grid(row=1, column=3)

plane_type_label = tk.Label(add_airplane_frame, text="plane_type")
plane_type_label.grid(row=2, column=2)
plane_type_entry = tk.Entry(add_airplane_frame)
plane_type_entry.grid(row=2, column=3)

propeller_label = tk.Label(add_airplane_frame, text="propeller")
propeller_label.grid(row=3, column=2)
propeller_entry = tk.Entry(add_airplane_frame)
propeller_entry.grid(row=3, column=3)

jet_engines_label = tk.Label(add_airplane_frame, text="jet_engines")
jet_engines_label.grid(row=4, column=2)
jet_engines_entry = tk.Entry(add_airplane_frame)
jet_engines_entry.grid(row=4, column=3)

add_airplane_back_button = tk.Button(add_airplane_frame, text="Back", command=lambda: airplane_page.tkraise(), width=15, height=5)
add_airplane_back_button.grid(row=6, column=1)                                 

add_airplane_btn = tk.Button(add_airplane_frame, text="Add", command=lambda: add_airplane_function(
    airlineID_entry.get(), tail_num_entry.get(), seat_capacity_entry.get(), speed_entry.get(),
    location_id_entry.get(), plane_type_entry.get(), skids_entry.get(), propeller_entry.get(), 
    jet_engines_entry.get()), width=15, height=5)
add_airplane_btn.grid(row=6, column=2)


# Airplane -> 1
# People -> 3, 12?, 13?, 17
# Pilot -> 4, 14, 15, 18
# Flights -> 5, 10, 11, 16
# Routes -> 7, 8, 9
# Tickets -> 6
# Airports -> 2
# Views and Simulation Cycle -> 19-25


#Start with front page 
front_page.tkraise()

# Configure row and column weights to make the buttons expand to fill the window
window.rowconfigure([0,1,2,3], weight=1)
window.columnconfigure([0,1], weight=1)

window.mainloop()

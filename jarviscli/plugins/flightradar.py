from plugin import plugin, require
from FlightRadar24.api import FlightRadar24API
flightapi = FlightRadar24API()

branch_coverage = {}

def track_branch(branch_id):
    branch_coverage[branch_id] = branch_coverage.get(branch_id, 0) + 1

def write_coverage():
    with open("branch_coverage.log", "w") as f:
        for branch, count in branch_coverage.items():
            f.write(f"Branch {branch}: {count} hits\n")

@require(network=True)
@plugin("flightradar")
def flightradar(jarvis, s):
    flightapi = FlightRadar24API()

    airports = flightapi.get_airports()
    airlines = flightapi.get_airlines()
    flights = flightapi.get_flights()

    option = int(input("What do you want to do:\n  1) Check Airline flights\n  2) Check Flight between Destinations\n 3) Track flight\nPlease chose between(1, 2, 3): "))

    if option == 1:
        track_branch(1)
        get_input_method = int(input("How will you give the name of the airline:\n  1) By icao\n  2) By airline name\nPlease chose between(1, 2): "))
        if get_input_method == 1:
            track_branch(2)
            airline_icao = input("What is the airlines icao: ")
            if airline_icao != "":
                track_branch(3)
                airline_planes = flightapi.get_flights(airline = airline_icao.upper())
                airline_flights = []
                for plane in airline_planes:
                    track_branch(4)
                    if plane.altitude != 0:
                        track_branch(5)
                        airline_flights.append(plane)
                jarvis.say("{:^5} {:^10} {:^20} {:^22} {:^10}   {:^10} {:^10} ".format("ICAO", "Registration", "Origin Airport", "Destination Airport", "latitude", "longitude", "time"))
                for flight in airline_flights:
                    track_branch(6)
                    jarvis.say("{:^5} {:^10}   {:^20} {:^22} {:^10}   {:^10}  {:^10}".format(flight.airline_icao, flight.registration, flight.origin_airport_iata, flight.destination_airport_iata, flight.latitude, flight.longitude, flight.time))
            else:
                track_branch(7)
                jarvis.say("Enter a ICAO")
        
        elif get_input_method == 2:
            track_branch(8)
            airline_name = input("What is the airlines Name: ")
            if airline_name == "":
                track_branch(9)
                jarvis.say("Enter a Airline name")
            run = False
            for airline in airlines:
                track_branch(10)
                if airline["Name"].lower() == airline_name.lower():
                    track_branch(11)
                    airline_icao = airline["ICAO"]
                    run = True
                    break
            if run:
                track_branch(12)
                airline_planes = flightapi.get_flights(airline = airline_icao)
                airline_flights = []
                for plane in airline_planes:
                    track_branch(13)
                    if plane.altitude != 0:
                        track_branch(14)
                        airline_flights.append(plane)
                jarvis.say("  {:^5}   {:^5} {:^10} {:^20} {:^22} {:^10}   {:^10} {:^10}".format("Name","ICAO", "Registration", "Origin Airport", "Destination Airport", "latitude", "longitude", "time"))
                for flight in airline_flights:
                    track_branch(15)
                    jarvis.say("{:^5}  {:^5} {:^10}   {:^20} {:^22} {:^10}   {:^10}  {:^10}".format(airline_name, flight.airline_icao, flight.registration, flight.origin_airport_iata, flight.destination_airport_iata, flight.latitude, flight.longitude, flight.time))
            else:
                track_branch(16)
                jarvis.say("No airline found")
        else:
            track_branch(17)
            jarvis.say("Enter a vaild option")

    elif option == 2:
        track_branch(18)
        get_input_method = int(input("How will you give the name of the airports:\n  1) By iata\n  2) By airport name\nPlease chose between(1, 2): "))
        if get_input_method == 1:
            track_branch(19)
            origin_airport_iata = input("What is the origin airport iata: ")
            destination_airport_iata = input("What is the destination airport iata: ")\
            
            if origin_airport_iata != destination_airport_iata:
                track_branch(20)
                route_flights = []
                for plane in flights:
                    track_branch(21)
                    if (plane.origin_airport_iata == origin_airport_iata) and (plane.destination_airport_iata == destination_airport_iata):
                        track_branch(22)
                        route_flights.append(plane)
                jarvis.say("{:^5} {:^10} {:^20} {:^22} {:^10}   {:^10} {:^10}".format("ICAO", "Registration", "Origin Airport", "Destination Airport", "latitude", "longitude", "time"))
                for flight in route_flights:
                    track_branch(23)
                    jarvis.say("{:^5} {:^10}   {:^20} {:^22} {:^10}   {:^10}  {:^10}".format(flight.airline_icao, flight.registration, flight.origin_airport_iata, flight.destination_airport_iata, flight.latitude, flight.longitude, flight.time))
        
        
        elif get_input_method == 2:
            track_branch(24)
            origin_airport_name = input("What is the origin airport name: ")
            destination_airport_name = input("What is the destination airport name: ")

            if origin_airport_name != destination_airport_name:
                track_branch(25)
                run = False
                orun = False
                drun = False
                for airport in airports:
                    track_branch(26)
                    if airport["name"].lower() == origin_airport_name.lower():
                        track_branch(27)
                        origin_airport_iata = airport["iata"]
                        orun = True
                    elif airport["name"].lower() == destination_airport_name.lower():
                        track_branch(28)
                        destination_airport_iata = airport["iata"]
                        drun = True
                    if orun and drun:
                        track_branch(29)
                        run = True
                        break
                if run:
                    track_branch(30)
                    jarvis.say(destination_airport_iata, origin_airport_iata)

                    route_flights = []
                    for plane in flights:
                        track_branch(31)
                        if (plane.origin_airport_iata == origin_airport_iata) and (plane.destination_airport_iata == destination_airport_iata):
                            track_branch(32)
                            route_flights.append(plane)
                    jarvis.say("{:^5} {:^10} {:^20} {:^22} {:^10}   {:^10} {:^10}".format("ICAO", "Registration", "Origin Airport", "Destination Airport", "latitude", "longitude", "time"))
                    for flight in route_flights:
                        track_branch(33)
                        jarvis.say("{:^5} {:^10}   {:^20} {:^22} {:^10}   {:^10}  {:^10}".format(flight.airline_icao, flight.registration, flight.origin_airport_iata, flight.destination_airport_iata, flight.latitude, flight.longitude, flight.time))
                else:
                    track_branch(34)
                    if not orun and not drun:
                        track_branch(35)
                        jarvis.say("Neither origin and destination airports were found")
                    elif not orun:
                        track_branch(36)
                        jarvis.say("The origin airport wasn't found")
                    elif not drun:
                        track_branch(37)
                        jarvis.say("The destination airport wasn't found")
        else:
            track_branch(38)
            jarvis.say("Enter a vaild option")

    elif option == 3:
        track_branch(39)
        flight_resgitration = input("What is the airplane resgistration: ")
        
        for flight in flights:
            track_branch(40)
            if flight.registration == flight_resgitration:
                track_branch(41)
                jarvis.say("{:^5} {:^10} {:^20} {:^22} {:^10}   {:^10} {:^10}".format("ICAO", "Registration", "Origin Airport", "Destination Airport", "latitude", "longitude", "time"))
                jarvis.say("{:^5} {:^10}   {:^20} {:^22} {:^10}   {:^10}  {:^10}".format(flight.airline_icao, flight.registration, flight.origin_airport_iata, flight.destination_airport_iata, flight.latitude, flight.longitude, flight.time))
                break

    else:
        track_branch(42)
        jarvis.say("Enter a vaild option")

import atexit
atexit.register(write_coverage)
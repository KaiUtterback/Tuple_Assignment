''' 1: Tuple Mastery In Python
Objective:
The aim of this assignment is to deepen your understanding of tuples in Python, along with their interaction 
with lists, dictionaries, and basic Python functionalities like functions, input handling, adn string formatting.
By completing this assignment, you will enhance your skills in data structuring, manipulation, and application of tuples in practical scenarios.

Task 1: Formatting Flight Itineraries
    Create a Python function that takes a list of tuples as an argument. 
    Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
    The function should format and return a string that lists each itinerary.
    For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")] 
    
    The output should be formatted as:

        "Itinerary 1: Alice - From New York to London
        Itinerary 2: Bob - From Tokyo to San Francisco"    

'''

def display_flight_information():
    flight_information = traveler, destination_1, destination_2
    traveler = input("Enter the Traveler's name: ")
    destination_1 = input("Enter where you will be flying from: ")
    destination_2 = input("Enter the destination you are flying to: ")
    print(flight_information)

display_flight_information()
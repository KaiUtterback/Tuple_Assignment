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
print()

def format_flight_itineraries(flights):
    formatted_itineraries = []
    for i, itinerary in enumerate(flights, start=1):
        traveler_name, origin, destination = itinerary
        formatted_itinerary = f"Itinerary {i}: {traveler_name} - From {origin} to {destination}"
        formatted_itineraries.append(formatted_itinerary)
    return '\n'.join(formatted_itineraries)

flights = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted_flights = format_flight_itineraries(flights)
print(formatted_flights)
print()


''' 2: Python Data Structure Challenges in Real-World Scenarios

Objective:
    This assignment is designed to enhance your understanding adn application of Python's core data structures -tuples, lists, and dictionaries
    in real world contexts. By engaging with these tasks, you will practice manipulating these data structures, applying built in python methods, and implementing error
    handling in practical situations.

Task 1: Library System Enhancement
    Sharpen your skills in managing and modifying data within tuples and lists.

Problem Statement:
    You are maintaining a library system where each book is stored as a tuple within a list.
    Your task is to update this system by adding books and ensuring no duplicates.

Existing Library Data:
    library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley)]

    - Add Functionality to insert new books into library 
    - Ensure that adding a duplicate book is handled appropriately.

'''


def add_book(library):
    title = input("Enter the book's Title: ")
    author = input("Enter the book's Author: ")
    genre = input("Enter the book's Genre: ")
    for book in library:
        book = title, author, genre
        if book not in library:
            library.append((book))
        else:
            print("Book already in library, please add a new entry")



def display_library(library):
    for book in library:
        title, author, genre = book
        print(f"\nTitle: {title}")
        print(f"Author: {author}")
        print(f"Genre: {genre}")



def run_library():
    library = [
        ("To Kill a Mockingbord", "Harper Lee", "Classic"),
        ("1984", "George Orwell", "Dystopian"),
        ("The Great Gatsby", "F. Scott Fitzgerald", "Classic"),
        ("Brave New World", "Aldous Huxly", "Dystopian")
    ]

    while True:
        print("\n1. Add a book to your Library")
        print("2. Display Library")
        print("3. Exit")
        choice = input("Enter your selection here: ")

        if choice == '1':
            add_book(library)
        elif choice == '2': 
            display_library(library)
        elif choice == '3':
            break
        else:
            print("Incorrect selection")
        
# run_library()

''' 3. Python Loops and Tuples in Analytical Applications
Objective:
    This assignment is designed to strengthen your expertise in using Python loops and Tuples, particularly in data analysis and processing scenarios.
    By completing these tasks,  you will gain practical experience in handling and analyzing data using these fundamental Python concepts.

Task 1: Stock Market Data Analysis:
    Enhance your skills in data manipulation and analysis using tuples and loops

Problem Statement:
    You have been provided with stock market data, where each data point is a tuple containing a company's stock symbol, the date, and the closing price.
    Your task is to analyze this data to find the average closing price of a specified stock over a given period.

Sample Data:
    stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]

    - Create a function to caclulate the average closing price of a specific symbol over all dates.
    - Ensure your solution handles cases where the stock symbol does not exist in the data.
'''



def aapl_average(stock_data):
    total_price = 0
    count = 0
    for data in stock_data:
        symbol, date, price = data
        if symbol == "AAPL":
            price = float(price)
            total_price += price
            count += 1
    if count > 0:
        average_price = total_price / count
        print(f"The average closing cost of AAPL is ${average_price:.2f}")
    else:
        print("No AAPL data found.")

def msft_average(stock_data):
    total_price = 0
    count = 0
    for data in stock_data:
        symbol, date, price = data
        if symbol == "MSFT":
            price = float(price)
            total_price += price
            count += 1
    if count > 0:
        average_price = total_price / count
        print(f"The average closing cost of MSFT is ${average_price:.2f}")
    else:
        print("No MSFT data found.")


def stock_program():
    stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]
    while True:
        print("\nWelcome to the Stock Identifier!")
        print("Enter a stock symbol to find the average closing cost\nor type exit to exit:")
        option = input("Enter Selection: ")
        option = option.lower()

        if option == "exit":
            break
        elif option == "aapl":
            aapl_average(stock_data)
        elif option == "msft":
            msft_average(stock_data)
        else:
            print("That's not a correct entry, please try again")

#stock_program()
            
''' TASK 2: Event Attendance Tracker
Apply Loops and tuples to track and report on event attendance.

Problem Statement:
    Your goal is to manage an attendance system for various events. 
    Each atendee's data is stored as a tuple containing their name and the event they attended.

    - Develop a function to list all atendees of a specific event
    - Implement a feature to count the number of atendees for each event

Example Attendee Data:
    attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
    # More attendees...
]

'''

attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
    # More attendees...
]

def list_attendees(attendees):
    for person, event in attendees:
        print(f"{person} is attending the {event}")

def count_event(attendees):
    event_counts = {}
    
    for _, event in attendees:
        event_counts[event] = sum(1 for _, e in attendees if e == event)
    
    for event, count in event_counts.items():
        print(f"\n{count} attended the {event}")



def run_event_data():
    list_attendees(attendees)
    count_event(attendees)

#run_event_data()
    
'''4. Mastering Tuple Packing and Unpacking in Python
Objective:
    The goal of this assignment is to deepen your understanding of tuple packing and unpacking in Python.
    You will apply these techniques in various practical scenarios, enhancing your ability to work with 
    flexible data structures and improve data handling efficiency.

Task 1: Customer Order Processing
    Refine your skills in tuple unpacking by managing customer orders.

Problem Statements:
    You are given a list of tuples, each representing a customer's order. 
    Each tuple contains the customer's name, the product ordered, and the quntity.
    Your task is to unpack each tuple and print the order details in a user-friendly format.

Sample Order Data:
    orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More Orders...
    ]

    - Write a function to iterate over the list of orders.
    - Unpack each tuple in the list and format the details for display.    

'''

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More Orders...
    ]

def display_orders(orders):
    for order in orders:
        name, product, quantity = order
        print(f"{name} purchased {quantity} {product}(s)")

display_orders(orders)
print()

''' Task 2: Sorting and Filtering Contact Information
Implement tuple packing and unpacking in sorting and filtering tasks.

Problem Statement:
    You have a list of contacts, where each contact is represented as a tuple containing a name, email, and phone number. 
    Your task is to:

    - Sort the Contacts by name
    - Filter and display contacts whose name start with a specific letter

Sample Data:

contacts = [
    ("Alice", "alice@email.com", "123-456-7890"),
    ("Bob", "bob@email.com", "234-567-8901"),
    # More contacts...
]

'''

contacts = [
    ("Alice", "alice@email.com", "123-456-7890"),
    ("Bob", "bob@email.com", "234-567-8901"),
    # More contacts...
]

sorted_contacts = sorted(contacts)

specific_letter = 'A'  
filtered_contacts = [contact for contact in sorted_contacts if contact[0].startswith(specific_letter)]

for contact in filtered_contacts:
    print(contact)
print()

'''5. Advanced Tuple Techniques: Joining and Nesting in Python
Objective:
    This assignment is designed to advance your understanding and application of joining and nesting tupleds in Python.
    You will engage in tasks that require organizing and manipulating complex data structures, improving your problem-solving skills
    in handling multi_dimensional data.

Task 1: Product Catalog Merging
    Utilize tuple joining to combine multiple product catalogs.

Problem Statement:
    You are managing the poroduct catalogs for an online store.
    Each catalog is a tuple of products, and each product is a tuple containing the product name and price.
    Merge multiple catalogs into a single tuple.

    - Write a funciton to join two or more product catalogs into one.
    - Display the combined catalog, ensuring that it maintains the order of products as they were in their original catalogs.

Example Catalogs:

catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))

'''

catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))

def catalog_combiner():
    combined_catalog = catalog1 + catalog2
    for item, price in combined_catalog:
        print(f"The {item} is ${price}")

catalog_combiner()
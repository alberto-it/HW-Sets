"""
1. Python Sets Adventure
Task 1: Flight Route Comparison
Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. 
You have two sets of flight destinations, one for each airline. Write a Python program to find out:

Destinations that both airlines fly to.
Destinations unique to your airline.
Whether there are any destinations that neither airline shares.
Example Code:
"""
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

both = our_routes.intersection(competitor_routes)
print("\nAirports both airlines fly to:", both)

unique = our_routes.difference(competitor_routes)
print("Airports unique to our airline:", unique)

neither_airline = our_routes.symmetric_difference(competitor_routes)
print("Airports neither airline shares:", neither_airline, "\n")

"""
2. Set Operations in Data Analysis
Task 1: Duplicate Entries Cleanup
You are given a list of customer IDs, some of which are duplicated.
Write a Python script to remove duplicates and display the unique customer IDs.

Example Code:
"""
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
"""
Expected Outcome:
A set of unique customer IDs, ensuring no duplicates. For instance, {'C001', 'C002', 'C003', 'C004'}.
"""
print("Unique customer IDs:", sorted(set(customer_ids)), "\n")
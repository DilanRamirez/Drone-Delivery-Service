"""
CS 2302 - Data Structures
Instructor: Dr. Olac Fuentes
TA: Ismael Villanueva-Miranda
Laboratory 5 - Search Algorithms
Author: Dilan Ramirez
Description:
    A company wants to establish a drone service to deliver packages from city to city. Your task is to implement
    algorithms to help them plan the set of flights that will be needed to make sure packages can be delivered from
    every city to every other city they serve while minimizing flight distances. The file cities.xlsx contains the names
    of the cities to be served and the flight distance from each pair of cities from which it is feasible to fly a drone; if
    flying a drone between two cities is not feasible, the distance appears as -1. For example, the ”drone distance”
    from El Paso to Austin is 851, from Dallas to Las Vegas it’s 1700, and it is not feasible to fly a drone from
    Laredo to San Antonio
Last Modification: Jul 30, 2019
Lab Report Link: https://drive.google.com/open?id=1XIbAf2tEQ3WEIRN2_8_agIGFESvgZEO4
"""

def CityNames(path):
    cityNames = [] # a new list is created to store all the names of the cities according to their number
    for i in path:
        if i == -1:
            cityNames.append("EL Paso")
        if i == 0:
            cityNames.append("EL Paso")
        if i == 1:
            cityNames.append("San Antonio")
        if i == 2:
            cityNames.append("Houston")
        if i == 3:
            cityNames.append("Amarillo")
        if i == 4:
            cityNames.append("Dallas")
        if i == 5:
            cityNames.append("Austin")
        if i == 6:
            cityNames.append("Jackson")
        if i == 7:
            cityNames.append("Laredo")
        if i == 8:
            cityNames.append("Tulsa")
        if i == 9:
            cityNames.append("Lubbock")
        if i == 10:
            cityNames.append("Las Vegas")
        if i == 11:
            cityNames.append("Midland")
        if i == 12:
            cityNames.append("McAllen")
        if i == 13:
            cityNames.append("Denver")
        if i == 14:
            cityNames.append("Albuquerque")
        if i == 15:
            cityNames.append("Los Angeles")
        if i == 16:
            cityNames.append("Oklahoma City")
        if i == 17:
            cityNames.append("Phoenix")
        if i == 18:
            cityNames.append("New Orleans")
        if i == 19:
            cityNames.append("Wichita")
    return cityNames
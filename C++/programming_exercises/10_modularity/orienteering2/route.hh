/*
#############################################################################
# COMP.CS.110 Ohjelmointi 2: Rakenteet / Programming 2: Structures          #
# Project3: Suunnistus / Orienteering                                       #
# File: route.hh                                                            #
#                                                                           #
# Code written by                                                           #
# Name: Iiro Inkinen                                                        #
# Student number: 50393673                                                  #
# Username: vbiiin                                                          #
# Git: https://course-gitlab.tuni.fi/comp.cs.110-ohj-2_2022-KEVAT/vbiiin    #
# E-Mail: iiro.inkinen@tuni.fi                                              #
#                                                                           #
# Description: Class for a single route in orienteering map.                #
# Notes:                                                                    #
#############################################################################
*/

#ifndef ROUTE_HH
#define ROUTE_HH

#include "point.hh"
#include <iostream>
#include <cmath>
#include <iomanip>

// Linked list for points in one route.
struct Route_points {
    Point* point;
    Route_points* next;
};

class Route
{
public:
    // Constructor and destructor.
    // "name" = name of the route.
    // "first_point" = first point on the route.
    Route(std::string name, Point* first_point);
    ~Route();

    // Adds point "to" as the next point in the route.
    void addPoint(Point* to);

    // Prints all points in a route.
    void print();

    // Calculates and prints the length of the route.
    void calculate_length();

    // Calculates the highest continuous rise on any route after "start_point".
    // Returns the rise in meters.
    uint rise(Point* start_point);

private:
    // Route name and pointers to first and last point on the route.
    std::string name_;
    Route_points* first_;
    Route_points* last_;

    // Recursive function to determine where the rise ends. Used by method rise.
    uint recursiveRise(Route_points* start);
};


#endif // ROUTE_HH

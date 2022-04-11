/*
#############################################################################
# COMP.CS.110 Ohjelmointi 2: Rakenteet / Programming 2: Structures          #
# Project3: Suunnistus / Orienteering                                       #
# File: point.hh                                                            #
#                                                                           #
# Code written by                                                           #
# Name: Iiro Inkinen                                                        #
# Student number: 50393673                                                  #
# Username: vbiiin                                                          #
# Git: https://course-gitlab.tuni.fi/comp.cs.110-ohj-2_2022-KEVAT/vbiiin    #
# E-Mail: iiro.inkinen@tuni.fi                                              #
#                                                                           #
# Description: Class for a single point in orienteering map.                #
# Notes: * In this state the class could have been implemented as a struct  #
#          inside the class Routes.                                         #
#############################################################################
*/
#ifndef POINT_HH
#define POINT_HH
#include <iostream>

class Point
{
public:
    // Constructor and destructor.
    // "name" = name of the point
    // "x-coord = the x-coordinate of the point in the map
    // "y-coord = the y-coordinate of the point in the map
    // "height" = the height of the point in the map
    // "marker" = one char marker for the point
    Point(std::string name, unsigned int x_coord, unsigned int y_coord,
          unsigned int height, char marker);
    ~Point();

    // Returns the one character marker for the point.
    char getMarker();

    // Return the name of the point.
    std::string getName();

    // Returns the coordinates of the point via parameters (x,y).
    void getCoordinates(float& x, float& y);

    // Returns the height of the point.
    uint getHeight();

private:
    std::string name_;
    unsigned int x_;
    unsigned int y_;
    unsigned int height_;
    char marker_;
};

#endif // POINT_HH

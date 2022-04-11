#include "point.hh"
#include <iostream>

Point::Point(std::string name, unsigned int x_coord, unsigned int y_coord,
             unsigned int height, char marker): name_(name), x_(x_coord),
             y_(y_coord), height_(height), marker_(marker) {
}

Point::~Point()
{

}

char Point::getMarker()
{
    return marker_;
}

std::string Point::getName()
{
    return name_;
}

void Point::getCoordinates(float& x, float& y)
{
    x = x_;
    y = y_;
}

uint Point::getHeight()
{
    return height_;
}

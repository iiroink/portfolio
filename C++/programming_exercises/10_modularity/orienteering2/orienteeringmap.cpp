#include "orienteeringmap.hh"
#include <iostream>

OrienteeringMap::OrienteeringMap(): map_width_(0), map_height_(0),
    points_by_coord_({{}}), points_by_name_({})
{

}

OrienteeringMap::~OrienteeringMap()
{
    // Free all points from memory.
    for (unsigned int row = 1; row <= map_height_; ++row) {
        for (unsigned int column = 1; column <= map_width_; ++column) {
            Point* tmp_ptr = points_by_coord_.at(row).at(column);
            if (tmp_ptr) {
                delete tmp_ptr;
                tmp_ptr = nullptr;
            }
        }
    }
    // Free all routes from memory.
    for (auto route : routes_) {
        delete route.second;
        route.second = nullptr;
    }
    routes_.clear();
}

void OrienteeringMap::set_map_size(int width, int height)
{
    // Save the width and height values.
    map_width_ = width;
    map_height_ = height;
    // Initialize a map-size matrix with pointers, where points will be saved.
    for (unsigned int row = 1; row <= map_height_; ++row) {
        for (unsigned int column = 1; column <= map_width_; ++column) {
            points_by_coord_.insert({row, {}});
            points_by_coord_.at(row).insert({column, nullptr});
        }
    }
}

void OrienteeringMap::add_point(std::string name, int x, int y, int height,
                                char marker)
{
    Point* tmp_ptr = new Point(name, x, y, height, marker);
    // Save the new point with its coordinates.
    points_by_coord_.at(y).at(x) = tmp_ptr;
    // Save the new points with its name.
    if (points_by_name_.find(name) == points_by_name_.end()) {
        points_by_name_.insert({name, nullptr});
    }
    points_by_name_.at(name) = tmp_ptr;
}

bool OrienteeringMap::connect_route(std::string from, std::string to,
                                    std::string route_name)
{
    Point* point = points_by_name_.at(from);
    // Add a new route
    if (routes_.find(route_name) == routes_.end()) {
        routes_.insert({route_name, nullptr});
        routes_.at(route_name) = new Route(route_name, point);
    }
    // Add a point to an existing route
    routes_.at(route_name)->addPoint(points_by_name_.at(to));
    return true;
}

void OrienteeringMap::print_map() const
{
    // Column numbers on top.
    std::cout << "  ";
    for (unsigned int number = 1; number <= map_width_; ++number) {
        std::cout.width(2);
        std::cout << number << " ";
    }
    // Row numbers and map.
    std::cout << std::endl;
    for (unsigned int row = 1; row <= map_height_; ++row) {
        std::cout.width(2);
        std::cout << row;
        for (unsigned int column = 1; column <= map_width_; ++column) {
            std::cout << "  ";
            // If there is a point in the square, print its marker.
            if (points_by_coord_.at(row).at(column)) {
                std::cout << points_by_coord_.at(row).at(column)->getMarker();
            // Otherwise print symbol for empty square.
            } else {
                std::cout << ".";
            }
        }
        std::cout << std::endl;
    }
}

void OrienteeringMap::print_routes() const
{
    std::cout << "Routes:" << std::endl;
    for (auto& route : routes_) {
        std::cout << " - " << route.first << std::endl;
    }
}

void OrienteeringMap::print_points() const
{
    std::cout << "Points:" << std::endl;
    for (auto& point : points_by_name_) {
        std::cout << " - " << point.first << " : " << point.second->getMarker()
                  << std::endl;
    }
}

void OrienteeringMap::print_route(const std::string &name) const
{
    // Checks if route with the name exists.
    if (routes_.find(name) == routes_.end()) {
        std::cout << "Error: Route named " << name << " can't be found"
                  << std::endl;
    } else {
        // Class Route handles the printing.
        routes_.at(name)->print();
    }
}

void OrienteeringMap::route_length(const std::string &name) const
{
    // Checks if route with the name exists.
    if (routes_.find(name) == routes_.end()) {
        std::cout << "Error: Route named " << name << " can't be found"
                  << std::endl;
    } else {
        // Class Route handles the calculation and printing.
        routes_.at(name)->calculate_length();
    }
}

void OrienteeringMap::greatest_rise(const std::string &point_name) const
{
    // Checks if point with the name exists.
    if (points_by_name_.find(point_name) == points_by_name_.end()) {
        std::cout << "Error: Point named " << point_name << " can't be found"
                  << std::endl;
    } else {
        uint rise = 0;
        // List for the routes with the greatest rise.
        std::vector< std::string > rising_routes = {};
        Point* point = points_by_name_.at(point_name);
        for (auto& route : routes_) {
            // Finds the highest rise for "point" on "route".
            uint found_rise = route.second->rise(point);
            // Adds another route with the same rise to the list.
            if (0 < found_rise && rise == found_rise) {
                rising_routes.push_back(route.first);
            // Replaces previous rising routes if a bigger rise is found.
            } else if (0 < found_rise && rise < found_rise) {
                rise = found_rise;
                rising_routes.clear();
                rising_routes.push_back(route.first);
            }
        }
        // No rise after the point.
        if (rise == 0) {
            std::cout << "No route rises after point " << point_name
                      << std::endl;
        // Prints the greatest rise and routes where it is.
        } else {
            std::cout << "Greatest rise after point " << point_name << ", "
                      << rise << " meters, is on route(s):" << std::endl;
            for (auto& route : rising_routes) {
                std::cout << " - " << route << std::endl;
            }
        }
    }
}

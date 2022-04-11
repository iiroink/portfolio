#include "route.hh"

Route::Route(std::string name, Point* first_point): name_(name),
    first_(nullptr), last_(nullptr)
{
    // Assign pointer to the first point.
    Route_points* start = new Route_points({first_point, nullptr});
    first_ = start;
    last_ = start;
}

Route::~Route()
{
    // Frees all points from memory.
    Route_points* to_delete(first_);
    while (to_delete) {
        first_ = first_->next;
        delete to_delete;
        to_delete = first_;
    }
}

void Route::addPoint(Point *to)
{
    // New point is added to the end. At this point at least one point exists.
    Route_points* new_point = new Route_points{to, nullptr};
    last_->next = new_point;
    last_ = last_->next;
}

void Route::print()
{
    // First point is printed without the arrow.
    std::cout << first_->point->getName() << std::endl;
    Route_points* current_point(first_->next);
    // Print all remaining points on the route.
    while (current_point) {
        std::cout << "-> " << current_point->point->getName() << std::endl;
        current_point = current_point->next;
    }
}

void Route::calculate_length()
{
    // First distance is from first point to second.
    Route_points* current_point(first_->next);
    double route_length = 0;
    // Initialize with coordinates of the first point.
    float x_prev = 0;
    float y_prev = 0;
    first_->point->getCoordinates(x_prev, y_prev);

    // Go through the whole route.
    while (current_point) {
        float x_curr = 0;
        float y_curr = 0;
        // Get coordinates for the next point.
        current_point->point->getCoordinates(x_curr, y_curr);
        // Calculate the distance.
        route_length += sqrt(pow(x_curr-x_prev,2)+pow(y_curr-y_prev,2));
        // Move to the next stretch.
        current_point = current_point->next;
        x_prev = x_curr;
        y_prev = y_curr;
    }
    std::cout << std::setprecision(2) << "Route " << name_ << " length was "
              << route_length << std::endl;
}

uint Route::rise(Point *start_point)
{
    uint start_height = 0;
    uint end_height = 0;
    Route_points* current_point(first_);
    // Find the starting point from the route.
    while (current_point && current_point->point != start_point) {
        current_point = current_point->next;
    }
    // If the point is not on the route, there is no rise.
    if (not current_point) {
        return 0;
    }

    // Start height is the height of the starting point.
    start_height = current_point->point->getHeight();
    // End height is checked with recursion.
    end_height = recursiveRise(current_point);
    // The rise is the height difference.
    return end_height - start_height;
}

uint Route::recursiveRise(Route_points *prev)
{
    Route_points* next = prev->next;
    // When the route ends or next point is lower than the previous one, that
    // is the end height for the rise.
    if (! next or next->point->getHeight() < prev->point->getHeight()) {
        return prev->point->getHeight();
    }
    // Rise continues.
    return recursiveRise(next);
}

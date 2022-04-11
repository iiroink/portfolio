#include "queue.hh"
#include <iostream>

Queue::Queue(unsigned int cycle): cycle_(cycle){
}

Queue::~Queue()
{
    while (first_ != nullptr) {
        Vehicle* to_destroy = first_;
        first_ = first_->next;
        delete to_destroy;
    }
}

void Queue::enqueue(const string &reg)
{
    if (is_green_) {
        std::cout << "GREEN: The vehicle " << reg << " need not stop to wait" << std::endl;
    } else {
        Vehicle* new_car = new Vehicle{reg, nullptr};
        if (first_ == nullptr) {
            first_ = new_car;
            last_ = new_car;
        } else {
          last_->next = new_car;
          last_ = new_car;
        }
    }
}

void Queue::switch_light()
{
    if (is_green_) {
        is_green_ = false;
        print();
    } else if (!is_green_ and first_ == nullptr) {
        is_green_ = true;
        print();
    } else  {
        std::cout << "GREEN: Vehicle(s) ";
        unsigned int cars_through = 0;
        Vehicle* car = first_;
        while (cars_through < cycle_ and car != nullptr) {
            std::cout << car->reg_num << " ";
            car = car->next;
            ++cars_through;
            delete first_;
            first_ = car;
        }
        std::cout << "can go on" << std::endl;
    }
}

void Queue::reset_cycle(unsigned int cycle)
{
    cycle_ = cycle;
}

void Queue::print() const
{
    if (is_green_) {
        std::cout << "GREEN: ";
    } else {
        std::cout << "RED: ";
    }
    if (first_ == nullptr) {
        std::cout << "No vehicles waiting in traffic lights" << std::endl;
    } else {
        std::cout << "Vehicle(s) ";
        Vehicle* next_car = first_;
        while (next_car != nullptr) {
            std::cout << next_car->reg_num << " ";
            next_car = next_car->next;
        }
        std::cout << "waiting in traffic lights" << std::endl;
    }
}

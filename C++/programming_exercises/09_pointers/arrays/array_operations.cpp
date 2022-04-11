#include "array_operations.hh"

int greatest_v1(int *itemptr, int size)
{
    int greatest = *itemptr;
    int* ptr = itemptr;
    while (ptr < itemptr + size) {
        if (*ptr > greatest) greatest = *ptr;
        ++ptr;
    }
    return greatest;
}

int greatest_v2(int *itemptr, int *endptr)
{
    int greatest = *itemptr;
    int* ptr = itemptr;
    while (ptr < endptr) {
        if (*ptr > greatest) greatest = *ptr;
        ++ptr;
    }
    return greatest;
}

void copy(int *itemptr, int *endptr, int *targetptr)
{
    int* from_ptr = itemptr;
    int* to_ptr = targetptr;
    while (from_ptr < endptr) {
        *to_ptr = *from_ptr;
        ++from_ptr;
        ++to_ptr;
    }
}

void reverse(int *leftptr, int *rightptr)
{
    int* start = leftptr;
    int* end = rightptr - 1;
    int tmp = 0;
    while (start < end) {
        tmp = *start;
        *start = *end;
        *end = tmp;
        ++start;
        --end;
    }
}

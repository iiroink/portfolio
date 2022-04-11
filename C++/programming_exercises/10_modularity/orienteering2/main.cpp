/*  COMP.CS.100 Project 3: ORIENTEERING
 *
 * Orienteering map analyser
 *
 * Reads the orienteering map data from a given file and offers tools to analyze
 * the routes and points in the map.
 *
 * Commands:
 * Commands are not capital sensitive. All parameters are checked.
 * - QUIT
 * - MAP: Prints the orienteering map. Points are represented by their marker.
 * - ROUTES: Prints all routes in ASCII-order.
 * - ROUTE <route>: Prints all points on <route>. Format is
 *                  first point
 *                  -> second point
 *                  -> ...
 * - POINTS: Prints all points and their markers in ASCII-order.
 * - LENGTH <route>: Prints the length of <route> starting from first point and
 *                   ending at the last point. Doesn't take height into account.
 * - RISE <point>: Prints the largest continuous rise after <point> and all
 *                 routes where it is found. Flat stretches are allowed.
 *
 * Code written by
 * Name: Iiro Inkinen
 * Student number: 50393673
 * Username: vbiiin
 * ( https://course-gitlab.tuni.fi/comp.cs.110-ohj-2_2022-KEVAT/vbiiin )
 * E-Mail: iiro.inkinen@tuni.fi
 *
 * */

#include "orienteeringmap.hh"
#include "parser.hh"
#include "cli.hh"
#include <iostream>

int main()
{
    std::shared_ptr<OrienteeringMap> routes(new OrienteeringMap);
    std::cout << "Input> ";
    std::string input;
    getline(std::cin, input);
    if( not read_input_from_file(input, routes) )
    {
        return EXIT_FAILURE;
    }
    Cli cli(routes);
    while( cli.exec_prompt() ){ }
    return EXIT_SUCCESS;
}



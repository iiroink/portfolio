#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <vector>

const std::string HELP_TEXT = "S = store id1 i2\nP = print id\n"
                              "C = count id\nD = depth id\n";

using Storage = std::map<std::string, std::vector<std::string>>;

std::vector<std::string> split(const std::string& s,
                               const char delimiter,
                               bool ignore_empty = false)
{
    std::vector<std::string> result;
    std::string tmp = s;

    while(tmp.find(delimiter) != std::string::npos)
    {
        std::string new_part = tmp.substr(0, tmp.find(delimiter));
        tmp = tmp.substr(tmp.find(delimiter) + 1, tmp.size());
        if(not (ignore_empty and new_part.empty()))
        {
            result.push_back(new_part);
        }
    }
    if(not (ignore_empty and tmp.empty()))
    {
        result.push_back(tmp);
    }
    return result;
}

void print(Storage& network, std::string& id, size_t depth=0)
{
    ++depth;
    for (auto name : network.at(id)) {
        std::string indent(depth * 2, '.');
        std::cout << indent << name << std::endl;
        if (network.find(name) != network.end()) {
                print(network, name, depth);
        }
    }
}

int count(Storage& network, std::string& name)
{
    int sum = 0;
    if (network.find(name) == network.end()) {
        return 1;
    } else {
        for (auto subname : network.at(name)) {
            sum += count(network, subname);
        }
        return sum + 1;
    }
}

int dep(Storage& network, std::string& name, int depth=0)
{
    ++depth;
    if (network.find(name) == network.end()) {
        return depth;
    } else {
            int tempD = 0;
        for (auto subname : network.at(name)) {
            if (dep(network, subname, depth) > tempD) {
                tempD += dep(network, subname, depth);
            }
        }
        return tempD;
    }
}

int main()
{
    std::map<std::string, std::vector<std::string>> network;


    while(true)
    {
        std::string line;
        std::cout << "> ";
        getline(std::cin, line);
        std::vector<std::string> parts = split(line, ' ', true);

        // Allowing empty inputs
        if(parts.size() == 0)
        {
            continue;
        }

        std::string command = parts.at(0);

        if(command == "S" or command == "s")
        {
            if(parts.size() != 3)
            {
                std::cout << "Erroneous parameters!" << std::endl << HELP_TEXT;
                continue;
            }
            std::string id1 = parts.at(1);
            std::string id2 = parts.at(2);

            if (network.find(id1) == network.end()) {
                network.insert({id1, {id2}});
            } else {
                network.at(id1).push_back(id2);
            }
        }
        else if(command == "P" or command == "p")
        {
            if(parts.size() != 2)
            {
                std::cout << "Erroneous parameters!" << std::endl << HELP_TEXT;
                continue;
            }
                std::string id = parts.at(1);
                std::cout << id << std::endl;
                print(network, id);
        }
        else if(command == "C" or command == "c")
        {
            if(parts.size() != 2)
            {
                std::cout << "Erroneous parameters!" << std::endl << HELP_TEXT;
                continue;
            }
            std::string id = parts.at(1);
            std::cout << count(network, id) - 1 << std::endl;

        }
        else if(command == "D" or command == "d")
        {
            if(parts.size() != 2)
            {
                std::cout << "Erroneous parameters!" << std::endl << HELP_TEXT;
                continue;
            }
            std::string id = parts.at(1);

            std::cout << dep(network, id) << std::endl;

        }
        else if(command == "Q" or command == "q")
        {
           return EXIT_SUCCESS;
        }
        else
        {
            std::cout << "Erroneous command!" << std::endl << HELP_TEXT;
        }
    }
}

#include <iostream>
#include <cmath>
#include <string>

int main() {
    // input string stuff
    std::string input;
    std::getline(std::cin, input);
    std::string height_str = input.substr(0, input.find(' '));
    std::string radius_str = input.substr(input.find(' ') + 1);

    // convert strings to float
    float height = std::stof(height_str);
    float radius = std::stof(radius_str);

    // V = π * r * r * h (π = 3.1415926536)
    float volume = M_PI * radius * radius * height;

    // rounding to 2 decimal places
    volume = round(volume * 100) / 100;
    std::cout << std::fixed;
    std::cout.precision(2);

    std::cout << volume << " cubic inches" << std::endl;

    return 0;
}
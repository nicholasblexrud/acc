//******************************************************************
// Author:                      Nick Blexrud
// Assignment Number:           Programming Assignment "Lab 1.2"
// File Name:                   blexrud_Lab1.2.cpp
// Course/Section:              COSC 1337 Section OO6
// Due Date:                    March 3, 2025
// Instructor:                  Professor Mohamed
//
// This programs calculates and displays the height of a basketball player
// in feet and inches
//******************************************************************
#include <iostream>    // input/output
using namespace std;

// main program
int main()
{
    // declare named constants
    const int HEIGHT_IN_INCHES = 74;  // set player height
    const int INCHES_IN_FOOT = 12;    // set inches in foot

    // calculate feet and inches
    int feet = HEIGHT_IN_INCHES / INCHES_IN_FOOT;
    int inches = HEIGHT_IN_INCHES % INCHES_IN_FOOT;

    // display the basketball player's height in feet/inches
    cout << "A " << HEIGHT_IN_INCHES << " inch tall basketball player is " 
    << feet << " feet " << inches << " inches tall." << endl;
    cout << "----------------------------------";

    return 0;
}
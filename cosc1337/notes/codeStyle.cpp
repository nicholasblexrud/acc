//******************************************************************
// Author:                      <Your name here>
// Assignment Number:           Programming Assignment "x"
// File Name:                   Program"x".cpp
// Course/Section:              COSC 1337 Section <your section number here>
// Due Date:                    <date goes here>
// Instructor:                  <your instructor's name here> 
//
// This program computes the miles per gallon for a trip given
// starting and ending mileage, and number of gallons used.
// It then displays the inputs and results.
//******************************************************************

#include <iostream>		// input/output
#include <iomanip>		// i/o manipulators
using namespace std;

// function prototypes
double mileage( double beginMiles, double endMiles, double gallonsUsed );

// main program
int main()
{
    double startMiles;      // Starting mileage
    double finishMiles;     // Ending mileage
    double gallonsUsed;     // Gallons of gas used
    double mpg;             // Computed miles per gallon

    //  Set up floating-point output format
    cout << fixed << setprecision(2);

    //  Get starting and ending mileage, and gallons of gas used
    cout << "Enter starting mileage: ";
    cin >> startMiles;
    cout << "Enter ending mileage: ";
    cin >> finishMiles;
    cout << "Enter number of gallons of gas used: ";
    cin >> gallonsUsed;

    //  Calculate miles per gallon
    mpg = mileage( startMiles, finishMiles, gallonsUsed );

    //  Print starting and ending mileage, gallons of gas used,
    //  and calculated mileage
    cout << "For a trip with:" << endl;
    cout << "    " << gallonsUsed << " gallons of gas used" << endl;
    cout << "    and a starting mileage of " << startMiles << endl;
    cout << "    and  an ending mileage of " << finishMiles << endl;
    cout << "    the mileage per gallon is " << mpg << endl;

    return 0;
}

// mileage
//	calculates and returns the trip miles per gallon
//	given a beginning mileage, ending mileage, 
//	and number of gallons of gas used
double mileage( double beginMiles, double endMiles,	double gallonsUsed )	
{
    double milesTraveled;		// Total miles traveled
    double milesPerGallon;		// Computed miles per gallon

	//  Calculate miles per gallon
    milesTraveled = endMiles - beginMiles;
    milesPerGallon = milesTraveled / gallonsUsed;

    return milesPerGallon;
}
/*
Enter starting mileage: 15500
Enter ending mileage: 15575
Enter number of gallons of gas used: 2.3
For a trip with:
    2.30 gallons of gas used
    and a starting mileage of 15500.00
    and  an ending mileage of 15575.00
    the mileage per gallon is 32.61
*/



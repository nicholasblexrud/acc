//******************************************************************
// Author:                      Nick Blexrud
// Assignment Number:           Programming Assignment "Lab 3"
// File Name:                   blexrud.Lab3.cpp
// Course/Section:              COSC 1337 Section OO6
// Due Date:                    March 24, 2025
// Instructor:                  Professor Mohamed
//
// The program asks the end user to enter sales amounts for four regions.
// It then displays the region and the amount, that is the highest. 
//******************************************************************
#include <iostream>    // input/output
#include <iomanip>     // i/o manipulators
#include <cstring>     // string class
using namespace std;

// function prototypes
int getSales(string divisionName);
void findHighest(int northEast, int southEast, int northWest, int southWest);

// main program
int main()
{

    // obtain the sales amount for each region
    double northEastSales = getSales("Northeast");
    double southEastSales = getSales("Southeast");
    double northWestSales = getSales("Northwest");
    double southWestSales = getSales("Southwest");

    // display the highest region and amount
    findHighest(northEastSales, southEastSales, northWestSales, southWestSales);

    return 0;
}

// getSales
//  asks the user for the sales amount for the region, checks is sales amount 
//  is valid, and then if valid, returns that amount
int getSales( string divisionName )
{
    bool isSalesValid = false;
    int salesAmount;

    cout << "Enter the quarterly sales for the " << divisionName 
    << " division: ";
    cin >> salesAmount;

    while (salesAmount <= 0)
    {
        cout << "Sales figures cannot be negative. Please re-enter." << endl;
        cout << "Enter the quarterly sales for the " << divisionName << ": " <<
        endl;
        cin >> salesAmount;
    }

    return salesAmount;
}

// findHighest
//  accepts four sales figures, determines the highest, and displays 
//  the region and amount that is the highest
void findHighest(int northEast, int southEast, int northWest, int southWest)
{
    double northHighest = 0;
    string northHighestString;

    double southHighest = 0;
    string southHighestString;

    double overallHighest = 0;
    string overallHighestString;

    northHighest = (northEast > northWest) ? northEast : northWest;
    northHighestString = (northEast > northWest) ? "Northeast" : "Northwest";

    southHighest = (southEast > southWest) ? southEast : southWest;
    southHighestString = (southEast > southWest) ? "Southeast" : "Southwest";

    overallHighest = (northHighest > southHighest) ? northHighest : southHighest;
    overallHighestString = (northHighest > southHighest) ? northHighestString :
    southHighestString;

    // setup floating-point output format
    cout << fixed << showpoint << setprecision(2);
    cout << endl;
    cout << "The " << overallHighestString << 
    " had the highest sales this quarter." << endl;
    cout << "Their sales were $" << overallHighest << endl; 

}
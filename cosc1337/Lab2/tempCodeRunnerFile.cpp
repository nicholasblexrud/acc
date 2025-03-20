//******************************************************************
// Author:                      Nick Blexrud
// Assignment Number:           Programming Assignment "Lab 2"
// File Name:                   blexrud_Lab2.cpp
// Course/Section:              COSC 1337 Section OO6
// Due Date:                    March 10, 2025
// Instructor:                  Professor Mohamed
//
// The program asks the end user how many software packages they'd like to
// purchase, and determines and applies a discount, if purchase qualifies.
// It then displays the total cost. 
//******************************************************************
#include <iostream>    // input/output
#include <iomanip>     // i/o manipulators
using namespace std;

// function prototypes
double calculateDiscount(int softwarePackages);
double calculateCost(int softwarePackages);

// declare named constants
const double SOFTWARE_PACKAGE_COST = 199.00;
const int MIN_NUMBER_OF_PACKAGES = 1;
const int PACKAGES_NEEDED_FOR_DISCOUNT = 10;

// main program
int main()
{
    int softwarePackages;  // # of software packages being purchased
    double cost;           // cost of the total purchase
    double discount;       // discount amount

    // setup floating-point output format
    cout << fixed << showpoint << setprecision(2);

    // get number of software packages
    cout << "How many units are being purchased? ";
    cin >> softwarePackages;

    // validate the input
    while (softwarePackages < MIN_NUMBER_OF_PACKAGES)
    {
        // display error
        cout << "ERROR: Enter a valid value that is equal to or greater than "
        << MIN_NUMBER_OF_PACKAGES << endl;

        // ask again
        cout << "How many units are being purchased? ";
        cin >> softwarePackages;
    }

    // check if the number of software packages qualifies for a discount
    if (softwarePackages >= PACKAGES_NEEDED_FOR_DISCOUNT)
    {
        discount = calculateDiscount(softwarePackages);
        cost = calculateCost(softwarePackages) - discount;
    } else 
    {
        cost = calculateCost(softwarePackages);
    }

    // display the cost 
    cout << "The total cost of the purchase is $" << cost << endl;

    return 0;
}

// calculateDiscount
//	determines the discount percentage based on the number of packages, 
//  and calculates and returns the discount amount
double calculateDiscount( int packages )
{
    double percentDiscount;

    if (packages >= 10 && packages <= 19)
    {
        percentDiscount = .20;
    } else if (packages >= 20 && packages <= 49)
    {
        percentDiscount = .30;
    } else if (packages >= 50 && packages <= 99)
    {
        percentDiscount = .40;
    }  else {
        percentDiscount = .50;
    }

    return packages * SOFTWARE_PACKAGE_COST * percentDiscount;
}

// calculateCost
//  calculates and returns the cost based on number of packages 
double calculateCost(int packages)
{
    return packages * SOFTWARE_PACKAGE_COST;
}
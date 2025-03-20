//******************************************************************
// Author:                      Nick Blexrud
// Assignment Number:           Programming Assignment "Lab 1.1"
// File Name:                   blexrud_Lab1.1.cpp
// Course/Section:              COSC 1337 Section OO6
// Due Date:                    March 3, 2025
// Instructor:                  Professor Mohamed
//
// This programs computes & displays the gross pay per paycheck 
// for both bi-monthly and bi-weekly pay periods.
//******************************************************************
#include <iostream>    // input/output
#include <iomanip>     // i/o manipulators
using namespace std;

// main program
int main()
{
    // declare named constants
    const int GROSS_SALARY = 39000;        // set gross salary
    const int BI_MONTHLY_PAY_PERIODS = 24; // set # of bi-monthly pay periods
    const int BI_WEEKLY_PAY_PERIODS = 26;  // set # of bi-weekly pay periods

    // calculate gross pay for different pay periods
    int bi_monthly_pay = GROSS_SALARY / BI_MONTHLY_PAY_PERIODS;
    int bi_weekly_pay = GROSS_SALARY / BI_WEEKLY_PAY_PERIODS;

    // display gross pay, and per pay period pays
    cout << "Annual gross salary " << setw(15) << "$" << setw(5)
    << GROSS_SALARY << endl;
    cout << "Gross pay per bi-monthly paycheck $" << setw(5) 
    << bi_monthly_pay << endl;
    cout << "Gross pay per bi-weekly  paycheck $" << setw(5) 
    << bi_weekly_pay << endl;
    cout << "-----------------------------------";

    return 0;
}
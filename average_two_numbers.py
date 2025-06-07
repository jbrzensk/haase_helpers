#!/usr/bin/env python3
##
# @file average_two_numbers.py
#
# @brief Computes the average of two command-line input numbers.
#
# @details This script accepts two numbers as command-line arguments,
#          computes their average, and prints the result. These comments
#          are writtetn in a Doxygen style format. You can generate a 
#          documentation using Doxygen by running `doxygen && doxygen`
#
# @author Jared Brzenski
#
# @date 2025-06-06
#
# @version 1.0
#
# The documentation follows the same format as the otehr files. There is
# a brief introduction, detail about the inputs, the outputs, and a brief 
# example of how torun the file. Remember, this is for others to understand
# the code, and also for you when you forget what you did in a few months.
#
# In doxygen, the input and output are given as @params.
# @param argv1 - command line argument 1, a string representing the first number.
#                This will be converted to a float.
# @param argv2 - command line argument 2, a string representing the second number
#                This will also be converted to a float.
#
# @return 0 on success, 1 on failure. We will print the results to stdout.
#
# @example To average 10.5 and 20.0, run the script as follows:
#          python3 average_two_numbers.py 10.5 20.0
#
# Here are some other examples:
#  ?> python3 average_two_numbers.py 20 21
#  The average of 20.0 and 21.0 is 20.5
#
#  ?> python3 average_two_numbers.py 20 -10
#  The average of 20.0 and -10.0 is 5.0
#
#  ?> python3 average_two_numbers.py 20 -1d
#  Error: Both inputs must be valid numbers.

# Note other things. There is constant spacing in this file. Sections are 
# seperated by a single line, and the comments are indented to match the code.
# The comments and description are taking up more than the actual code,
# but it is useful for understanding the code, especially for those who are not
# familiar with your specific bunch of code.

import sys

def main():
    ##
    # @brief Main function that handles input parsing and average calculation.
    #
    # @details This function checks for proper argument count, parses the 
    #          arguments as floats, computes the average, and prints the 
    #          result. Exits with an error message if input is invalid.
    #

    # Code not obvious to non-python people gets an explanation.
    # Check if exactly two arguments are provided (excluding the script name)
    # If not, print a useful message to the user, and exit with an error code.
    # It is always nice to tell the user what they did wrong, if anything.
    if len(sys.argv) != 3:
        print("Usage: python3 average_two_numbers.py <num1> <num2>")
        sys.exit(1)

    try:
        ##
        # @var num1
        # @brief First input number converted from string to float.
        ##
        # @var num2
        # @brief Second input number converted from string to float.
        ##
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    # Note that the next three lines don't need a comment, the code says
    # what it does. Here we tell the user exactly what went wrong. Error
    # checking is important, and helpful as code gets more complex.
    except ValueError:
        print("Error: Both inputs must be valid numbers.")
        sys.exit(1)

    ##
    # @var average
    # @brief The computed average of num1 and num2.
    ##
    average = (num1 + num2) / 2

    # Print the result
    print(f"The average of {num1} and {num2} is {average}")

##
# @brief Script entry point.
#
# @details Calls the main() function when the script is executed directly.
#
# This is also python specific, and it is not needed in C/C++, FORTRAN, etc.
if __name__ == "__main__":
    main()

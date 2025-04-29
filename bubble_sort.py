#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: April 27th, 2025

# Bubble sort program in python

import random
import time


def bubble_sort(array):

    # Initialize new array
    new_array = []
    length = len(array)
    iterations = 0

    red = "\033[91m"
    reset = "\033[0m"

    # Create new array that's a replica of old one
    for i in range(len(array)):
        new_array.append(array[i])

    while True:

        # Check array
        array_sorted = True

        for n in range(1, length):
            if new_array[n - 1] > new_array[n]:
                array_sorted = False

        if array_sorted:
            break

        # Sort array
        for x in range(1, length):  # start from 1 to avoid x-1 being -1
            iterations += 1

            if new_array[x - 1] > new_array[x]:

                # Show before (properly colored)
                highlighted = []
                for h in range(length):
                    if h == x or h == x - 1:
                        highlighted.append(f"{red}{new_array[h]}{reset}")
                    else:
                        highlighted.append(
                            str(new_array[h])
                        )  # convert to str for printing

                print("Swap:", " ".join(highlighted))  # print colored output

                # Swap
                new_array[x - 1], new_array[x] = new_array[x], new_array[x - 1]
                
        time.sleep(0.1)

    # Return new array as well as number of iterations
    return new_array, iterations


def setup_array(length):
    array = []

    for i in range(length):
        array.append(random.randrange(1, 100))

    return array


def main():

    # Get length of array from user
    length = input("Please enter an integer length for your array: ")

    # Try catch to make sure that length is valid
    try:

        # Convert length to integer, setup array
        length = int(length)
        original_array = setup_array(length)

        print("Your array is:", original_array)

        new_array, iterations = bubble_sort(original_array)

        print("Your original array was:", original_array)
        print("Your new array is:", new_array)
        print("It took", iterations, "iterations to sort.")
        print("The worst case scenario would have been", length**2, "iterations.")

        # Prompt program restart
        restart = input("Try again? (yes/no): ")

        if restart == "yes":
            main()
        else:

            # Termination message
            print("Thanks for using my sorting program!")

    except:

        # User didn't enter proper length
        print("Please enter a proper integer")


if __name__ == "__main__":
    main()

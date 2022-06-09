#!/usr/bin/env python3

# Created by: Andrew-Ten-Den
# Created on: June 2022
# This program finds the smallest of 10 random numbers

import random


def main():

    random_numbers = []

    loop_counter = 0
    smallest = 100
    # input
    print("Here are the 10 numbers:")

    for loop_counter in range(10):
        random_variable = random.randint(0, 100)
        random_numbers.append(random_variable)
        if random_variable < smallest:
            smallest = random_variable

        loop_counter = loop_counter + 1
    print("")
    print(random_numbers)
    print("The smallest of these 10 numbers is {}".format(smallest))

    print("\n\nDone.")


if __name__ == "__main__":
    main()

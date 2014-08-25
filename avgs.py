#!/usr/bin/python3
"""
Copyright (c) 2014 Robert Wallis All Rights Reserved
Quick script for scraping comments on linkedin for guesses on a jelly-bean contest.
For the purpose of using the median [Francis Galton 1907 - Nature et al] to guess the correct answer.
"""
import re
def averages(threshold=0.01):
    """
    Search the file guesses.txt for numbers, and calculate the averages
    Filters out extreme guesses, via 3-5 digits.  Also I manually deleted some large guesses and phone numbers in guesses.txt
    threshold = percent to display people that are close to the average at the time of their guess
    """
    filename = "guesses.txt" # copy-pasta from 210+ pages of linkedin comments
    rex_guess = re.compile(r"[\d\,]{3,5}")
    rex_time_ago = re.compile(r"\d\d?[dhs] ago")
    numbers = []

    pages = 1 # linkedin pages are 1 based
    line_i = 0
    line_last = 0
    total = 0
    total_100 = 0

    for line in open(filename):

        match_number = rex_guess.search(line)

        if match_number:
            guess = re.sub(",", "", match_number.group())
            guess = int(guess)

            # out the people that are using the same method
            if len(numbers) > 0:
                avg = total / len(numbers)
                if guess > avg - (avg * threshold) and guess < avg + (avg * threshold):
                    print("*** close ***", line.strip(), " avg:", avg, " line:", line_i)

            numbers.append(guess)
            total += guess 
            total_100 += guess

            # show progress per 100 guesses for the purposes of graphing the settling to a median
            if len(numbers) % 100 == 0:
                print("i:", len(numbers), " avg:", avg, " avg 100:", total_100 / 100)
                total_100 = 0

        # newline between page numbers
        if len(line.strip()) == 0:
            pages += 1
            line_last = line_i

        # display copypasta errors with getting first guess on a page
        elif line_last == line_i-1:
            if rex_time_ago.search(line):
                print("line: ", line_i, " missing top page:", pages)

        line_i += 1

    # validate the number of pages (currently this is incorrect)
    print("pages:", pages)
    
    # total result
    print("avg:", (sum(numbers) / len(numbers)), " of:", len(numbers))

    # return numbers for further analysis
    return numbers


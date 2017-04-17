# -*- coding: UTF-8 -*-
"""Refactoring.

This excercise is very similar to week 2, exercise 2. It contains a complete
and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

The resulting file should feel as close to english as possible.
It must also pass the linter.

This is the first file that will be run against the pydocstyle checker. If
you've run the week5_system_prep.sh file you should be getting blue linter dots
that show you where lintere errors are. If they aren't working, you should be
getting the errors in the test output.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""

from __future__ import division
from __future__ import print_function
import math
import requests


# This is a terrible function. The rest of the functions in this file do a
# much better job of what it's trying to do. Once you've has a little look,
# move on, and eventually delete this function. (And this comment!)
def do_bunch_of_bad_things():
    """Run Ben's initial test of doing bad stuff."""
    print("Getting ready to start in 9")
    print("Getting ready to start in 8")
    print("Getting ready to start in 7")
    print("Getting ready to start in 6")
    print("Getting ready to start in 5")
    print("Getting ready to start in 4")
    print("Getting ready to start in 3")
    print("Getting ready to start in 2")
    print("Getting ready to start in 1")
    print("Let's go!")

    triangle = {"base": 3, "height": 4}
    triangle["hypotenuse"] = triangle["base"]**2 + triangle["height"]**2
    print("area = " + str((triangle["base"] * triangle["height"])/2))
    print("side lengths are:")
    print("base: {}".format(triangle["base"]))
    print("height: {}".format(triangle["height"]))
    print("hypotenuse: {}".format(triangle["hypotenuse"]))

    another_hyp = 5**2 + 6**2
    print(another_hyp)

    yet_another_hyp = 40**2 + 30**2
    print(yet_another_hyp)


# return a lit of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    """Print a coundown from a value. Return a different complete message.

    Push it to a list and return the list at the end.
    """
    output_list = []
    print(start)
    start = int(start)
    print(stop)
    stop = int(stop)
    if stop < start:
        step = -1
    else:
        step = 1
    i = start
    while i != stop:
        print(message + str(i))
        output_list.append(message + str(i))
        i = i + step
    output_list.append(completion_message)
    return output_list


countdown("Getting ready to start in ", 9, 0, "Let's go!")


# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    """Calculate the hypotenuse of a triangle."""
    hypotenuse = math.sqrt(math.pow(base, 2) + math.pow(height, 2))
    print(hypotenuse)
    return hypotenuse


def calculate_area(base, height):
    """Calculate the area of a triangle."""
    area = (base * height) / 2
    return area


def calculate_perimeter(base, height):
    """Calculate the perimeter of a triangle."""
    hypotenuse = calculate_hypotenuse(base, height)
    perimeter = hypotenuse + base + height
    return perimeter


def calculate_aspect(base, height):
    """Calculate the aspect ratio.

    returns tall, wide or equal
    """
    if base > height:
        return "wide"
    elif base < height:
        return "tall"
    else:
        return "equal"


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    """Return the triangle facts."""
    area = calculate_area(base, height)
    perimeter = calculate_perimeter(base, height)
    hypotenuse = calculate_hypotenuse(base, height)
    aspect = calculate_aspect(base, height)
    return {"area": area,
            "perimeter": perimeter,
            "height": height,
            "base": base,
            "hypotenuse": hypotenuse,
            "aspect": aspect,
            "units": units}


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    """Output a diagram of the triangle."""
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = ("This triangle is {area}{units}²\n"
               "It has a perimeter of {perimeter}{units}\n"
               "This is a {aspect} triangle.\n")

    facts = pattern.format(**facts_dictionary)
    if facts_dictionary["aspect"] == "tall":
        output = tall.format(**facts_dictionary)
        print(output + facts)
        return output + facts
    elif facts_dictionary["aspect"] == "wide":
        output = wide.format(**facts_dictionary)
        print(output + facts)
        return output + facts
    else:
        output = equal.format(**facts_dictionary)
        print(output + facts)
        return output + facts


def triangle_master(base,
                    height,
                    return_diagram=False,
                    return_dictionary=False):
    """Return a diagram, a dictionary, or both."""
    triangle_dictionary = get_triangle_facts(base, height, units="mm")
    diagram = tell_me_about_this_right_triangle(triangle_dictionary)
    if return_diagram and return_dictionary:
        # return diagram
        # return triangle_dictionary
        None
    elif return_diagram:
        return diagram
    elif return_dictionary:
        # return triangle_dictionary
        None
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    """Create a word pyramid with functions."""
    list_of_lengths = []
    for i in range(3, 21, 2):
        list_of_lengths.append(i)
    for i in range(20, 3, -2):
        list_of_lengths.append(i)
    return list_of_words_with_lengths(list_of_lengths)


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    while True:
        try:
            result = int(raw_input(message))
            return result
        except:
            print("Not an integer")


def get_a_word_of_length_n(length):
    """Get a word of specified length."""
    baseURL = "http://www.setgetgo.com/randomword/get.php?len="
    url = baseURL + str(length)
    r = requests.get(url)
    message = r.text
    return message


def list_of_words_with_lengths(list_of_lengths):
    """Get a list of lengths to call words."""
    pyramid_list = []
    for i in list_of_lengths:
        message = get_a_word_of_length_n(i)
        pyramid_list.append(message)
    return pyramid_list


if __name__ == "__main__":
    do_bunch_of_bad_things()

#!/usr/bin/python
"""This program calculates your weight on the moon"""
import random
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("user_input")
args = parser.parse_args()

EARTH_GRAVITY = 9.8
MOON_DIFFERENTIAL = 1.622
user_earth_weight = args.user_input

def get_moon_fact():
    moon_facts = ["The Moon is Earth's only permanent natural satellite",
    "The Moon always shows Earth the same face.",
    "The Moon's surface is actually dark.",
    "There is water on the Moon!",
     "The Moon makes the Earth move as well as the tides.",
     "The Moon was made when a rock smashed into Earth.",
     "The Moon is moving approximately 3.8 cm away from our planet every year.",
     "The Moon is 400 times smaller than the Sun,"
    ]
    return moon_facts[random.randint(1,8)]



def calc_moon_weight(user_weight):
    earth_weight = float(user_weight)

    moon_weight = (earth_weight/ EARTH_GRAVITY) * MOON_DIFFERENTIAL

    return str(round(moon_weight, 3))

def show_results_to_user():
    user_moon_weight = calc_moon_weight(user_earth_weight)
    user_moon_fact = get_moon_fact()

    print("Moon Fact: ")
    print(user_moon_fact + "\n")
    print("Your weight on the moon would be: " + user_moon_weight)

show_results_to_user()




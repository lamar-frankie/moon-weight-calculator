#!/usr/bin/env python3
"""
Author : Frank Lamar
Date   : 01/19/2021
Purpose: Print out a pirate message
"""

import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Print out a Pirate Message')

    parser.add_argument('-h', '--help', help='Print a Pirate message')

    return parser.parse_args()

def main():
    args = get_args()
    print(args)

if __name__ == '__main__':
    main() 
#!/usr/bin/env python
"""
A python script to check Alexa rankings of websites.

Requirements:
- Python 3.x
"""
import argparse

def main():
    """
    Main function.
    Checks command-line arguments and calls the relevant function.
    """

    cli_argparser = argparse.ArgumentParser(description='')
    cli_argparser.add_argument('-l', '--all', help="Lists all the information about the current WAN IP.", required=False)
    cli_argparser.add_argument('-c', '--country', help="Lists the country of origin for the current WAN IP.", required=False)
    cli_args = cli_argparser.parse_args()

if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python
"""
A python script to check Alexa rankings of websites.

Requirements:
- Python 3.x
"""
import sys
import argparse
import urllib.request, json

def myip(*arg):
    """
    Function to get the WAN IP's information.
    """

    ip_response =  json.loads(urllib.request.urlopen('http://wtfismyip.com/json').read().decode("utf-8"))
    
    if (arg):
        if (arg[0] == "l"):
            print ("\nYour WAN IP's location is: " + ip_response["YourFuckingLocation"] + "\n")
        elif (arg[0] == "a"):
            print ("\nYour WAN IP is:\t\t\t" + ip_response["YourFuckingIPAddress"])
            print ("Your WAN IP's hostname is:\t" + ip_response["YourFuckingHostname"])
            print ("Your WAN IP's ISP-ASN is:\t" + ip_response["YourFuckingISP"])
            print ("Your WAN IP's location is:\t" + ip_response["YourFuckingLocation"] + "\n")
        else:
            print ("Wrong argument!")
    else:
        return ip_response["YourFuckingIPAddress"]

def main():
    """
    Main function.
    Checks command-line arguments and calls the relevant function.
    """

    cli_argparser = argparse.ArgumentParser(description='pymyip - A python script that shows your current WAN IP address.')
    cli_argparser.add_argument('-a', '--all', nargs='?', const=1, help="Lists all the information about the current WAN IP.", required=False)
    cli_argparser.add_argument('-l', '--location', nargs='?', const=1, help="Lists the country of origin for the current WAN IP.", required=False)

    cli_args = cli_argparser.parse_args()

    if (cli_args.all):
        (myip("a"))
    elif (cli_args.location):
        (myip("l"))
    else:
        print ("\nYour WAN IP is: " + myip() + "\n")

if __name__ == '__main__':
    sys.exit(main())

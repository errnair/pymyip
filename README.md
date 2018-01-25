### pymyip - A python script that shows your current WAN IP address.  

#### Requirements

- Python 3.x

#### Purpose

This script displays your WAN IP information from the command-line. It makes use of a fun website called [wtfismyip.com](https://wtfismyip.com/)  
The script also accepts arguments to:  

- Display the location of the current WAN IP.
- List all the information associated with the current WAN IP.

```
$ python pymyip.py --help
usage: pymyip.py [-h] [-a [ALL]] [-l [LOCATION]]

pymyip - A python script that shows your current WAN IP address.

optional arguments:
  -h, --help                            show this help message and exit
  -a [ALL], --all [ALL]                 Lists all the information about the current WAN IP.
  -l [LOCATION], --location [LOCATION]  Lists the country of origin for the current WAN IP.
```

#### Usage

1. List the current WAN IP address.
```
$ python pymyip.py

Your WAN IP is: 2XX.XX.XXX.XX7

```

2. List the current WAN IP's geographical location.
```
$ python pymyip.py -l

Your WAN IP's location is: LOCATION, COUNTRY

```
  
3. List all the relevant information about the current WAN IP.
```
$ python pymyip.py -a

Your WAN IP is:                 2XX.XX.XXX.XX7
Your WAN IP's hostname is:      hostname.domainname.tld
Your WAN IP's ISP-ASN is:       ISP-ASN
Your WAN IP's location is:      LOCATION, COUNTRY
```  
  
#### Credits  

- [wtfismyip.com](https://wtfismyip.com)

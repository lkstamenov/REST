from urllib.parse import urlparse
import requests
from flask import Flask


# a valid URL
url = 'http://127.0.0.1:5000/api/v1/countries?name=Italy'

# Dictionary with all available countries
codes = {'Bulgaria':'BG','France':'FR','Germany':'DE','Ireland':'IR','Spain':'SP','UK':'UK'}

# Parsing the URL
o = urlparse(url)

# Extract the country name from the URL
substr = o.query[5:]

# Print the URL
print('The URL you entered is:', url)

# Search if the country has a code
if substr in codes.keys():
    # Print the country code
    print('The country code for',substr,'is:', codes[substr])
else:
    print('The country code for',substr,'is not present')
    # Convert country dictionary keys to a string
    substrcodes=str(codes.keys())
    # Slice substrcodes
    print('Available countries are: ',substrcodes[11:-2])

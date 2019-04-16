import requests
import json
import argparse
import configparser
import read_configfile
import urllib
import urllib.request,urllib.parse,urllib.error
import sys

parser = argparse.ArgumentParser(description='Process movies names and queries Rotten')
parser.add_argument('--movie', help='Type movie name to search' ,required=True)

args = parser.parse_args()
movietitle=args.movie

obj=read_configfile.read_config_file ("config.txt")
apitoken=obj["Omdb"]["apikey"]
if not apitoken:
    print ("api token is not provided. Please check the config file")
    sys.exit(1)
else:
    api_token="&apikey="+apitoken
istomatoes=obj["Omdb"]["tomatoes"]
if not istomatoes:
    print ("Rotten tomotoes config not found, setting default to True") 
    is_tomatoes="&tomatoes="+"true"
else:
    is_tomatoes="&tomatoes="+istomatoes

# api_token = 'i=tt3896198&apikey=bddd0ce0'
api_url_base = 'http://www.omdbapi.com/?'
RottenRatting = False
try:
    url = api_url_base + urllib.parse.urlencode({'t': movietitle})+api_token+is_tomatoes
    res =  urllib.request.urlopen(url)    
    json_data = json.load(res)
    if json_data['Response']=='True':
        print ("title:" , json_data["Title"])
        print ("Year:", json_data["Year"])
        print ("Rating:", json_data["Rated"])
        print ("Release Date:", json_data["Released"])
        print ("Show Time:", json_data["Runtime"])
        print ("Director:", json_data["Director"])
        print ("Writer:", json_data["Writer"])  
        ratingsobj = json_data['Ratings']
        if ratingsobj is not None:
            for source in ratingsobj:
                if (source['Source']=='Rotten Tomatoes'):
                    RottenRatting = True
                    print ("Rotten Tomatoes Rating:", source['Value'])
                    break;
        if (RottenRatting == False):
            print ("Rotten Tomatoes doesn't have a rating for this movie")
    else:
        print ("Please pass valid movie name")

except urllib.error.URLError as e:
    print ("ERROR:",(e.reason)+ "  ERROR CODE:", (e.code))
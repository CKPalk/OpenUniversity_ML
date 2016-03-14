
from urllib.request import urlopen
from urllib.request import Request
import json
import sys
import pandas as pd
import numpy as np

key = '7ad6e966485527aa'

def getWeatherJSON( day, month, year ):

    url = "http://api.wunderground.com/api/{key}/history_{YYYY}{MM:0>2d}{DD:0>2d}/q/WA/Seattle.json".format(
        key     = key,
        YYYY    = year,
        MM      = month,
        DD      = day )

    request = Request( url )
    with urlopen( request ) as response:
        response = response.read()
    parsed_json = json.loads( response.decode('utf-8') )
    return parsed_json


def appendTempIfNeeded( df ):
    if 'Temp' not in df.columns:
        df['Temp'] = np.nan
    return df


def findBestTemp( date ):
    json = getWeatherJSON( date.day, date.month, date.year )
    



def addWeatherData( csv_filename ):

    df = pd.read_csv( csv_filename, parse_dates=['Dates'], date_parser=lambda
            x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S' ) )

    df = appendTempIfNeeded( df )

    for idx, row in df.iterrows():
        if pd.isnull( row['Temp'] ):
            print( "Found a null temperature, looking up temp for", row['Dates'] )
            row_temp = findBestTemp( row['Dates'] )

            return
        else:
            print( "Found temperature", row['Temp'] )






    #response = getWeatherJSON( 9, 6, 1994 )
    #print( response['history']['dailysummary'][0]['meantempi'] )

def main( argv ):
    addWeatherData( argv[1] )


if __name__ == '__main__':
    main( sys.argv )


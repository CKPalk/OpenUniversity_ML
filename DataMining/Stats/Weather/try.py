
import json
import sys


json_str = open( sys.argv[1], 'r' ).read()
data = json.loads( json_str )

print( data['2002-03-27']['history']['observations'][2] )

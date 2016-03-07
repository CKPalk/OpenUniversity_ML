import sys
import operator


def statsForAttr( Data, attr ):
    attr_index = Data[0].index( attr )
    counts = {}
    print( attr_index )
    for row in Data[1]:
        print( len( row ) )
        val = row[ attr_index ]
        if val in counts:
            counts[ val ] += 1
        else:
            counts[ val ]  = 1
    output_string = ""
    sorted_counts = sorted( counts.items(), key=operator.itemgetter(1) )
    return repr(sorted_counts)
        



def main( argv ):
    if len( argv ) != 2:
        print( "Usage: \"python3 {} <CSV> <Output_File>\"".format( sys.argv[0] ) ); return

    csv_file    = argv[ 0 ]
    output_file = argv[ 1 ]

    csv_attrs = []
    csv_data  = []
    
    with open( csv_file, 'r' ) as csv_stream:
        csv_raw = csv_stream.read()
        csv_raw_rows = csv_raw.split( '\n' )
        csv_split_rows = [ row.split( ',' ) for row in csv_raw_rows ]
        csv_data = ( csv_split_rows[0], csv_split_rows[1:] )

    with open( output_file, 'w+' ) as output_stream:
        section_split = "\n\n\n"
        for attr in csv_data[0]:
            output_stream.write( statsForAttr( csv_data, attr ) )
            output_stream.write( section_split )


if __name__=='__main__':
    main( sys.argv[1:] )

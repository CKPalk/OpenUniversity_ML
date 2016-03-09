import sys
import operator


def statsForAttr( Data, attr, summarized=False ):

	attr_index = Data[0].index( attr )
	counts = {}
	attr_count = len( Data[0] )

	empty_cell_count = 0
	unusable_row_count = 0
	for row_i, row in enumerate(Data[1]):

		if len( row ) != attr_count:
			print( "Row", row_i, "does not have", attr_count, "attributes, it has", len( row ) )
			unusable_row_count += 1
			continue

		val = row[ attr_index ]
		if val is '':
			empty_cell_count += 1
		elif val in counts:
			counts[ val ] += 1
		else:
			counts[ val ]  = 1

	sorted_counts = sorted( [ (v,k) for k,v in counts.items() ], reverse=True )
	sorted_length = len( sorted_counts )
	if sorted_length > 500:
		return ( 
			"{:34}  ->  {:7} unique cells    {:7} empty cells\n".format(attr,sorted_length,empty_cell_count) + 
			"" if summarized else ( "----------------------------------------\n" + 
					'\n'.join( [ "{}: {}".format(k,v) for v,k in [ sorted_counts[0], sorted_counts[-1] ] ] ) ) )
	else:
		return ( 
			"{:34}  ->  {:7} unique cells    {:7} empty cells\n".format(attr,sorted_length,empty_cell_count) + 
			"" if summarized else ( "----------------------------------------\n" + 
					'\n'.join( [ "{}: {}".format(k,v) for v,k in sorted_counts ] ) ) )



def main( argv ):
	if len( argv ) != 2:
		print( "Usage: \"python3 {} <CSV> <Output_File>\"".format( sys.argv[0] ) ); return

	csv_file	= argv[ 0 ]
	output_file = argv[ 1 ]

	csv_attrs = []
	csv_data  = []
	
	with open( csv_file, 'r' ) as csv_stream:
		csv_raw = csv_stream.read()
		csv_raw_rows = csv_raw.split( '\n' )
		csv_split_rows = [ [ val.upper() for val in row.split( ',' ) ] for row in csv_raw_rows ]
		csv_data = ( csv_split_rows[0], csv_split_rows[1:-1] )

	with open( output_file, 'w+' ) as output_stream:
		section_split = "\n\n\n"

		output_stream.write( section_split )
		for attr in csv_data[0]:
			output_stream.write( statsForAttr( csv_data, attr, summarized=True ) )
		output_stream.write( section_split )
		for attr in csv_data[0]:
			output_stream.write( statsForAttr( csv_data, attr ) )
			output_stream.write( section_split )


if __name__=='__main__':
	main( sys.argv[1:] )

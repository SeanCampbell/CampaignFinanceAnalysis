import csv, sys

# Get filename from command line argument.
with open(sys.argv[1], "rb") as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	# This dictionary will hold all the information.
	# ID : Transaction code : List of amounts
	data_dict = {}
	for row in reader:
		#row = reader.next()
		filer_id = row[0]
		transaction_code = row[2]
		amount = row[19]
		# If the transaction is not of type A, B, or C, we don't care
		# about it.
		if (transaction_code in ['A', 'B', 'C']):
			# Create an entry in the dictionary if there isn't already
			# one there for this filer.
			if (not filer_id in data_dict.keys()):
				data_dict[filer_id] = { 'A': [], 'B': [], 'C': []}
			# And finally, add this donation to the list of the filer's donations.
			data_dict[filer_id][transaction_code].append(amount)
	print data_dict

import csv

filepath = './20170817_Flow_Anon.csv'

with open(filepath, 'rb') as infile:
	reader = csv.reader(infile.read().splitlines())
	headers = reader.next()
	for header in headers:
		print headers.index(header), header

	new_header = ["Patient Name", "Time Type", "Flow Step", " Start Time", "End Time"]

	with open("./20170817_Flow_Anon_transformed.csv", "wb") as outfile:
		writer = csv.writer(outfile)
		writer.writerow(new_header)
		for row in reader:
			#arrival step
			write_row = [row[0], "Expected", "Expected Arrival Time", row[1], row[1]]
			writer.writerow(write_row)

			#start/end steps
			for i in xrange(2, 15, 2):
				if i in range(0, 4): 
					time_type = "Expected"
					flow_step = headers[i]
				else:
					time_type = "Actual"
					flow_step = headers[i]
					flow_step = flow_step.rsplit(' ', 1)[0]
				
				try:
					write_row = [row[0], time_type, flow_step, row[i], row[i+1]]
					writer.writerow(write_row)
				except IndexError:
					print i, "INDEX"
					for col in row:
						print row.index(col), col
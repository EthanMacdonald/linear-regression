from pattern.en import sentiment
import csv

csv_path = "../data/reddit/csv/trainingandTestDataset.csv"
output_path="../data/reddit/csv/senti_training.csv"

# Read CSV and create output
r=csv.reader(open(csv_path, 'rb'))
output=[]

# Modify headers and append to output
headers = next(r)
headers.insert(-1, 'affect')
headers.insert(-1, 'objectivity')
output.append(headers)

# Modify data and append to output
for line in r:
	pos, obj = sentiment(line[1])
	print pos, obj
	line.insert(-1, pos)
	line.insert(-1, obj)
	output.append(line)

# Write output to file
output_file=csv.writer(open(output_path, 'wb'))
output_file.writerows(output)
output_file.close()
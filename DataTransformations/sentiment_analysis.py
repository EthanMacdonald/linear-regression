from pattern.en import sentiment
import csv

#TODO: Remember to make sure score is at the end of the csv row

csv_path = "../data/reddit/csv/training.csv"
output_path="../data/reddit/csv/senti_training.csv"

r=csv.reader(open(csv_path, 'rb'))
output=[]
for line in r:
	pos, obj = sentiment(line[0])
	line.append(pos)
	line.append(obj)
	output.append(line)

output_file=csv.writer(open(output_path, 'wb'))
output_file.writerows(output)
output_file.close()
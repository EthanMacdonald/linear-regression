import json, os

data_dir = "../data/reddit/json/sub"
write_dir = "../data/reddit/json/_sub"

for f in [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith(".json")]:
	f_json = json.loads(open(f).read())
	scrape_time = f_json["scrape_time_utc"]
	del f_json["scrape_time_utc"]
	for child in f_json["data"]["children"]:
		child["data"]["scrape_time_utc"] = scrape_time
	new_f = open(os.path.join(write_dir, os.path.basename(f)), 'w')
	json.dump(f_json, new_f)
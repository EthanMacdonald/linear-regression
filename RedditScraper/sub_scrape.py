import json, praw, os, time

data_dir = "../data/reddit/json/sub"
url = 'https://www.reddit.com/r/all/new'

params = {'limit': 100}
i = 0
while True:
	try: 
		if i % 20 == 0:
			time.sleep(60)
		r = praw.Reddit(user_agent='laptop:YnAFbPkdUgE0Ig:1.0')
		r.config.store_json_result = True
		submissions = r.request_json(url, params=params, as_objects=False)
		submissions['scrape_time_utc'] = time.time()
		after = submissions['data']['after']
		params = {'limit': 100, 'after': after}
		with open(os.path.join(data_dir, after+'.json'), 'w+') as f:
			json.dump(submissions, f)
		i += 1
		print "Submissions saved: " + str(i*100)
	except Exception as e:
		print e
		continue

import requests
#import json # used for lines 10 - 17 only
from operator import itemgetter 

# make an API call to see if hacker news site status code is 200
# top stories API, page 380
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# region Explore the structure of the data by storing it locally as readable json

# response_dict = r.json()
# readable_file = 'data/readable_hn_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(response_dict, f, indent = 4)

# endregion

# process info about each submission
submission_ids = r.json()
submission_dicts = []

# check top 30 latest submissions
for submission_id in submission_ids[:30]:
    # Make a seperate API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id : {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # build a dictionary for each article
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'score': response_dict['score'],
    }
    submission_dicts.append(submission_dict)

# sort list of dictionary by the article score
submission_dicts = sorted(submission_dicts, key = itemgetter('score'), reverse = True)

# output info from submission_dicts in terminal
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Score: {submission_dict['score']}")
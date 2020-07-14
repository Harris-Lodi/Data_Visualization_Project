import requests
from plotly.graph_objs import Bar 
from plotly import offline 

# make an API call and store the response
# url api source: located in README.md file
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# headers ask api to use specific version
headers = {'Accept': 'application/vnd.github.v3+json'} 
# once inputs are set, we use requests to make a call to the API
r = requests.get(url, headers=headers)
# find status code from API response and print it, 200 means we are connected
print(f"status code: {r.status_code}")

# store API response in a variable as json object
response_dict = r.json()

# find the total number of repos and print it 
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories
repo_dicts = response_dict['items']
print(f"Repositories Returned: {len(repo_dicts)}")

# process results for plotting
repo_links, stars, labels = [], [], []

for repo_dict in repo_dicts:

    # x and y values for plot
    # add clickable links to the repos, x value
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href = '{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    # Y value
    stars.append(repo_dict['stargazers_count'])

    # create label for each repo
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# make visualization
data = [
    {
        'type': 'bar',
        'x': repo_links,
        'y': stars,
        'hovertext': labels,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.6,
    }]

my_layout = {
    'title': 'Most Starred Python Projects on Github',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
    }

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'python_repos.html')

# region examine first entry only

# examine the first repository (comment)
# repo_dict_alpha = repo_dicts[0]
# print the key attributes we can access about the repo (comment)
# print(f"\nKeys: {len(repo_dict_alpha)}") # print new line then Keys
# print keys (comment)
# for key in sorted(repo_dict_alpha.keys()):
#     print(key)

# endregion

# region pull some info from the top repos

# output dictionary keys available in response, (comment)
# results were 'total_count', 'incomplete_results', and 'items' (comment)
# print(response_dict.keys())

# print("\nSelected info about each repo!")
# for repo_dict in repo_dicts:

#     print(f"\nName: {repo_dict['name']}")
#     print(f"Owner: {repo_dict['owner']['login']}")
#     print(f"Stars: {repo_dict['stargazers_count']}")
#     print(f"Repository URL: {repo_dict['html_url']}")
#     print(f"Created: {repo_dict['created_at']}")
#     print(f"Updated last: {repo_dict['updated_at']}")
#     print(f"Description: {repo_dict['description']}")

# endregion

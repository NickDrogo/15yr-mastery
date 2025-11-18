import requests
import plotly.express as px

# Make an API call and check the response .
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()


submission_dicts, discussions_links, comments, hover_texts = [], [], [], []

for submission_id in submission_ids[:5]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"

    r = requests.get(url)

    print(f"status code: {r.status_code}")

    response_dict = r.json()


    # Build  a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link':f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],

    }

    discussions_link = f"<a href={submission_dict['hn_link']}>{submission_dict['title']}</a>"

    submission_dicts.append(submission_dict)
    discussions_links.append(discussions_link)
    comments.append(submission_dict['comments'])
    
    
    # Build hover texts.
    hover_text = submission_dict['title']
    hover_texts.append(hover_text)


title = "Most-Active Discussions"
labels = {'x':'Titles', 'y':'Comments'}
fig = px.bar(x=discussions_links, y=comments, title=title, labels=labels, hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()   
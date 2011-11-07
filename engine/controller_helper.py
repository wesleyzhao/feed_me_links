# helper functions for controller.py
import requests
import json

def get_hn_links(user_id = None):    
    HN_API_LINK = "http://api.ihackernews.com/page"
    r = requests.get(HN_API_LINK)
    page_json = json.loads(r.content)
    link_items = page_json['items']
    hn_links = [{
            'title' : link['title'], 
            'url' : link ['url'],
            'id' : link['id']
            } for link in link_items]
    return hn_links

def format_links_to_json(links_to_format):
    status_code = get_status_code(links_to_format)
    unformatted_json = {
        "status" : {
            "code" : status_code,
            "link_count" : len(links_to_format)
            },
        "links" : links_to_format
        }
    formatted = json.dumps(unformatted_json)
    return formatted

def get_status_code(the_links):
    if the_links:
        return "OK"
    else:
        return "NO"

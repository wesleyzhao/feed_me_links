# controller functions
from engine.controller_helper import *

def get_json_links_by_request(request):
    # first check if user is logged in
    # if user is logged in then get their links
    # otherwise aggregate all links
    
    links = []
    
    links.extend(get_hn_links())
    
    jsonified_links = format_links_to_json(links)
    return jsonified_links

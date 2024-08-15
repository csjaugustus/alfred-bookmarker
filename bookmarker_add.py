import sys
import json
import os
from search_algorithm import contains_chinese, pinyin_matched, fuzzy_search
from urllib.parse import urlparse

def get_base_url(url):
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    return base_url


query = sys.argv[1]
fuzz_value = int(os.environ["fuzz_value"])

with open("bookmarks.json", "r", encoding="utf-8") as f:
    bookmarks = json.load(f)

formatted_lst = []
exact_match_found = False

for k, v in bookmarks.items():
    if query == k:
        exact_match_found = True

    parsed_v = [get_base_url(x).strip(r"https://").strip(r"http://") for x in v]
    if len(v) > 1:
        subtitle = f"{len(v)} links"
    else:
        subtitle = v[0]

    if contains_chinese(query):
        if query in k:
            formatted_lst.append({
                                "title": k,
                                "subtitle" : subtitle,
                                "arg" : k,
                                "score": len(query) / len(k) * 100
                            })
        
        elif any(query in url for url in parsed_v):
            for url in parsed_v:
                if query in url:
                    formatted_lst.append({
                                        "title": k,
                                        "subtitle" : subtitle,
                                        "arg" : k,
                                        "score": len(query) / len(url) * 100
                                    })
    
    else:
        if fuzzy_search(query, k) or pinyin_matched(query, k):
            formatted_lst.append({
                                "title": k,
                                "subtitle" : subtitle,
                                "arg" : k,
                                "score": max(fuzzy_search(query, k), pinyin_matched(query, k))
                            })
    
        # for reverse searches
        elif any(fuzzy_search(query, url) for url in parsed_v):
            for url in parsed_v:
                if fuzzy_search(query, url):
                    if not any(d.get('title') == k for d in formatted_lst):
                        formatted_lst.append({
                            "title": k,
                            "subtitle" : subtitle,
                            "arg" : k,
                            "score": fuzzy_search(query, url)
                        })

formatted_lst.sort(key=lambda x: x['score'], reverse=True)

if not exact_match_found:
    formatted_lst.insert(0, {
            "title" : query,
            "subtitle" : "This will be added as a new entry.",
            "arg" : f"new||{query}",
            "icon" : {"path" : "bookmarker_new.png"}
        })
    

formatted_d = {"items" : formatted_lst}

data = json.dumps(formatted_d)

sys.stdout.write(data)

from linklens.infrastructure import http_client
from bs4 import BeautifulSoup
import json

ARCHIVE_URL = "https://dls2.iran-onemovies-dcenter.com/DonyayeSerial/donyaye_serial_all_archive.html"

search_name = "Game of Thrones"

import re

def normalize(text: str) -> str:
    return re.sub(r'\s+', '', text).lower()

def remove_leading_number(text: str) -> str:
    return re.sub(r'^\d+\.\s*', '', text)

with http_client.HTTPClient() as client :
    html = client.fetch_html(ARCHIVE_URL)
    
soup = BeautifulSoup(html, "html.parser")

h3 = None
name_tag = None

for tag in soup.find_all("h3"):
    name_tag = normalize(remove_leading_number(tag.text))
    if normalize(search_name) == name_tag :
        h3 = tag
        break
    
if h3 == None :
    print("Not found !")

else :
    print(f"Found : {h3.text.strip()}")
    current_tag = h3.find_next_sibling()
    
    series_data = {}
    while True :
        if current_tag is None or current_tag.name == "hr" :
            break
        
        if current_tag.name == "p" and current_tag.text.strip().lower().startswith("season") :
            season_name = current_tag.text.strip().lower().capitalize()
            
            next_p = current_tag.find_next_sibling("p")
            if next_p :
                
                for a in next_p.find_all("a") :
                    quality_text = a.get_text(strip=True)
                    quality_link = a["href"]
                    if season_name not in series_data :
                        series_data[season_name] = []
                    
                    series_data[season_name].append([quality_text, quality_link])
                                    
        current_tag = current_tag.find_next_sibling()
        
    print(json.dumps(series_data, indent=2, ensure_ascii=False))

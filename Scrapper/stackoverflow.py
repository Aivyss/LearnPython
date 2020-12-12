import requests
from bs4 import BeautifulSoup as bs
# https://stackoverflow.com/jobs?q=python&pg=5
URL="https://stackoverflow.com/jobs?c=KRW&d=20&q=python&sort=i&u=Km&so_source=JobSearch&so_medium=Internal&pg="

def extract_last_page():
    req = requests.get(URL+"1")
    html = bs(req.text, 'html.parser')

    all_anchor = html.find_all('a', {'class': 's-pagination--item'})
    print(all_anchor)
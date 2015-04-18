from app import app
from flask import render_template, Response, abort
from bs4 import BeautifulSoup
from requests import get
import re

@app.route('/api/<value>')
def get_website(value):
    val_dict = {
        "backers": "9000",
        "moni": "$9000",
        "goal": "$1"
    }
    if not value in val_dict.keys():
        abort(404)
    html = get("https://www.kickstarter.com/projects/nova-labs/nova-labs-v20-help-build-a-better-makerspace")
    soup = BeautifulSoup(html.text)
    val_dict["backers"] = "%s backers" % soup.find(itemprop="Project[backers_count]").text
    val_dict["moni"] = soup.find(itemprop="Project[pledged]").text
    val_dict["goal"] = "pledged out of %s" % soup.find(class_="money usd no-code").text
    return "%s" % (val_dict[value])

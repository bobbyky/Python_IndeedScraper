#!/usr/bin/python3

from flask import Flask, abort, request
from bs4 import BeautifulSoup
import requests
import json

app = Flask(__name__)

urls = []

@app.route('/', methods=['GET','POST'])
def foo():
    if not request.json:
        abort(400)
    info = request.json

    for a in range(len(info['jobs'])):
        url = (info['jobs'][a])
        urls.append(url)

    list = []
    # Iterates through each url in the list
    # For each job listing, print its title, location, company, and url
    for x in range(len(urls)):
        info = {}
        # Content of web page retrieved using get() function
        # Stored in variable page
        page = requests.get(urls[x])

        # Parse through the page using Python's built-in
        # HTML parser
        soup = BeautifulSoup(page.text, "html.parser")

        # Find the tags that correspond to
        # the job posting's title, location, company, and url.
        # Print each job posting's title, location, company, and url.
        job_title = soup.find(class_='jobtitle').get_text()
        info['title'] = job_title

        job_location = soup.find(class_='location').get_text()
        info['location'] = job_location

        job_company = soup.find(class_='company').get_text()
        info['company'] = job_company

        info['url'] = urls[x]
        list.append(info)

    return json.dumps(list, indent = 4)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
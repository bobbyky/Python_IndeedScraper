#!/usr/bin/python3

from flask import Flask, abort, request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import json

# create an instance of a web server
app = Flask(__name__)

# List used to store the list of urls passed through curl command
urls = []

@app.route('/', methods=['GET','POST'])
def find_job_info():
    if not request.json:
        abort(400)

    # info used to store information from -d (data) field of curl command
    info = request.json
    # list used to store each job listing's url
    url_list = []
    for a in range(len(info['jobs'])):

        # iterates through the curl command to find each url associated with the 'jobs' name
        url = (info['jobs'][a])
        urls.append(url)

        # Retrieve contents of job list page from indeed.com
        jobs = requests.get(urls[a])
        # URL linking to indeed.com page containing
        # list of jobs

        # list used to store URLs linking to job postings
        job_urls = []

        # Parse through the page using Python's built-in
        # HTML parser
        job_soup = BeautifulSoup(jobs.text, "html.parser")
        # Find the tags that correspond to
        # each job listings' url,
        # store the url of the job in job_url and append it
        # to the list of job urls
        job_tbl = job_soup.find(id = "resultsCol")

        # iterates through job_tbl to find all elements with the corresponding
        # name and attribute, job_url is the url of each individual job listing
        for link in job_tbl.find_all('a', attrs = {'data-tn-element' : 'jobTitle'}):
            job_url = urljoin(urls[a], link.attrs["href"])
            job_urls.append(job_url)
        url_list.extend(job_urls)

    # list used to store the information scraped from each job listing
    info_list = []

    # Iterate through each url in job_urls
    # For each job listing, print its title, location, company, and url
    for x in range(len(url_list)):
        info = {}
        # Content of web page retrieved using get() function
        # Stored in variable job_page
        job_page = requests.get(url_list[x])

        # Parse through the page using Python's built-in
        # HTML parser
        soup = BeautifulSoup(job_page.text, "html.parser")

        # Find the tags that correspond to
        # the job posting's title, location, company, and url.
        # Print each job posting's title, location, company, and url.
        job_title = soup.find(class_='jobtitle').get_text()

        info['title'] = job_title

        job_location = soup.find(class_='location').get_text()
        info['location'] = job_location

        job_company = soup.find(class_='company').get_text()
        info['company'] = job_company

        info['url'] = url_list[x]

        info_list.append(info)

    return json.dumps(info_list, indent=4)

# start the web server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


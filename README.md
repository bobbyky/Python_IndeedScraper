# Python_IndeedScraper
A web server written in python that scrapes job listings from Indeed and returns the job titles, locations, and company names. Built using flask, BeautifulSoup, requests, urljoin and json modules.

**Project: Web Scraper**

**Instructions:**
*Write a web server that scrapes job listings from Indeed and returns the job titles, locations, and company names.* 

**Python_indeedScraperURL.py**:

Interpretation: Given a list of URLs linking to job listings from indeed.com, return the job title, location, company name, and url for each listing.

*Command Line Input:* curl -i -H "Content-Type: application/json" -X POST -d '{"jobs":["http://www.indeed.com/viewjob?jk=8cfd54301d909668","http://www.indeed.com/viewjob?jk=b17c354e3cabe4f1","http://www.indeed.com/viewjob?jk=38123d02e67210d9"]}' http://localhost:5000/

*Output:* 
![My image](https://github.com/bobbyky/IndeedWebScraper/blob/master/Images/out3.JPG)


**Python_indeedScraperPage.py**:

Interpretation: Given a list of URLs linking to a page of job listings from indeed.com, create a list of URLs from each page. With the list of URLs return the job title, location, company name, and url for each listing for each job listing.

*Command Line Input:* curl -i -H "Content-Type: application/json" -X POST -d '{"jobs":["https://www.indeed.com/jobs?q=accountant&l=San+Francisco%2C+CA","https://www.indeed.com/jobs?q=data+scientist&l=San+Diego%2C+CA"]}' http://localhost:5000/

*Output:*
![My image](https://github.com/bobbyky/IndeedWebScraper/blob/master/Images/a.JPG)
![My image](https://github.com/bobbyky/IndeedWebScraper/blob/master/Images/b.JPG)
![My image](https://github.com/bobbyky/IndeedWebScraper/blob/master/Images/c.JPG)

**Please note that not all job listing pages from indeed.com will work with this program, job listing pages that include "Indeed Prime" job listings can't be used with Python_indeedScraperPage.py**

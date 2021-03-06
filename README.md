## Site Quality Crawler

A tool that crawls a website and reports the HTTP response codes and redirects for each link.
The results will be displayed as a dynamic site map.

### Contributors
* Matt McGraw
* Mateusz Bocian

### Running Crawler

Run this command and swap out "http://www.xyz.com" with the full destination of the site you want to analyze.
	Root is the root of the URL you want to continue scraping.  Anything without this root URL will be ignored.
	Start is the page you want to begin the crawl at.
	Limit is the maximum number of pages to crawl.
```
python3 -m crawler.crawler --root="http://www.xyz.com" --start="http://www.xyz.com" --limit=5
```

### Running Visualization

You must run the crawler at least once to have a visualization.  After you've crawled once you'll be able to run the server on your localhost and choose reports from any of the crawling sessions that you've previously kept in your "/reports/" folder.
```
python3 -m server
```

### Testing

Should you want to test the application please run this command.  Most tests are self-contained but a few do require an internet connection to test requests.
```
python3 -m unittest discover -p "test_*.py"
```

### Requirements
This project requires the use of Flask (http://flask.pocoo.org/, BSD License), Requests (http://docs.python-requests.org/en/latest/, Apache2 License), and BeautifulSoup (http://www.crummy.com/software/BeautifulSoup/, MIT License).  We use these libraries in their native form, without modification.

### License

This project is licensed under a two-clause BSD License.  Please see the LICENSE file for details.
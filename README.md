## Site Quality Crawler

A tool that crawls a website and reports the HTTP response codes and redirects for each link.
The results will be displayed as a dynamic site map.

### Contributors

Matt McGraw
Mateusz Bocian

### Running Crawler
```
python -m server
```
Note: still using old python until I figure out venv

### Running Crawler
```
python3 -m crawler.crawler
```

### Testing
```
python3 -m unittest discover -p "test_*.py"
```
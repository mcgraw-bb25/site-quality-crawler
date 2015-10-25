/*
This file shows the final output of a mock object which represents the Site Report.
The Site Report will contain many page reports at the end of a crawling session.
It will be represented as a json object to later be processed by Site Report Processor.
The Site Report Processor will spit out something that can be passed to a browser
and visualized in D3.js or something like it...
*/

SiteReportObject = 
{
	"site_name_id" : "mysite.com",
	"site_entry_url" : "http://www.mysite.com",
	"site_url_map" : 
		[
			{PageReport1},
			{PageReport2},
			{PageReport3},
			{PageReport4}
		] 
}

PageReportURL1 = {
	"url" : "http://www.mysite.com",
	"status_code" : 200,
	"redirects" : [],
	"page_links" : ["http://www.mysite.com/aboutus/", 
					"http://www.mysite.com/login/", 
					"http://www.mysite.com/products"]
}

PageReportURL2 = {
	"url" : "http://www.mysite.com/aboutus/",
	"status_code" : 200,
	"redirects" : ["http://www.mysite.com/about/"],
	"page_links" : ["http://www.mysite.com"]
}

PageReportURL3 = {
	"url" : "http://www.mysite.com/login/",
	"status_code" : 200,
	"redirects" : [],
	"page_links" : []
}

PageReportURL4 = {
	"url" : "http://www.mysite.com/products/",
	"status_code" : 404,
	"redirects" : [],
	"page_links" : []
}
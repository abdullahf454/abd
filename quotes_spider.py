# importing scrapy module 
import scrapy 


class ExtractUrls(scrapy.Spider): 
	
	# Name of the spider 
	crawled = set() 
	
	# Set to avoiding duplicate url 
	name = "extract"

	def start_requests(self): 

		# Starting url mentioned 
		urls = ['http://www.geeksforgeeks.org', ] 
		for url in urls: 
			yield scrapy.Request(url = url, 
					callback = self.parse) 

	def parse(self, response): 
		title = response.css('title::text').extract_first() 
		links = response.css('a::attr(href)').extract() 
		for link in links: 
			yield
		{ 
			'title': title, 
			'links': link 
		} 

		if ('geeksforgeeks' in link and
			link not in self.crawled): 
			self.crawled.update(link) 
			yield scrapy.Request(url = link, 
					callback = self.parse) 

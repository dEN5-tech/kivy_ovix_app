from __future__ import unicode_literals
import requests
import time
from bs4 import BeautifulSoup
from random import  randint,choice
from fake_headers import Headers
import json
from lxml import html
from itertools import groupby
from datetime import datetime

def get_html(site):
	"""Summary
	
	Args:
		site (TYPE): Description
	
	Returns:
		TYPE: Description
	"""
	r = requests.get(site)
	return r.text


def get_page_data(html):
	"""Summary
	
	Args:
		html (TYPE): Description
	
	Returns:
		TYPE: Description
	"""
	soup = BeautifulSoup(html, 'html.parser')
	line = soup.find('table', id='theProxyList').find('tbody').find_all('tr')
	pb = []
	for index, tr in enumerate(line, 1):
		
		td = tr.find_all('td')
		ip = str(td[1].text)
		port = str(td[2].text)
		country = str(td[3].text.strip())
		anonym = str(td[4].text.strip())
		types = str(td[5].text.strip())
		time = td[6].text
		if time < "0.2"and not country.startswith("Росс"):
			proxy = {f"{types.lower()}": f"{ip}:{port}"}
			pb.append(proxy)
	proxies = choice(pb)
	print(proxies)
	return proxies



def mainpr():
	"""Summary
	
	Returns:
		TYPE: Description
	"""
	return get_page_data(get_html('http://foxtools.ru/Proxy'))

import requests
from fake_headers import Headers
from bs4 import BeautifulSoup as bs4
import re
link = "https://steamcommunity.com/sharedfiles/filedetails/?id=2070583974"
def searcher_steam(link):
	r = requests.get(link,headers=Headers().generate(),proxies=mainpr()).content

	soup = bs4(r,"lxml")
	soup = soup.find("div",id="mainContents")
	title = soup.find("div", class_="workshopItemTitle").text
	reting_section = soup.find("div", id="detailsHeaderRight") 
	main_photo = soup.find("div",id="highlight_strip_bg")
	commentthread_area = soup.find("div",class_="commentthread_area")
	stats_table = soup.find("table",class_="stats_table",recursive=True)
	xp = html.fromstring(str(soup))
	fileRatingDetails = xp.xpath('//*[@id="detailsHeaderRight"]/div/div[1]/img/@src')[0]
	list_screenshot = html.fromstring(str(main_photo)).xpath("//div[@class='highlight_strip_item highlight_strip_screenshot']/img/@src")
	list_preview = html.fromstring(str(main_photo)).xpath("//div[@class='highlight_strip_item highlight_strip_movie']/img/@src")
	list_images = list_preview+list_screenshot
	list_info_table = stats_table.text.strip("\n").split("\n")
	soup2 = bs4(str(commentthread_area),"lxml")
	responsive_body_text = soup2.findAll("div",id=re.compile(r"comment_.*"))
	commentthread = []
	for i in responsive_body_text:
		try:
			profile = html.fromstring(str(i)).xpath("//div[2]/div[1]/a/@href")
			name = html.fromstring(str(i)).xpath("//div[2]/div[1]/a/bdi/text()")
			text = html.fromstring(str(i)).xpath("//div[@class='commentthread_comment_text']/text()")[0].strip()
			timestamp = datetime.utcfromtimestamp(int(html.fromstring(str(i)).xpath("//div[2]/div[1]/span/@data-timestamp")[0].strip())).strftime('%Y-%m-%d %H:%M:%S')
			commentthread.append({"profile":profile,"name":name,"text":text,"timestamp":timestamp})
		except:
			pass

	list_main = {"list_images":list_images,"list_info_table":list_info_table,"comment_thread":comment_thread}
	return list_main





from plyer import notification
from bs4 import BeautifulSoup
import requests
import time

def notifyMe(title, message):
	notification.notify(
			title= title,
			message = message,
			app_icon = "C://Users//risha//Desktop//WebScraping//coronafinal.ico",
			timeout = 10
		)

def getData(url):
	r = requests.get(url)
	return r.text

if __name__=="__main__":
	while True:
		data = getData("https://www.mohfw.gov.in")
		soup = BeautifulSoup(data, "lxml")
		datastr=""
		for tr in soup.find_all('tbody')[7].find_all("tr"):
			datastr += tr.get_text()
		datastr = datastr[1:]
		itemlist = datastr.split("\n\n")

		states = ["Punjab", "Delhi", "Chandigarh"]
		for item in itemlist[0:24]:
			datalist = item.split("\n")
			if datalist[1] in states:
				nTitle = "Cases of Covid-19"
				nText = f"State: {datalist[1]}\nIndian: {datalist[2]}\nForeign: {datalist[3]}\nCured: {datalist[4]}\nDeaths: {datalist[5]}"
				notifyMe(nTitle, nText)
				time.sleep(2)
		time.sleep(3600)
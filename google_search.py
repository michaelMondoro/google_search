import bs4 as bs
import requests

class GoogleSearch():
    soup = None
    def __init__(self):
        self.url = "https://www.google.com/search?q="
        self.results = []
        self._headers = {'User-Agent': 'My User Agent 1.0'}
        self.soup = None
    def search(self, query):
        res = requests.get(self.url + query, headers=self._headers)
        self.soup = bs.BeautifulSoup(res.content, 'html.parser')

        result_class = "Gx5Zad"
        title_class = "vvjwJb"
        href_class = "kCrYT"
        desc_class = "BNeawe"

        items = self.soup.find_all("div",{"class":result_class})
        items = items[1:len(items)-2]

        results = []
        for i in items:
            title, href, desc = ("",)*3
            if i.find("div",{"class":title_class}):
                title = i.find("div",{"class":title_class}).text
            if i.find("div",{"class":href_class}) and i.find("div",{"class":href_class}).find("a"):
                href = i.find("div",{"class":href_class}).find("a")['href'].strip("/url?q=")
            # if i.find("div",{"class":[desc_class]}):
            #     desc = i.find("div",{"class":desc_class}).text
            i.find("div",class_ = "BNeawe s3v9rd AP7Wnd")
            
            if title != "":
                results.append({"title":title,"href":href,"desc":desc})
                
        self.results = results
        return results

google = GoogleSearch()
a = google.search("the notorious B.I.G")

for i in a:
    print(i)
    print()
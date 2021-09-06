from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import requests

# 美食抽象類別
class Food(ABC):

    def __init__(self, area,category):
        self.area = area  # 地區
        self.category = category  # 美食類別


    @abstractmethod #抽象方法(abstractmethod)就是共同的介面,多型態實用爬蟲,方便後續擴充
    def scrape(self):
        pass


# 愛食記爬蟲
class IFoodie(Food):


    def scrape(self):
        response = requests.get(
            "https://ifoodie.tw/explore/" + self.area + 
            "/list/"+self.category+
            "?opening=true&sortby=popular")


        soup = BeautifulSoup(response.content,  "html.parser")

        cards = soup.find_all(
             'div', {'class': 'jsx-3440511973 restaurant-info'}, limit=10)
        
        content = ""
        for card in cards:
        
            title = card.find(
                "a", {"class": "jsx-3440511973 title-text"}).getText()
            
            stars = card.find(#餐廳評價
                "div", {"class": "jsx-1207467136 text"}).getText()
            
            address = card.find(  # 餐廳地址
                "div", {"class": "jsx-3440511973 address-row"}).getText()


            #將取得的餐廳名稱、評價及地址連結一起，並且指派給content變數
            content += f"{title} \n{stars}顆星 \n{address} \n\n"
        
        return content
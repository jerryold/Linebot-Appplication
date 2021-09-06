---
tags: Linebot
---

# FoodLinebot
## Description
* 本次Linebot以Django框架進行開發，以知名網站知名美食網站愛食記為例，爬取其中的餐廳資訊，根據使用選擇地區和種類需求，爬取某地區前五名最高人氣且營業中的餐廳資訊
![](https://i.imgur.com/Q1jGoa7.jpg)

## Linebot設置
* 將這個頻道(Channel)與自己開發的應用程式連結，所以其中有兩個憑證會使用到，如下：
    * Channel secret(頻道密碼)：位於Basic settings頁籤中，如下圖：
    ![](https://i.imgur.com/aA0jxc4.png)
    * Channel access token(頻道憑證)：位於Messaging API頁籤中，要按下右方的「Issue」按鈕才會出現，如下圖：
    ![](https://i.imgur.com/Xx9UhHY.png)

* 開啟專案主程式下的settings.py檔案，增加LINE Developers上所取得的兩個憑證設定，來與LINE頻道(Channel)進行連結，如下範例：
    ![](https://i.imgur.com/SCe3Uxc.png)
    
* 在INSTALL_APPS的地方，加上剛剛所建立的Django應用程式(APP)，如下範例：
    ![](https://i.imgur.com/cPxKojf.png)

## Deploy
### 本機端
* 透過Ngrok，將本機的埠號對外公開，為例，Django在本機運行的埠號為8000
>     ngrok http 8000
![](https://i.imgur.com/TER0OJs.png)
* Ngrok就會隨機產生一個HTTPS的網址，只要把這個網址填入LINE Webhook URL，以及LINE Bot應用程式(APP) settings.py檔案中的ALLOWED_HOSTS，如下範例，LINE頻道(Channel)就能夠與LINE Bot應用程式(APP)互相連結：如下圖
![](https://i.imgur.com/H5gpP0A.png)


### Heroku
*　請先確保已經在 Heroku 上新增一個 App，並透過 git remote 指令將檔案與雲端專案連結。
    *　透過以下指令部署至 Heroku，push 成功後，Heroku 會去找我們的 Procfile ，透過 Procfile 內的指令來了解該如何啟動程式。
```
$ git add .  #加入所有變更的程式碼檔案到本地端Git Repository

$ git commit -m "your_message"  #儲存到硬碟中

$ heroku git:remote -a foodielinebot  #將Heroku雲端平台的Git Repository切換到LINE Bot的應用程式

$ git push heroku master  #推送到Heroku雲端平台的LINE Bot應用程式Git Repository
```

## How To Use
* 請掃下方QR Code加入好友

![](https://i.imgur.com/XdfxGcJ.png)
* 加入好友即可和FoodLine進行對話,並輸入關鍵字"哈囉",則可開始查詢，如下圖範例
![](https://i.imgur.com/gVfehZy.png)

## File Structure

```
FoodLinebot

├── Procfile:利用gunicorn伺服器，執行Django專案中的wsgi(web server gateway interface)檔案，來進行溝通。
├── README.md
├── manage.py
├── requirments.txt:架設heroku需要安裝套件環境
│   ├── foodlinebots
│   │   ├── migrations
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── scraper.py:進入愛食記網站爬蟲
│   │   ├── tests..py
│   │   ├── urls.py
│   │   ├── views.py:控制linebot的callback function動作
│   ├── mylinebot
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py:設置linebot token和static路徑
│   │   ├── urls.py
│   │   ├── wsgi.py

```

## Demo
https://user-images.githubusercontent.com/12774427/132226527-53e851e6-8f4c-4878-85ca-120191edbadc.mp4



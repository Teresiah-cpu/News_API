from email.mime import image
from http import client
from flask import Flask, render_template,request,redirect,url_for
from newsapi import NewsApiClient
# from app import app
app = Flask (__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bbc') 
def bbc(): 
#     api_key="9b1bbde4ec434625802e9867ef0aa86d"
#     topheadlines =api_key.get_top_headlines(sources="News24")  
    newapi = NewsApiClient(api_key="9b1bbde4ec434625802e9867ef0aa86d")
    topheadlines =newapi.get_top_headlines(sources="News24"
)
    articles =topheadlines['articles'] 
    news = []
    description = []
    link = []
    image = []
    time = []
    content = []

    for i in range(len(articles)):
        myarticles =articles[i]
        news.append(myarticles['title'])
        description.append(myarticles['description'])
        link.append(myarticles['url'])
        image.append(myarticles['urlToImage'])
        time.append(myarticles['publishedAt'])
        content.append(myarticles['content'])
        
        my_list =zip( news,description,link,image,time,content)


    return render_template('bbc.html',context=my_list)



@app.route('/google') 
def google():  
    # api_key="9b1bbde4ec434625802e9867ef0aa86d"
    # topheadlines =api_key.get_top_headlines(sources="IGN") 
    newapi = NewsApiClient(api_key="9b1bbde4ec434625802e9867ef0aa86d")
    topheadlines =newapi.get_top_headlines(sources="IGN"
)
    articles =topheadlines['articles'] 
    news = []
    description = []
    link = []
    image = []
    time = []
    content = []

    for i in range(len(articles)):
        myarticles =articles[i]
        news.append(myarticles['title'])
        description.append(myarticles['description'])
        link.append(myarticles['url'])
        image.append(myarticles['urlToImage'])
        time.append(myarticles['publishedAt'])
        content.append(myarticles['content'])
        

        my_list =zip( news,description,link,image,time,content)


    return render_template('google.html',context=my_list)


@app.route('/cnn') 
def cnn():   
    # api_key="9b1bbde4ec434625802e9867ef0aa86d"
    # topheadlines =api_key.get_top_headlines(sources="CNN")

    newapi = NewsApiClient(api_key="9b1bbde4ec434625802e9867ef0aa86d")
    topheadlines =newapi.get_top_headlines(sources="CNN"
)
    articles =topheadlines['articles'] 
    news = []
    description = []
    link = []
    image = []
    time = []
    content = []

    for i in range(len(articles)):
        myarticles =articles[i]
        news.append(myarticles['title'])
        description.append(myarticles['description'])
        link.append(myarticles['url'])
        image.append(myarticles['urlToImage'])
        time.append(myarticles['publishedAt'])
        content.append(myarticles['content'])
        
        my_list =zip( news,description,link,image,time,content)


    return render_template('cnn.html',context=my_list)



if __name__ == '__main__':
    app.run()
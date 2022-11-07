import requests
from myapp.models import PostModel



def get_news_article(url):
    try:
        data = requests.get(url)
        data = data.json()
        if data.get('articles'):
            for article in data.get('articles'):
                source = article.get('source').get('name')
                author = article.get('author')
                title = article.get('title')
                description = article.get('description')
                content = article.get('content')
                url = article.get('url')
                urlToImage = article.get('urlToImage')
                publishedAt = article.get('publishedAt')

                PostModel.objects.create(
                    source=source,
                    title=title,
                    author=author,
                    description=description,
                    publishedAt=publishedAt,
                    content=content,
                    url=url,
                    urlToImage=urlToImage
                )
    except Exception as e:
        print(e)
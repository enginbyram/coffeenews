import newspaper
import json
import nltk

nltk.download('punkt')

# birgun_news = newspaper.build('http://birgun.net')
sozcu_news = newspaper.build('http://www.sozcu.com.tr', memoize_articles=False, language='tr')
# hurriyet_news = newspaper.build('http://www.hurriyet.com.tr')
# akit_news = newspaper.build('http://www.yeniakit.com.tr')


# articleAuthors = article.authors
# articleDate = article.publish_date
# articleKeywords = article.keywords
# articleSummary = article.summary
# articleText = article.fulltext

i=0
for article in sozcu_news.articles:
    article.download()
    article.parse()
    article.nlp()
    print(article.title)
    json_dict = {
        "article_title": article.title,
        "article_authors": article.authors,
        "article_date": article.publish_date,
        "article.keywords": article.keywords,
        "article_text": article.text,
        "article_source": sozcu_news.brand
    }

    with open(f"bin/{sozcu_news.brand}-{i}.json", "w", encoding='utf8') as write_file:
        json.dump(json_dict, write_file, ensure_ascii=False)
    i += 1
    print(f"{sozcu_news.brand}-{i}.json created...")

    if i >=5:
        break



from mezzanine import template

from ecms.constants import NUM_ARTICLE_PAGES

register = template.Library()

@register.simple_tag
def display(val):
    print val.topic_page
    print type(val)
    return ""

@register.filter
def should_clear(val):
    clear = not ((val + 1) % 3)
    return clear

@register.filter
def home_gallery_articles(topic_pages):
    gallery_articles = []
    for topic_page in topic_pages:
        article_pages = topic_page.topicpage.get_article_pages() or []
        for article_page in article_pages:
            gallery_articles.append(article_page)
            if len(gallery_articles) >= NUM_ARTICLE_PAGES:
                return gallery_articles
    return gallery_articles

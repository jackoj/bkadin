from ecms.models import TopicPage

def main():
    print TopicPage.objects.get(id=4).get_article_pages()

if __name__ == '__main__':
    from django.core.management import setup_environ
    from django.contrib.auth.models import User
    import settings
    setup_environ(settings)
    main()

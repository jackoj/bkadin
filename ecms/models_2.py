from ecms.models import TopicPage

def main():
    print TopicPage.objects.all()

if __name__ == '__main__':
    from django.core.management import setup_environ
    from django.contrib.auth.models import User
    import settings
    setup_environ(settings)
    main()

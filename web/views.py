from django.utils import timezone
from django.views.generic import ListView

from news.models import Event, Article
from itertools import chain


class Home(ListView):
    template_name = 'web/index.html'

    def get_queryset(self):
        articles = Article.objects.filter(published=True).exclude(id__in=Event.objects.all())
        events = Event.objects.filter(end_date__gt=timezone.now())
        return sorted(chain(articles, events), key=lambda o: o.datetime_published)

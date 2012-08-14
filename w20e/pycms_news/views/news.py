from repoze.catalog.query import Eq
from pyramid.url import resource_url
from w20e.pycms.views.base import ContentView
from w20e.pycms_news.interfaces import INews


class NewsListingMixin:
    
    def listnews(self):

        cat = self.context.root._catalog

        res = cat.query(Eq('nature', "w20e.pycms_news.interfaces.INews"))

        objs = []

        for result in res[1]:
            obj = cat.get_object(result)
            
            objs.append({"title": obj.title,
                         "date": obj.created.strftime('%d-%m-%Y'),
                         "sortdate": obj.created.strftime('%Y%m%d'),
                         "url": resource_url(obj, self.request),
                         "text": obj.full_text})

        def newest_sort(a, b):

            return cmp(b['sortdate'], a['sortdate'])

        objs.sort(newest_sort)
                
        return objs


class NewsViewlet(object, NewsListingMixin):

    """ Fetch news and provide to viewlet"""

    def __init__(self, context, request):

        self.context = context
        self.request = request

        self.limit = self.request.get('kwargs', {}).get('limit', 5)
        self._news = self.listnews()

    def __call__(self):

        return {}

    @property
    def news(self):

        return self._news[:self.limit]

    @property
    def has_more_news(self):

        return len(self._news) > self.limit


class NewsView(ContentView):

    @property
    def date(self):
        return self.context.created.strftime('%d-%m-%Y')


class NewsListingView(ContentView, NewsListingMixin):

    pass

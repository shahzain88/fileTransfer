from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewSitemap(Sitemap):

    def items(self):
        return ['accounts.login', 'logout', 'articles', 'shoukai', 'contact', '404', 'manifest', 'robots']

    def location(self, item):
        return reverse(item)

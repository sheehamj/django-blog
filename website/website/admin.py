from django.contrib import admin

from website.blog.models import Entry

from website.blog.admin import EntryAdmin



from website.links.models import Link

from website.links.admin import LinkAdmin



class AdminSite(admin.AdminSite):

    pass



site = AdminSite()

site.register(Entry, EntryAdmin)

site.register(Link, LinkAdmin)


from django.views.generic.list_detail import object_list



from tagging.models import Tag

from blog.models import Entry



def tag_detail(request):


	tag = Tag.objects.get()

	qs = Tag.objects.all()

	return object_list(request, queryset=qs, template_name='about/list.html')


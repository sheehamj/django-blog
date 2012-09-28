from django.views.generic.list_detail import object_list



from tagging.models import Tag,TaggedItem

from blog.models import Entry



def tag_detail(request):



	tag = Tag.objects.get()

	qs = TaggedItem.objects.get_by_model(Entry, tag)

	return object_list(request, queryset=qs, template_name='main/list.html')






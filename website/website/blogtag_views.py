from django.views.generic.list_detail import object_list



from tagging.models import Tag,TaggedItem

from blog.models import Entry

from website.blog.models import Entry

from tagging.views import tagged_object_list



def tag_detail(request):

	qs = Tag.objects.all()

	return object_list(request, queryset=qs, template_name='tags/list.html')




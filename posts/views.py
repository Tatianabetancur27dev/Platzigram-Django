from django.http import HttpResponse

# Create your views here.

#
def list_post(request):
	"""List exiting post"""
	posts = [1,2,3]
	return HttpResponse(str(posts))

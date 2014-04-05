from django import template
register = template.Library()

@register.simple_tag
def tabactive(url, request):

    import re
    print type(request)
    if re.search(url, request.path):
        return 'active'
    else:
    	if url == "index" and re.match("^/$", request.path):
    		return 'active'
    	else:
        	return 'inactive'

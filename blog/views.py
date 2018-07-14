from django.shortcuts import render
from django.shortcuts import render_to_response
from datetime import datetime
from blog.models import BlogPost

# Create your views here.
# def archive(request):
#     post = BlogPost(title='mocktitle', body='mokbody', timestamp=datetime.now())
#     return render_to_response('archive.html', {'posts': [post]})
#
# def foo(request):
#     post = BlogPost(title='mocktitle', body='mokbody', timestamp=datetime.now())
#     return render_to_response('archive.html', {'posts': [post]})

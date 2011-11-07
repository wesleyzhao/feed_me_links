# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context,loader,RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib import auth
from engine.models import *
from engine.controller import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
STATIC_URL = '/static/'

def links(request):
    json_links = get_json_links_by_request(request)
    return HttpResponse(json_links)

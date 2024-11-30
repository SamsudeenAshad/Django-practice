

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  template = loader.get_template('myfirst.html')
  rendered_template = template.render()
  
  mymembers = Member.object.all().values()  
  template1 = loader.get_template('all_members.html')
  context1 = {
      'mymembers' : mymembers,
  }
  
  rendered_template1 = template1.render(context1, request)

  
  
  return HttpResponse(rendered_template)
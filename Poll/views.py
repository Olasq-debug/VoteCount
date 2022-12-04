from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import AnnouncedPuResults
from django.db import connections

# Create your views here.

class PostList(ListView):
    model = AnnouncedPuResults
    template_name = 'Poll/ListPoll.html'
    context_object_name = 'posts'
    

class PartyResultList(CreateView):
    model = AnnouncedPuResults
    fields = ['result_id', 'polling_unit_uniqueid', 'party_abbreviation', 'party_score', 'entered_by_user', 'date_entered', 'user_ip_address']
    template_name = 'Poll/PartyResult.html'
    context_object_name = 'form'

def PostList2(request):
   data = AnnouncedPuResults.objects.filter()
    


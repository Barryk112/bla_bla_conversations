from django.shortcuts import render
from django.views import generic
from .models import ConversationPost


class ConversationList(generic.ListView):

    template_name = 'index.html'
    model = ConversationPost

    # Gets the list of Conversation posts and displays only the appproved ones
    queryset = ConversationPost.objects.filter(status=1).order_by('-created_on')
    paginate_by = 15

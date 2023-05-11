from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import ConversationPost


class ConversationList(generic.ListView):

    template_name = 'index.html'
    model = ConversationPost

    # Gets the list of Conversation posts and displays only the appproved ones
    queryset = ConversationPost.objects.filter(status=1).order_by('-created_on')
    paginate_by = 15


class ConversationDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = ConversationPost.objects.filter(status=1)
        conversation = get_object_or_404(queryset, slug=slug)
        comments = conversation.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if conversation.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "conversation_detail.html",
            {
                "conversation": conversation,
                "comments": comments,
                "liked": liked
            },
        )
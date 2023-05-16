from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import ConversationPost
from .forms import CommentForm, ConversationForm
from django.utils.text import slugify



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
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = ConversationPost.objects.filter(status=1)
        conversation = get_object_or_404(queryset, slug=slug)
        comments = conversation.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if conversation.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(request.POST)

        # Checks if comment is valid and saves it
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = conversation
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "conversation_detail.html",
            {
                "conversation": conversation,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": comment_form
            },
        )


class ConversationLike(View):

    def post(self, request, slug):
        conversation = get_object_or_404(ConversationPost, slug=slug)

        if conversation.likes.filter(id=request.user.id).exists():
            conversation.likes.remove(request.user)
        else:
            conversation.likes.add(request.user)

        # Reloads page once like is clicked to update
        return HttpResponseRedirect(reverse('conversation_detail', args=[slug]))


class NewConversationPost(View):

    def get(self, request):
        return render(
            request,
            "new_conversation.html",
            {
                "conversation_form": ConversationForm()
            },
        )

    def post(self, request, *args, **kwargs):
        conversation_form = ConversationForm(request.POST, request.FILES)
        if conversation_form.is_valid():
            conversation_post = conversation_form.save(commit=False)
            conversation_post.author = request.user
            conversation_post.slug = slugify(conversation_post.title)
            conversation_post.save()
            return redirect('home')
        else:
            # pass the form with errors to the template
            return render(request, 'new_conversation.html', {'conversation_form': conversation_form})


class EditConversationPost(View):
    def get(self, request, slug):
        # Gets the current conversation post
        conversation = get_object_or_404(ConversationPost, slug=slug, author=request.user)
        # Populates the form with the current conversation details
        conversation_form = ConversationForm(instance=conversation)
        return render(request, 'edit_conversation.html', {
            'conversation': conversation,
            'conversation_form': conversation_form,
        })

    def post(self, request, slug):
        conversation = get_object_or_404(ConversationPost, slug=slug, author=request.user)
        conversation_form = ConversationForm(request.POST, instance=conversation)
        if conversation_form.is_valid():
            conversation_form.save()
            return redirect('conversation_detail', slug=conversation.slug)
        else:
            return render(request, 'edit_conversation.html', {
                'conversation': conversation,
                'conversation_form': conversation_form,
            })


class DeleteConversationPost(View):
    def get(self, request, slug):
        conversation = get_object_or_404(ConversationPost, slug=slug, author=request.user)
        conversation_form = ConversationForm(instance=conversation)
        return render(request, 'delete_conversation.html', {
            'conversation': conversation
        })

    def post(self, request, slug):
        conversation = get_object_or_404(ConversationPost, slug=slug, author=request.user)
        conversation.delete()
        return redirect('home')
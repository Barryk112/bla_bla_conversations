from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# For ConversationPost Model, status for a post id draft of published
STATUS = ((0, "Draft"), (1, "Published"))

# Model for a conversation post
class ConversationPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="conversation_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='conversation_like', blank=True)

    # Orders the posts in decending order
    class Meta:
        ordering = ['-created_on']

    # Returns the number of likes on a post
    def number_of_likes(self):
        return self.likes.count()

    # Returns the object as a string (Django recommends having this)
    def __str__(self):
        return self.title


# Model for a comment
class Comment(models.Model):
    post = models.ForeignKey(ConversationPost, on_delete=models.CASCADE, related_name="conversation_comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False) # This is so comments must be approved before they are published

    # Orders the comments in order
    class Meta:
        ordering = ["created_on"]

    # Returns comment and by who
    def __str__(self):
        return f"Comment {self.body} by {self.name}"

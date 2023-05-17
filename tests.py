from django.test import TestCase, Client
from django.urls import reverse
from conversations.models import ConversationPost
from django.contrib.auth.models import User



class ConversationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.conversation = ConversationPost.objects.create(title='Test Conversation', content='This is a test conversation.', author=self.user)

    def test_conversation_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

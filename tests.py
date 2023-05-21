from django.test import TestCase, Client
from django.urls import reverse
from conversations.models import ConversationPost
from django.contrib.auth.models import User



class ConversationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.conversation = ConversationPost.objects.create(
            title='Test Conversation',
            content='This is a test conversation post.',
            author=self.user,
            status=1,
            slug='test-conversation'
        )

    def test_conversation_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_conversation_detail(self):
        response = self.client.get(reverse('conversation_detail', args=[self.conversation.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'conversation_detail.html')
        self.assertContains(response, self.conversation.title)
        self.assertContains(response, self.conversation.content)

    def test_new_conversation(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('new_conversation'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_conversation.html')

    def test_edit_conversation(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('edit_conversation', args=[self.conversation.slug]), {
            'title': 'Updated Conversation',
            'content': 'This is the updated content.',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_conversation.html')

    def test_delete_conversation_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('delete_conversation', args=[self.conversation.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_conversation.html')

        # Ensure the post is deleted
        response = self.client.post(reverse('delete_conversation', args=[self.conversation.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(ConversationPost.objects.filter(pk=self.conversation.pk).exists())
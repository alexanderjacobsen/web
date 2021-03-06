from django.contrib.auth.models import User, Permission
from django.test import TestCase
from django.urls import reverse

from contentbox.models import ContentBox, DisplayContentBoxView


class ModelTestCase(TestCase):
    def test_str(self):
        contentbox = ContentBox.objects.create(title='TEST_TITLE')
        self.assertEqual(contentbox.title, 'TEST_TITLE')
        self.assertEqual(contentbox.title, str(contentbox))

    def test_get(self):
        self.assertEqual(ContentBox.objects.count(), 0)
        contentbox = ContentBox.get(title='TEST_TITLE')
        self.assertEqual(ContentBox.objects.count(), 1)
        self.assertEqual(contentbox.title, 'TEST_TITLE')

        contentbox2 = ContentBox.get(title='TEST_TITLE')
        self.assertEqual(ContentBox.objects.count(), 1)
        self.assertEqual(contentbox, contentbox2)

    def test_display_view(self):
        view = DisplayContentBoxView()
        view.title = 'TEST_TITLE'
        context = view.get_context_data()
        self.assertTrue('contentbox' in context)
        self.assertEqual(context['contentbox'].title, 'TEST_TITLE')

    def test_edit_without_permission(self):
        ContentBox.get(title='TEST_TITLE')
        response = self.client.get(reverse('contentbox-edit', args=(1,)))
        self.assertNotEqual(response.status_code, 200)

    def test_edit_with_permission(self):
        username = 'TEST_USER'
        password = 'TEST_PASS'
        user = User.objects.create_user(username=username, password=password)
        permission = Permission.objects.get(codename='change_contentbox')
        user.user_permissions.add(permission)
        self.client.login(username=username, password=password)
        contentbox = ContentBox.get(title='TEST_TITLE')
        response = self.client.get(reverse('contentbox-edit', args=(contentbox.id,)))
        self.assertEqual(response.status_code, 200)

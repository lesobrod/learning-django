from django.test import TestCase

from ..models import News, Comment
from django.urls import reverse


class NewsListViewTest(TestCase):

    def test_home_page(self):
        # send GET request.
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_news/authors.html')

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    def test_view_context(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('csrf_token' in resp.context)
        self.assertTrue(resp.context['is_verified'] == False)


class NewsDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Создаем тестовую новость
        News.objects.create(title='BigNews', description='WOW!!!')

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('news_detail', kwargs={'news_id': 1}))
        self.assertEqual(resp.status_code, 200)

    def test_view_context(self):
        resp = self.client.get(reverse('news_detail', kwargs={'news_id': 1}))
        self.assertTrue(resp.context['news'] == News.objects.get(id=1))
        self.assertTrue(resp.context['staticUrl'] == '/static/')

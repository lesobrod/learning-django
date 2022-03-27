from django.test import TestCase
from datetime import date
from ..models import News


class NewsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Создаем тестовую новость
        News.objects.create(title='BigNews', description='WOW!!!')

    def test_first_name_label(self):
        # Проверка метки
        news = News.objects.get(id=1)
        field_label = news._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'название')

    def test_first_name_max_length(self):
        # Проверка длины поля
        author = News.objects.get(id=1)
        max_length = author._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_date_created(self):
        # Проверка даты создания
        current_news = News.objects.get(title='BigNews')
        self.assertEquals(current_news.created_at.date(), date.today())


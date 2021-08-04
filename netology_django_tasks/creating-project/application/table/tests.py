from django.test import TestCase
from table.models import Table, Path


class TableModelTest(TestCase):
    """Тест модели таблицы."""

    def test_saving_and_retrieving(self):
        """Тест сохранение и получения объекта."""

        first_object = Table()
        first_object.name = 'Телефон'
        first_object.width = 2
        first_object.number = 1
        first_object.save()

        saved_object = Table.objects.first()

        self.assertEqual(saved_object, first_object)
        self.assertEqual(saved_object.name, 'Телефон')
        self.assertEqual(saved_object.width, 2)
        self.assertEqual(saved_object.number, 1)


class PathModelTest(TestCase):
    """Тест модели Путь."""

    def setUp(self) -> None:
        self.object_ = Path()
        self.object_.path = '/users/'
        self.object_.save()

    def test_saving_and_retrieving(self):
        """Тест сохранение и получения объекта."""

        saved_object = Path.objects.first()
        self.assertEqual(saved_object, self.object_)
        self.assertEqual(saved_object.path, '/users/')

    def test_method_get(self):
        self.assertEqual(self.object_.get_path(), self.object_.path)



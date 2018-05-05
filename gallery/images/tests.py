from django.test import TestCase
from .models import Editor,Post,tags
# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Ramza= Editor(first_name = 'Ramza', last_name ='Reseni', email ='Ramza@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))
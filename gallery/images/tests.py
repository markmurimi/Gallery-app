from django.test import TestCase
from .models import Editor,Post,tags
# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Ramza= Editor(first_name = 'Ramza', last_name ='Reseni', email ='Ramza@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Ramza,Editor))

    # Testing Save Method
    def test_save_method(self):
        self.Ramza.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class PostTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.Ramza= Editor(first_name = 'Ramza', last_name ='Reseni', email ='Ramza@moringaschool.com')
        self.Ramza.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_post= Post(title = 'Test Post',post = 'This is a random test Post',editor = self.Ramza)
        self.new_post.save()

        self.new_post.tags.add(self.new_tag)

def test_get_images_today(self):
        today_images = Post.todays_images()
        self.assertTrue(len(today_images)>0)

def test_get_images_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        images_by_date = Post.days_images(date)
        self.assertTrue(len(images_by_date) == 0)

def tearDown(self):
    Editor.objects.all().delete()
    tags.objects.all().delete()
    Post.objects.all().delete()
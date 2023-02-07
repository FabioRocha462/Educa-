from factory import Faker,SubFactory
from factory.django import DjangoModelFactory
from apps.products.models import Cleaning
from apps.users.models import User
from factory.fuzzy import FuzzyInteger
class UserFactory(DjangoModelFactory):

    username =  Faker("name")
    email = Faker("email")
    password = Faker("password")

    class Meta:
        models = User
        django_get_or_create = ['username']

class CleaningFactory(DjangoModelFactory):

    name = Faker("name")
    quantity = FuzzyInteger(1,200)
    user = SubFactory(UserFactory)
    
    class Meta:
        models = Cleaning
        django_get_or_create = ["name"]
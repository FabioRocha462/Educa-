from factory import Faker,SubFactory
from factory.django import DjangoModelFactory
from apps.products.models import Cleaning
from factory.fuzzy import FuzzyInteger

class CleaningFactory(DjangoModelFactory):

    name = Faker("name")
    quantity = FuzzyInteger(1,200)
    
    class Meta:
        model = Cleaning
        django_get_or_create = ["name"]
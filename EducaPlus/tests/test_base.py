from django.test import Client, TestCase
from apps.products.models import Food, Cleaning, Request_Food, Request_Cleaning
from apps.users.models import User
from apps.documents.models import Memorando, Official, Requeriment
from apps.events.models import Event
import datetime
class Base_test_core(TestCase):
    
    ####################################################
    ##########                                 #########
    ##########           Core User             #########
    ##########                                 #########
    ####################################################
    
    def setUp(self) -> None:
        return super().setUp

    def tearDown(self) -> None:
        return super().tearDown()

    def create_user(self):
        user = User.objects.create(
        username='teste', 
        email = 'teste@example.com',
        password='t1234567.',
        typeUser = 'asg',
        )
        user.save()
        return user

    def login(self):
        user_logged = self.cliente.login(email = 'teste@example.com', password = 't1234567.')
        return user_logged
    
    ####################################################
    ##########                                 #########
    ##########          Core Products          #########
    ##########                                 #########
    ####################################################

    def create_food(self):

        food = Food(
            name = "testefood",
            quantity = 40,
            validity = datetime.date.today(),
            typeCategoria = 1,
        )
        food.save()
        return food
    
    def create_request_food(self):

        request_food = Request_Food(
            name = "testerequest",
        )
        request_food.save()
        return request_food
    
    def create_cleaning(self):

        cleaning = Cleaning(
            name = "testecleaning",
            quantity = 60,
            user = self.create_user()
        )
        cleaning.save()
        return cleaning

    def create_request_cleaning(self):
        request_cleaning = Request_Cleaning(
            name = "testrequest"
        )
        request_cleaning.save()
        return request_cleaning

    def create_request_food(self):

        request_food = Request_Food(
            name = "testerequest",
        )

        request_food.save()
        return request_food
    
    ####################################################
    ##########                                 #########
    ##########          Core Documents         #########
    ##########                                 #########
    ####################################################
    
    def create_memorando(self):

        memorando = Memorando(
            others = "testefood",
            number = 4,
            receiver = "recebido",
            destiny = '1',
            description = "Teste de descrição de memorando",
            user = self.create_user(),
            created_at = datetime.date.today(),
        )
        memorando.save()
        return memorando
    
    def create_official(self):

        official = Official(
            others = "testefood",
            number = 4,
            receiver = "recebido",
            destiny = '1',
            description = "Teste de descrição de official",
            user = self.create_user(),
            created_at = datetime.date.today(),
        )
        official.save()
        return official
    
    def create_requirement(self):

        requeriment = Requeriment(
            others = "testefood",
            number = 4,
            receiver = "recebido",
            destiny = '1',
            description = "Teste de descrição de requeriment",
            user = self.create_user(),
            created_at = datetime.date.today(),
        )
        requeriment.save()
        return requeriment
    
    
    ####################################################
    ##########                                 #########
    ##########           Core Event            #########
    ##########                                 #########
    ####################################################
    
    def create_event(self):

        event = Event.objects.create(
            name = 'eventtest',
            school = 3,
            date = datetime.date.today(),
            user = self.create_user()
        )
        return event
from django.test import Client, TestCase
from django.urls import reverse_lazy, reverse
# from django.contrib.auth.models import User
from apps.users.models import User
from apps.documents.models import Memorando, Official, Requeriment
import datetime
class Test_Views_Products(TestCase):
    #test food
    #----------------------------------------------------------------
    #----------------------------------------------------------------
    #----------------------------------------------------------------   
    def setUp(self) -> None:
        return super().setUp

    def tearDown(self) -> None:
        return super().tearDown()



    def create_user(self):
        user = User.objects.create(
        username='teste', 
        email = 'teste@example.com',
        cpf = '123.456.789-00',
        password='t1234567.',
        typeUser = 'asg',
        )
        user.save()
        return user

    def login(self):
        user_logged = self.cliente.login(email = 'teste@example.com', password = 't1234567.')
        return user_logged

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
    
    #test Models documents Memorando
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
    def test_model_memorando(self):
        
        memorando = self.create_memorando()
        self.assertEqual(str(memorando.number) + '/' + str(memorando.created_at), str(memorando))
        
        
    #test Models documents Official
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
    def test_model_official(self):
        
        official = self.create_official()
        self.assertEqual(str(official.number) + '/' + str(official.created_at), str(official))
        
        
    #test Models documents Official
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
    def test_model_requirements(self):
        
        requirements = self.create_requirement()
        self.assertEqual(str(requirements.number) + '/' + str(requirements.created_at), str(requirements))
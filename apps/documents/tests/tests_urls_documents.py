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
            user = self.create_user()
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
            user = self.create_user()
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
            user = self.create_user()
        )
        requeriment.save()
        return requeriment
    
    #test URLs documents Memorando
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
    def test_url_create_memorando(self):
        
        url = reverse_lazy('documents:memorando_create')
        self.assertEqual(url, "/documents/memorandocreate/")
        
    def test_url_list_memorando(self):
        
        url = reverse_lazy('documents:memorando_list')
        self.assertEqual(url, '/documents/memorandolist/')
        
    def test_url_detail_memorando(self):
        
        memorando = self.create_memorando()
        url = reverse_lazy('documents:memorando_detail' , kwargs={'uuid': memorando.uuid})
        self.assertEqual(url, f'/documents/memorandodetail/{memorando.uuid}/')
        
    
    #test URLs documents Official
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
    def test_url_create_official(self):
        
        url = reverse_lazy('documents:official_create')
        self.assertEqual(url, "/documents/officialcreate/")
        
    def test_url_list_official(self):
        
        url = reverse_lazy('documents:official_list')
        self.assertEqual(url, '/documents/officiallist/')
        
    def test_url_detail_official(self):
        
        official = self.create_official()
        url = reverse_lazy('documents:official_detail' , kwargs={'uuid': official.uuid})
        self.assertEqual(url, f'/documents/officialdetail/{official.uuid}/')
        
    
    #test URLs documents Requirements
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
    def test_url_create_requirement(self):
        
        url = reverse_lazy('documents:requeriment_create')
        self.assertEqual(url, '/documents/requerimentcreate/')
        
    def test_url_list_requirements(self):
        
        url = reverse_lazy('documents:requeriment_list')
        self.assertEqual(url, '/documents/requerimentlist/')
        
    def test_url_detail_requirements(self):
        
        requirement = self.create_requirement()
        url = reverse_lazy('documents:requeriment_detail' , kwargs={'uuid': requirement.uuid})
        self.assertEqual(url, f'/documents/requerimentdetail/{requirement.uuid}/')
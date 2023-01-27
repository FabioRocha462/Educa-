from django.test import Client, TestCase
from django.urls import reverse_lazy, reverse
# from django.contrib.auth.models import User
from apps.account.models import User
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
    
    #test views documents Memorando
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
    def test_memorando_create_view(self):
        
        response = self.client.get(reverse_lazy("documents:memorando_list"),follow=True)
        assert response.status_code == 200
        
    def test_memorando_create_view_post(self):
        
        response = self.client.post(reverse_lazy("documents:memorando_list"),{"others":"testefood" , "number":4 , "receiver":"recebido" , "destiny":'1' , "description":"Teste de descrição de memorando" , "user":self.create_user()},follow=True)
        assert response.status_code == 200
        
    def test_memorando_list_view(self):
        
        response = self.client.get(reverse_lazy("documents:memorando_list"), follow=True)
        assert response.status_code == 200
        
    def test_memorando_detail_view(self):
        
        memorando = self.create_memorando()
        response = self.client.get(reverse_lazy("documents:memorando_detail", kwargs = {"uuid":memorando.uuid}),follow=True)
        assert response.status_code == 200
        
    #test views documents Official
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
    def test_official_create_view(self):
        
        response = self.client.get(reverse_lazy("documents:official_create"),follow=True)
        assert response.status_code == 200
        
    def test_official_create_view_post(self):
        
        response = self.client.post(reverse_lazy("documents:official_create"),{"others" : "testefood" , "number" : 4 , "receiver" : "recebido" , "destiny" : '1' , "description" : "Teste de descrição de official" , "user" : self.create_user()},follow=True)
        assert response.status_code == 200
        
    def test_official_list_view(self):
        
        response = self.client.get(reverse_lazy("documents:official_list"), follow=True)
        assert response.status_code == 200
        
    def test_official_detail_view(self):
        
        official = self.create_official()
        response = self.client.get(reverse_lazy("documents:official_detail", kwargs = {"uuid":official.uuid}),follow=True)
        assert response.status_code == 200
        
    
    #test views documents Requirements
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
    def test_requirements_create_view(self):
        
        response = self.client.get(reverse_lazy("documents:requeriment_create"),follow=True)
        assert response.status_code == 200
        
    def test_requirements_create_view_post(self):
        
        response = self.client.post(reverse_lazy("documents:requeriment_create"),{"others" : "testefood" , "number" : 4 , "receiver" : "recebido" , "destiny" : '1' , "description" : "Teste de descrição de requirement" , "user" : self.create_user()},follow=True)
        assert response.status_code == 200
        
    def test_requirements_list_view(self):
        
        response = self.client.get(reverse_lazy("documents:requeriment_list"), follow=True)
        assert response.status_code == 200
        
    def test_requirements_detail_view(self):
        
        requirement = self.create_requirement()
        response = self.client.get(reverse_lazy("documents:requeriment_detail", kwargs = {"uuid":requirement.uuid}),follow=True)
        assert response.status_code == 200
from EducaPlus.tests import test_base
from django.urls import reverse_lazy, reverse
import datetime
class Test_Views_Documents(test_base.Base_test_core):
  
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
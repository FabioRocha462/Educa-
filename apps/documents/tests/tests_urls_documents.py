from EducaPlus.tests import test_base
from django.urls import reverse_lazy, reverse
import datetime
class Test_Urls_Documents(test_base.Base_test_core):
    
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
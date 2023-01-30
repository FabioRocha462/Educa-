from EducaPlus.tests import test_base
from django.urls import reverse_lazy, reverse
import datetime
class Test_Models_Documents(test_base.Base_test_core):
    
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
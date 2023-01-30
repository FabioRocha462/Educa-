from EducaPlus.tests import test_base
from django.urls import reverse_lazy
import datetime

class Test_Models_Events(test_base.Base_test_core):

    #test Models Event
    #----------------------------------------------------------------
    #----------------------------------------------------------------
    #----------------------------------------------------------------
    
    def test_model_events(self):
        
        event = self.create_event()
        self.assertEqual(event.name, str(event))
from django.forms import ModelForm
from community.models import *

class Form(ModelForm):
    class Meta:
        model=UserData
        fields=['height','weight','action_lv','action_cl','action_pp','action_tm','action_wk','action_pc','health','today_feel']

from django.forms import ModelForm
from .models import Project

class ProjectReg(ModelForm):
    required_css_class = "required"

    class Meta:
        model = Project
        fields = ['studentname', 'ptopic', 'planguages', 'pduration']  # Corrected typo from 'plangauges'

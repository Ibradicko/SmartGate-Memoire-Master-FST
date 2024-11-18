from django import forms
from django.contrib.auth.models import User
from .models import Categorie, Formation, Lesson



class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'
        help_texts = {
            'Titre': 'Psh. Categorie 11 ose Categorie e Informatikes',
            'Description':'Vendos nje pershkrim te shkurte te categories',
            'Image':'Mund te vendosesh nje fotografi e categories ose mund te lihet bosh'
        }

class LendaForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['Createur','slug', 'Titre', 'Categorie', 'Description', 'Image_formation']
        help_texts = {
            'Titre': 'Psh. Matematika, Gjeografi etj',
            'Description':'Vendos nje pershkrim te shkurte te lendes',
            'Categorie':'Zhgjidhni categorien per te cilen do te creerni lenden',
            'Image_formation':'Mund te vendosesh nje fotografi e lendes ose mund te lihet bosh'
        }
        labels = {
            'Titre':'Titre i lendes'
        }
        widgets = {'Createur': forms.HiddenInput(), 'slug': forms.HiddenInput()}


class MesimiForm(forms.ModelForm):
    class Meta:
        model = Lesson 
        fields = ['slug','Titre', 'lenda', 'video_id', 'position', ]
        help_texts = {
            'Titre':'Vendosni Titren e mesimit',
            'lenda':'Zgjidhni lenden per te cilen i perket ky mesim',
            'video_id':'Vendosni ID e videos nga Youtube te cilen do te ngarkoni (<a href="/media/youtube_help.png">ku mund ta gjej ID</a>)',
            'position':'Vendosni numrin e pozicionit ose radhen e mesimit '
        }
        widgets = {
            'slug': forms.HiddenInput()
        }
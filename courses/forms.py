from django import forms
from .models import Categorie, Formation, Lesson
from ckeditor.widgets import CKEditorWidget  # Importez CKEditorWidget

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'  # Inclut tous les champs du modèle
        help_texts = {
            'Titre': 'Le titre de la catégorie',
            'Description': 'Donnez une description de la catégorie',
            'Image': 'Importer une image illustrative de la catégorie de formation'
        }


class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['Createur', 'slug', 'Categorie', 'Titre',  'Description', 'Image_formation']
        help_texts = {
            'Categorie': 'selectionner la catégorie',
            'Titre': 'Le titre de la formation',
            'Description': 'Donnez une petite description de la formation',
            'Image_formation': 'Mund te vendosesh nje fotografi e lendes ose mund te lihet bosh'
        }
        labels = {
            'Titre': 'Le Titre de la formation'
        }
        widgets = {
            'Createur': forms.HiddenInput(),  # Masquer le champ Createur
            'slug': forms.HiddenInput(),      # Masquer le champ slug
        }


class CoursForm(forms.ModelForm):
    categorie = forms.ModelChoiceField(
        queryset=Categorie.objects.all(),
        required=True,
        label="Catégorie",
        help_text="Sélectionnez une catégorie pour afficher ses formations.",
    )

    class Meta:
        model = Lesson
        fields = ['categorie', 'formation', 'slug', 'Titre', 'video_id','Contenu', 'position']
        help_texts = {
            'Titre': 'Entrez le titre de la leçon.',
            'formation': 'Sélectionnez la formation correspondante.',
            'video_id': 'Ajoutez l’ID de la vidéo Youtube.',
            'position': 'Position ou ordre de la leçon.',
            'Contenu' : 'créez votre cours avec notre editeur',
        }
        widgets = {
            'slug': forms.HiddenInput(),  # Masquer le champ slug
            'Contenu': CKEditorWidget(),
        }

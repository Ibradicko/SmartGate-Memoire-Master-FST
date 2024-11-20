from django.db import models
from memberships.models import Membership
from django.contrib.auth.models import User
from django.urls import reverse 


class Categorie(models.Model):
    Titre = models.CharField(max_length=150)
    Description = models.TextField() # Utilisation de CKEditor pour la description
    Description = models.TextField(max_length= 2000, null=True)
    Image = models.ImageField(upload_to='cat_images', default='cat_images/default.jpg')

    def __str__(self):
        return '{}'.format(self.Titre)

class Formation(models.Model):
    Createur = models.ForeignKey(User,on_delete = models.CASCADE)
    slug = models.SlugField()
    Titre = models.CharField(max_length=30)
    Categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    Description = models.TextField() # Utilisation de CKEditor pour la description
    Creer_le = models.DateTimeField(auto_now=True)
    Image_formation = models.ImageField(upload_to='formationimages', default='default.jpg')

    def __str__(self):
        return self.Titre

    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"slug": self.slug})

    def get_courses_related_to_memberships(self):
        return self.courses.all()

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')


class Lesson(models.Model):
    slug = models.SlugField()
    Titre = models.TextField()
    formation = models.ForeignKey(Formation,on_delete=models.CASCADE, default=1)
    video_id = models.CharField(max_length=11)
    Contenu = models.TextField()
    position = models.IntegerField()

    def __str__(self):
        return self.Titre

    def get_absolute_url(self):
        return reverse("courses:lesson_detail", kwargs={"course_slug": self.formation.slug,'lesson_slug':self.slug})

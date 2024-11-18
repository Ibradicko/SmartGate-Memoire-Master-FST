from django.urls import path
from django.contrib.auth.decorators import login_required

from courses.views import HomeView,AboutView,ContactView,CourseListView, CourseDetailView,LessonDetailView, SearchView, creer_cat, creer_formation, creer_cours

app_name = 'courses'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('courses/<int:category>', CourseListView, name='course_list'),
    path('courses/<slug>/', login_required(CourseDetailView.as_view()), name='course_detail'),
    path('courses/<course_slug>/<lesson_slug>/', login_required(LessonDetailView.as_view()), name='lesson_detail'),
    path('search/', SearchView, name='rechercher_cours'),
    path('creer/categorie', creer_cat, name='creer_cat'),
    path('creer/lende', creer_formation, name='creer_formation'),
    path('creer/mesim', creer_cours, name='creer_cours')
]

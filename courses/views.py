import secrets
from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,DetailView,View
from courses.models import Formation,Lesson,Categorie
from memberships.models import UserMembership
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CategorieForm, LendaForm, MesimiForm
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Categorie.objects.all()
        context['category'] = category
        return context

class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'



def CourseListView(request, category):
    courses = Formation.objects.filter(Categorie=category)
    context = {
        'courses':courses
    }
    return render(request, 'courses/course_list.html', context)



class CourseDetailView(DetailView):
    context_object_name = 'course'
    template_name = 'courses/course_detail.html'
    model = Formation


 
class LessonDetailView(View,LoginRequiredMixin):
    def get(self, request, course_slug, lesson_slug, *args, **kwargs):
        course = get_object_or_404(Formation, slug=course_slug)
        lesson = get_object_or_404(Lesson, slug=lesson_slug)
        context = {'lesson': lesson}
        return render(request, "courses/lesson_detail.html", context)


@login_required
def SearchView(request):
    if request.method == 'POST':
        kerko = request.POST.get('search')
        results = Lesson.objects.filter(Titre__contains=kerko)
        context = {
            'results':results
        }
        return render(request, 'courses/search_result.html', context)


@login_required
def creer_cat(request):
    if not request.user.profile.is_teacher == True:
        messages.error(request, f'Llogaria juaj nuk ka akses ne kete url vetem llogarite e mesuesve!')
        return redirect('courses:home')
    if request.method == 'POST':
        form = CategorieForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Categorie juaj u krijua.')
            return redirect('courses:home')
    else:
        form = CategorieForm()
    context = {
        'form':form
    }
    return render(request, 'courses/creer_cat.html', context)


@login_required
def creer_formation(request):
    if not request.user.profile.is_teacher == True:
        messages.error(request, f'Llogaria juaj nuk ka akses ne kete url vetem llogarite e mesuesve!')
        return redirect('courses:home')
    if request.method == 'POST':
        form = LendaForm(request.POST)
        if form.is_valid():
            form.save()
            Categorie = form.cleaned_data['Categorie']
            slug = Categorie.id
            messages.success(request, f'Lenda juaj u krijua.')
            return redirect('/courses/' + str(slug))
    else:
        form = LendaForm(initial={'Createur':request.user.id, 'slug':secrets.token_hex(nbytes=16)})
    context = {
        'form':form
    }
    return render(request, 'courses/creer_formation.html', context)


@login_required
def creer_cours(request):
    if not request.user.profile.is_teacher == True:
        messages.error(request, f'Llogaria juaj nuk ka akses ne kete url vetem llogarite e mesuesve!')
        return redirect('courses:home')
    if request.method == 'POST':
        form = MesimiForm(request.POST)
        if form.is_valid():
            form.save()
            lenda = form.cleaned_data['lenda']
            slug = lenda.slug
            messages.success(request, f'Mesimi juaj u krijua.')
            return redirect('/courses/' + str(slug) )
    else:
        form = MesimiForm(initial={'slug':secrets.token_hex(nbytes=16)})
    context = {
        'form':form
    }
    return render(request, 'courses/creer_cours.html', context)


def view_404(request, exception):
    return render(request, '404.html')

def view_403(request, exception):
    return render(request, '403.html')

def view_500(request):
    return render(request, '500.html')

# def get(self,request,course_slug,lesson_slug,*args,**kwargs):
#
#     course_qs = Course.objects.filter(slug=course_slug)
#     if course_qs.exists():
#         course = course_qs.first()
#     lesson_qs = course.lessons.filter(slug=lesson_slug)
#     if lesson_qs.exists():
#         lesson = lesson_qs.first()
#     user_membership = UserMembership.objects.filter(user=request.user).first()
#     user_membership_type = user_membership.membership.membership_type
#
#     course_allowed_membership_type = course.allowed_memberships.all()
#     context = {'lessons':None}
#
#     if course_allowed_membership_type.filter(membership_type=user_membership_type).exists():
#         context = {'lesson':lesson}
#
#     return render(request,'courses/lesson_detail.html',context)

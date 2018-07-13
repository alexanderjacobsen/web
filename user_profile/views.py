from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, CreateView

from .models import Profile, Skill, Project
from .forms import ProfileForm, ProjectForm


class DetailSkillView(DetailView):
    model = Skill


class DetailProjectView(DetailView):
    model = Project


class CreateProjectView(PermissionRequiredMixin, CreateView):
    redirect_field_name = 'user_profile/project.html'
    permission_required = 'recommendation.change_entry'
    model = Project
    form_class = ProjectForm

##############################################


def profile(request, username):
    user = get_object_or_404(User, username=username)
    try:
        user.profile  # Accessing a non-existent profile (they do no exist by default) triggers an error
    except Profile.DoesNotExist:
        new_profile = Profile(user=user)
        new_profile.save()

    # populate()
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            # user.profile.skills.remove(user.profile.skills.all()) seems to delete all skills completely from the DB
            # removing the connection one way does not remove it the other way...?
            for skill in Skill.objects.all():
                user.profile.skills.remove(skill)
                skill.members.remove(user.profile)
            for skill in form.cleaned_data['skills']:
                user.profile.skills.add(skill)
                skill.members.add(user.profile)

    return render(
        request,
        'user_profile/profile.html',
        {'profile': user.profile, 'edit': request.user == user, 'form': form}
    )


def populate():
    print("POPULATING...")
    print(".")
    print(".")
    s1 = Skill(name='ku')
    s2 = Skill(name='hest')
    s3 = Skill(name='gris')

    for s in [s1, s2, s3]:
        s.save()

    p1 = Project(title='Nytt hus')
    p2 = Project(title='Male båt')
    p1.save()
    p2.save()

    u1 = User(username='Pål', password='123qweasd')
    u2 = User(username='Gunnar', password='123qweasd')
    u1.save()
    u2.save()

    p1 = Profile(user=u1)
    p2 = Profile(user=u2)
    p1.skills.add(s1)
    p1.skills.add(s2)
    p2.skills.add(s2)
    p2.skills.add(s3)
    p1.projects.add(p1)
    p2.projects.add(p1)
    p2.projects.add(p2)
    p1.save()
    p2.save()
    print("DONE")

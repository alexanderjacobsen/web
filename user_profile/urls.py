from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import profile, DetailSkillView, DetailProjectView, CreateProjectView, apply_to_project, DeleteProjectView, \
    EditProjectView, ListProjectView

urlpatterns = [
    url(r'projects/$', ListProjectView.as_view(), name='project_list'),
    url(r'project/(?P<pk>\d+)/delete/$', DeleteProjectView.as_view(), name='delete_project'),
    url(r'project/(?P<pk>\d+)/edit/$', EditProjectView.as_view(), name='edit_project'),
    url(r'project/(?P<pk>\d+)/apply/$', apply_to_project, name='apply_to_project'),
    url(r'project/(?P<pk>\d+)$', DetailProjectView.as_view(), name='project'),
    url(r'project/new/$', CreateProjectView.as_view(), name='project_form'),
    url(r'skill/(?P<pk>\d+)$', DetailSkillView.as_view(), name='skill'),

    # must always be at the end, else it will interpret skill, project etc. as usernames
    url(r'(?P<username>[-\w.]+)/$', profile, name='profile'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


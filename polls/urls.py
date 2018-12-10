from django.urls import path
from django.conf.urls import include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'choices', views.ChoiceViewSet)


app_name = 'polls'
urlpatterns = [
    path('api/create/', views.CreateView.as_view(), name='create'),
    path('api/', include(router.urls)),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


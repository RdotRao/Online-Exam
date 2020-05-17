try:
    from django.conf.urls import url , path
except ImportError:
    from django.urls import re_path as url , path
from .views import *

urlpatterns = [

    path('',loginuser),
    path('logout',userlogout, name = 'logout'),
    path('importstudentcsv',importstudentcsv, name = 'importstudentcsv'),
    path('myprofile',myprofile, name = 'myprofile'),
    path('adminuser',adminuser, name = 'adminuser'),

    url(r'^password/$', change_password, name='change_password'),
    
    url(r'^quizlist/$',
        view=QuizListView.as_view(),
        name='quiz_index'),
    url(r'^category/$',
        view=CategoriesListView.as_view(),
        name='quiz_category_list_all'),

    url(r'^category/(?P<category_name>[\w|\W-]+)/$',
        view=ViewQuizListByCategory.as_view(),
        name='quiz_category_list_matching'),

    url(r'^progress/$',
        view=QuizUserProgressView.as_view(),
        name='quiz_progress'),

    url(r'^quizmarking/$',
        view=QuizMarkingList.as_view(),
        name='quiz_marking'),

    url(r'^marking/(?P<pk>[\d.]+)/$',
        view=QuizMarkingDetail.as_view(),
        name='quiz_marking_detail'),

    #  passes variable 'quiz_name' to quiz_take view
    url(r'^(?P<slug>[\w-]+)/$',
        view=QuizDetailView.as_view(),
        name='quiz_start_page'),

    url(r'^(?P<quiz_name>[\w-]+)/take/$',
        view=QuizTake.as_view(),
        name='quiz_question'),
]

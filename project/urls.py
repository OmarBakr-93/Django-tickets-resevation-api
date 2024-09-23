from django.contrib import admin
from django.urls import path, include
from reservation import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guests', views.viewsets_guests)
router.register('movies', views.viewsets_movie)
router.register('reservations', views.viewsets_reservation)

urlpatterns = [
    path('admin/', admin.site.urls),
    #1
    path('django/jsonResponse', views.no_rest_no_model, name='no_rest_no_model'),
    #2
    path('django/jsonResponse2', views.no_rest_from_model, name='no_rest_from_model'),
    #3.1
    path('fbvList/', views.FBV_list, name='fbcList'),
    #3.2
    path('fbvPk/<int:pk>/', views.FBV_pk, name='fbvPk'),
    #4.1
    path('cbvView/', views.CBV_View.as_view(), name='cbvView'),
    #4.2
    path('cbvGeneric/<int:pk>/', views.CBV_Pk.as_view(), name='cbvGeneric'),
    #5.1
    path('api/mixinslist/',views.Mixin_List.as_view()),
    #5.2
    path('api/mixinspk/<int:pk>/',views.Mixin_Pk.as_view()),
    #6.1
    path('api/genericlist/',views.Generic_List.as_view()),
    #6.2
    path('api/genericpk/<int:pk>/',views.Generic_Pk.as_view()),
    #7.1
    path('api/viewsetlist/',include(router.urls)),
    #8.1
    path('api/findmovie/',views.find_movie),
    #9.1
    path('api/reservation/',views.create_reservation),
]

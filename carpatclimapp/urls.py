from django.urls import path
from django.conf.urls import url
from . import views, views_test


urlpatterns = [
    path('', views.home, name='home'),
    path('yearly/', views.yearly, name='yearly'),
    path('monthly/', views.monthly, name='monthly'),
    path('daily/', views.daily, name='daily'),
    path('<int:year>/<int:month>/<int:day>/figure.png', views.carpatclim_d_figure, name='carpatclim_d_figure'),
    path('<int:year>/<int:month>/figure.png', views.carpatclim_m_figure, name='carpatclim_m_figure'),
    path('<int:year>/figure.png', views.carpatclim_y_figure, name='carpatclim_y_figure'),
    path('<int:year>/<int:month>/<int:day>/', views.carpatclim_d, name='carpatclim_d'),
    path('<int:year>/<int:month>/', views.carpatclim_m, name='carpatclim_m'),
    path('<int:year>/', views.carpatclim_y, name='carpatclim_y'),
    # test view examples
    path('test/', views_test.test, name='test'),
    path('test/random.png', views_test.random_graph, name='random_graph'),
    path('test/sine_variant_1.png', views_test.sine_variant_1, name='sine_variant_1'),
    path('test/sine_variant_2.png', views_test.sine_variant_2, name='sine_variant_2'),
    path('test/sine.png', views_test.sine, name='sine'),
    path('test/spiral.png', views_test.spiral_graph, name='spiral_graph'),
]

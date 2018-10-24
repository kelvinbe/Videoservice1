from django.urls import path
from .views import MembershipSelect

app_name = 'Memberships'
urlpatterns = [
     path('', MembershipSelect.as_view(), name='select')

 ]

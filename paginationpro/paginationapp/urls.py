from django.conf.urls import url,include
from paginationapp import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('emp_viewset',views.EmpViewset)

urlpatterns = [
	url(r'',include(router.urls))

]
from rest_framework import routers

from emploees.views import EmployeesViewSet, PersonViewSet, FunctionViewSet

router = routers.DefaultRouter()
router.register(r'employees', EmployeesViewSet)
router.register(r'person', PersonViewSet)
router.register(r'function', FunctionViewSet)



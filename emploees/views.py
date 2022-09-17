from rest_framework.viewsets import ModelViewSet

from emploees.models import Employees, Person, Function
from emploees.serializers import EmployeesSerializer, PersonSerializer, FunctionSerializer

# Каждый из нижеописанных классов, наследуясь от (ModelViewSet),
# имеет все методы CRUD, что отражено а админке DRF


class EmployeesViewSet(ModelViewSet):
    serializer_class = EmployeesSerializer
    queryset = Employees.objects.all()


class PersonViewSet(ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class FunctionViewSet(ModelViewSet):
    serializer_class = FunctionSerializer
    queryset = Function.objects.all()
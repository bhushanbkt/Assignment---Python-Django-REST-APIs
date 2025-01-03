from rest_framework.viewsets import ModelViewSet
from .models import Expense, Settlement, Group, Category
from .serializers import ExpenseSerializer, SettlementSerializer, GroupSerializer, CategorySerializer


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class SettlementViewSet(ModelViewSet):
    queryset = Settlement.objects.all()
    serializer_class = SettlementSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from apps.expenses.views import ExpenseViewSet, SettlementViewSet, GroupViewSet, CategoryViewSet
from apps.users.views import UserViewSet

router = DefaultRouter()
router.register('expenses', ExpenseViewSet)
router.register('settlements', SettlementViewSet)
router.register('groups', GroupViewSet)
router.register('categories', CategoryViewSet)
router.register('users', UserViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Expense Splitter API",
        default_version='v1',
        description="API for expense splitting and tracking",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

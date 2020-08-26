from django.urls import include, path

from .views import TransactionCreate, TransactionDetail, TransactionList

urlpatterns = [
    path('', TransactionList.as_view(), name="list"),
    path('<int:pk>/', TransactionDetail.as_view(), name="detail"),
    path('new/', TransactionCreate.as_view(), name="create"),
]
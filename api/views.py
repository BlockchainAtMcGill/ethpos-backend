from rest_framework import generics

from .models import TransactionLog
from .serializers import TransactionSerializer
from .permissions import IsOwner

class TransactionList(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return TransactionLog.objects.filter(vendor=user)

class TransactionCreate(generics.CreateAPIView):
    queryset = TransactionLog.objects.all()
    serializer_class = TransactionSerializer

    # To avoid exposing the vendor, we set his value based on the logged in user
    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user) 

class TransactionDetail(generics.RetrieveDestroyAPIView):
    queryset = TransactionLog.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsOwner,)
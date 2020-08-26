from rest_framework import serializers

from .models import TransactionLog

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        # Does not expose the vendor
        fields = ('id', 'price', 'description',)
        model = TransactionLog
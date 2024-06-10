from rest_framework import serializers
from api.models import company,employee
# cresate serializer
class companyserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=company
        fields="__all__"


class employeeserialixer(serializers.HyperlinkedModelSerializer):
    # id=serializers.ReadOnlyField()
    class Meta:
        model=employee
        fields="__all__"

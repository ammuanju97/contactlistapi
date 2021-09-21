from rest_framework.serializers import ModelSerializer
from .models import ContactList

class ContactSerializer(ModelSerializer):
    class Meta:
        model = ContactList
        fields = ['country_code', 'id', 'first_name', 'last_name', 'phone_number', 
        'contact_picture', 'is_favorite']
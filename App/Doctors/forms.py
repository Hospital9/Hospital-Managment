from django import forms 
from .models import Appointment,Profile,Doctor



class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'education', 'quote'] 


class DateInput(forms.DateInput):
    input_type = 'date' 

class TextInput(forms.TextInput):
    input_type = 'text'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment   

        fields = '__all__' 

        exclude = ['doctor']

        widgets = {
                'date':DateInput(attrs={'id':'datepicker'}),
                'doctor':TextInput(attrs={
                      
                }),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__' 
        exclude = ['user']

        widgets = {
                'birth_date':DateInput(attrs={'id':'datepicker'})
        }


from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from datetime import date
from Doctors.models import Profile, Appointment

class BaseTest(TestCase):
    def setUp(self): 
        self.register_url = reverse('registerView')
        self.user = { 
            'first_name':'User',
            'last_name':'User', 
            'username':'user',
            'email':'user@gmail.com',
            'password1':'django123',
            'password2':'django123',
        }
        return super().setUp()

class RegisterTest(BaseTest):
    def test_can_view_page_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'Register/register.html')



class DoctorDashboardViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user.save()
        self.profile = Profile.objects.create(user=self.user, is_doctor=True)
        self.appointment = Appointment.objects.create(doctor=self.user.profile.doctor, date=date.today(),timeslot=2)

    def test_doctor_dashboard_view_with_user_not_logged_in(self):
        response = self.client.get(reverse('doctorDashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/dashboard')

    def test_doctor_dashboard_view_with_not_doctor_user(self):
            self.client.login(username='testuser',password='testpassword')
            self.profile.is_doctor = False
            self.profile.save()
            response = self.client.get(reverse('doctorDashboard'))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "Please go back,this page it's only for staff.")

    def test_doctor_dashboard_view_with_doctor_user(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('doctorDashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Dashboard/doctorDashboard.html')
        self.assertContains(response, 1)
        self.assertContains(response, 1)

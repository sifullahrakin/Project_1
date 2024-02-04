# from django.test import TestCase
# from django.urls import reverse
# from .models import Company, Employee, Device
#
# class AssetManagementTests(TestCase):
#
#     def setUp(self):
#         self.company = Company.objects.create(name='Test Company')
#         self.employee = Employee.objects.create(company=self.company, name='John Doe')
#         self.device = Device.objects.create(name='Laptop', condition='Good')
#
#     def test_company_list_view(self):
#         response = self.client.get(reverse('company_list'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, self.company.name)
#
#     def test_employee_list_view(self):
#         response = self.client.get(reverse('employee_list', args=(self.company.id,)))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, self.employee.name)
#
#     def test_device_list_view(self):
#         response = self.client.get(reverse('device_list'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, self.device.name)
#
#     def test_checkout_device(self):
#         response = self.client.post(reverse('checkout_device', args=(self.device.id,)), {'employee': self.employee.id})
#         self.assertEqual(response.status_code, 302)  # Redirect after successful checkout
#         self.device.refresh_from_db()
#         self.assertIsNotNone(self.device.checked_out)
#         self.assertEqual(self.device.employee, self.employee)
#
#     def test_return_device(self):
#         self.device.checked_out = timezone.now()
#         self.device.employee = self.employee
#         self.device.save()
#         response = self.client.post(reverse('return_device', args=(self.device.id,)))
#         self.assertEqual(response.status_code, 302)  # Redirect after successful return
#         self.device.refresh_from_db()
#         self.assertIsNone(self.device.checked_out)
#         self.assertIsNone(self.device.employee)
#

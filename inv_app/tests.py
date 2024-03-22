from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Invoice, InvoiceDetail

class InvoiceAPITestCase(APITestCase):
    def setUp(self):
        self.invoice = Invoice.objects.create(date='2024-03-19', customer_name='Test Customer')

    def test_create_invoice(self):
        data = {
            'date': '2024-03-19',
            'customer_name': 'Test Customer'
        }
        url = reverse('invoice-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Invoice.objects.count(), 2)

    def test_retrieve_invoice(self):
        url = reverse('invoice-detail', args=[self.invoice.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['customer_name'], 'Test Customer')

    def test_update_invoice(self):
        data = {
            'date': '2024-03-20',  # Updated date
            'customer_name': 'Updated Customer Name'  # Updated customer name
        }
        url = reverse('invoice-detail', args=[self.invoice.pk])
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['date'], '2024-03-20')
        self.assertEqual(response.data['customer_name'], 'Updated Customer Name')

    def test_delete_invoice(self):
        url = reverse('invoice-detail', args=[self.invoice.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Invoice.objects.filter(pk=self.invoice.pk).exists())

class InvoiceDetailAPITestCase(APITestCase):
    def setUp(self):
        self.invoice = Invoice.objects.create(date='2024-03-19', customer_name='Test Customer')
        self.invoice_detail = InvoiceDetail.objects.create(invoice=self.invoice, description='Test Description', quantity=2, unit_price=10, price=20)

    def test_update_invoice_detail(self):
        data = {
            'invoice': self.invoice.pk,
            'description': 'Updated Description',
            'quantity': 3,
            'unit_price': 15,
            'price': 45
        }
        url = reverse('invoicedetail-detail', args=[self.invoice_detail.pk])
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['description'], 'Updated Description')
        self.assertEqual(response.data['quantity'], 3)
        self.assertEqual(int(float(response.data['unit_price'])), 15)
        self.assertEqual(int(float(response.data['price'])), 45)

    def test_delete_invoice_detail(self):
        url = reverse('invoicedetail-detail', args=[self.invoice_detail.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(InvoiceDetail.objects.filter(pk=self.invoice_detail.pk).exists())

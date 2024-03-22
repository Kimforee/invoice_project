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


class InvoiceDetailAPITestCase(APITestCase):
    def setUp(self):
        self.invoice = Invoice.objects.create(date='2024-03-19', customer_name='Test Customer')
        self.invoice_detail = InvoiceDetail.objects.create(invoice=self.invoice, description='Test Description', quantity=2, unit_price=10, price=20)

    def test_create_invoice_detail(self):
        data = {
            'invoice': self.invoice.pk,
            'description': 'Test Description',
            'quantity': 2,
            'unit_price': 10,
            'price': 20
        }
        url = reverse('invoicedetail-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(InvoiceDetail.objects.count(), 2) 

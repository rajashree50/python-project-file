from django.test import TestCase

# Create your tests here.
class CalculatorTests(TestCase):
    def test_add(self):
        res = self.client.get('/result/',{'num1':'5','num2':'3','operation':'add'})
        self.assertcontains(res,'result:8.0')

    def test_divide_by_zero(self):
        res = self.client.get('/result/',{'num1':'5','num2':'0','operation':'divide'})
        self.assertcontains(res,'Error: Division by zero')

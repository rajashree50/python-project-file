from django.shortcuts import render

def home (request):
    return render(request,'calculatorapp/home.html')

def result(request):
    if request.method == 'GET':
        num1 = request.GET.get('num1')
        num2 = request.GET.get('num2')
        op = request.GET.get('operation')
        result = None
        error = None

        try:
            a = float(num1)
            b = float(num2)
            if op == 'add':
                result = a + b
            elif op == 'subtract':
                result = a - b
            elif op == 'multiple':
                result = a * b
            elif op == 'divide':
                result = a / b if b != 0 else(_ for _ in ()).throw(ZeroDivisionError)
            else:
                error = 'invalid operation'
        except ZeroDivisionError:
            error = 'error: Division by Zero'
        except:
            error = 'Error: invalid input'

        return render(request,'calculatorapp/result.html',{'result':result,'error':error})
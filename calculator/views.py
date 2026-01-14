from django.shortcuts import render

def index(request):
    res = None
    if request.method == "POST":
        try:
            n1 = float(request.POST.get('n1', 0))
            n2 = float(request.POST.get('n2', 0))
            op = request.POST.get('op')

            if op == "sumar": res = n1 + n2
            elif op == "restar": res = n1 - n2
            elif op == "multiplicar": res = n1 * n2
            elif op == "dividir":
                res = n1 / n2 if n2 != 0 else "Error: Div por 0"
            elif op == "potencia": res = n1 ** n2
        except (ValueError, TypeError):
            res = "Error de entrada"
            
    return render(request, 'index.html', {'resultado': res})
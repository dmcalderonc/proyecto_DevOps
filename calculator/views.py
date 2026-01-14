from django.shortcuts import render

def index(request):
    res = None  # Valor por defecto
    if request.method == "POST":
        try:
            # Los nombres 'n1', 'n2' y 'op' deben coincidir con tu HTML y tu Test
            n1 = float(request.POST.get('n1', 0))
            n2 = float(request.POST.get('n2', 0))
            op = request.POST.get('op')
            
            if op == "sumar":
                res = n1 + n2
            elif op == "restar":
                res = n1 - n2
        except (ValueError, TypeError):
            res = "Error en los datos"

    # Es vital que 'resultado' esté aquí para que el test lo encuentre
    return render(request, 'index.html', {'resultado': res})
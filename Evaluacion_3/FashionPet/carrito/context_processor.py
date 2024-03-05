# Esto es IMPORTANTÍSIMO para el carrito:
def importe_total_carrito(request):
    total=0
    if 'carrito' in request.session:
        for key, value in request.session["carrito"].items():
            total=total+int(value["precio"])
    return {"importe_total_carrito": total}
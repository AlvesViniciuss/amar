from django.shortcuts import render, redirect
from .models import User, Item
from .forms import ItemForm

def default_view(request):
    return redirect('inventory:login')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username, password=password)
            # Aqui você pode redirecionar para a tela de controle de estoque após o login bem-sucedido
            return redirect('inventory:stock_control')
        except User.DoesNotExist:
            # Aqui você pode exibir uma mensagem de erro de login inválido
            pass
    return render(request, 'inventory/login.html')

def user_registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        User.objects.create(username=username, password=password, email=email)
        # Aqui você pode redirecionar para a tela de login após o registro bem-sucedido
        return redirect('inventory:login')
    return render(request, 'inventory/user_registration.html')

def stock_control(request):
    items = Item.objects.all()
    return render(request, 'inventory/stock_control.html', {'items': items})


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:stock_control')

    else:
        form = ItemForm()

    return render(request, 'inventory/add_item.html', {'form': form})

def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('inventory:stock_control')
    return redirect('inventory:confirm_delete_item', item_id=item_id)

def confirm_delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, 'inventory/confirm_delete_item.html', {'item': item})

def edit_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventory:stock_control')
    else:
        form = ItemForm(instance=item)
    return render(request, 'inventory/edit_item.html', {'form': form})


def sales_balance(request):
    items = Item.objects.all()

    for item in items:
        valor_compra = item.valor or 0  # Tratar valor de compra como 0 se for None
        valor_venda = item.valor_venda or 0  # Tratar valor de venda como 0 se for None
        item.balance = item.quantidade * (valor_compra - valor_venda)

    return render(request, 'inventory/sales_balance.html', {'items': items})
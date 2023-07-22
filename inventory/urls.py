# amar/inventory/urls.py

from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.default_view, name='default_view'),  # Add this line for the root URL
    path('login/', views.login, name='login'),
    path('user-registration/', views.user_registration, name='user_registration'),
    path('stock-control/', views.stock_control, name='stock_control'),
    path('add-item/', views.add_item, name='add_item'),  # URL para adicionar item ao estoque
    path('confirm-delete-item/<int:item_id>/', views.confirm_delete_item, name='confirm_delete_item'),  # URL para confirmação de exclusão
    path('delete-item/<int:item_id>/', views.delete_item, name='delete_item'),  # URL para excluir item do estoque
    path('edit-item/<int:item_id>/', views.edit_item, name='edit_item'),  # Nova URL para edição do item
    path('sales-balance/', views.sales_balance, name='sales_balance'),
]

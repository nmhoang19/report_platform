from django.shortcuts import render

# Create your views here.
def home(request):
    items = [{'id': i, 'name': f'Item {i}', 'description': f'This is description for item {i}'} for i in range(1, 11)]
    return render(request, 'home/home.html', {'items': items})

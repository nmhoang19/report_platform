from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def reports(request):
    items = [{'id': i, 'name': f'Item {i}', 'description': f'This is description for item {i}'} for i in range(1, 11)]
    return render(request, 'home/reports.html', {'items': items})

def users(request):
    return render(request, 'home/users.html')

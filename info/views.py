from django.shortcuts import render

# Create your views here.


def main(request):
    # context=default.defult()
    return render(request, 'info/main.html',)
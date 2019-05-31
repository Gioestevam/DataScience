from django.shortcuts import render

# Create your views here.
def dataScienceHtml(request):
    return render(request, 'importExcel.html', {})
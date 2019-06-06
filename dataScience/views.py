from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pandas as pda

# Create your views here.
def dataScienceHtml(request):
    if request.method == 'POST' and request.FILES['my_file']:
        my_file = request.FILES['my_file']
        fs = FileSystemStorage()
        filename = fs.save(my_file.name, my_file)
        fileUrl  = fs.url(filename)
        csvObject = pda.read_csv(fileUrl)
        print(csvObject.head(5))
        return render(request, 'graphic.html', { 'csvObjectColumns': csvObject.columns })
    return render(request, 'importExcel.html')
    
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pandas as pda
import json as json

# Create your views here.
def dataScienceHtml(request):
    if request.method == 'POST' and request.FILES['my_file']:
        my_file = request.FILES['my_file']
        fs = FileSystemStorage()
        filename = fs.save(my_file.name, my_file)
        fileUrl  = fs.url(filename)
        csvObject = pda.read_csv(fileUrl)
        LabelsColumns = json.dumps(csvObject.columns.values.tolist())
        valuesColumns = csvObject.values.tolist()
        typeCharts    = request.POST.get('group1')
        return render(
                    request, 
                    'graphic.html', 
                    { 
                        'labelsColumns': LabelsColumns, 
                        'valuesColumns': valuesColumns,
                        'typeChart':  typeCharts
                    }
                )
    return render(request, 'importExcel.html')

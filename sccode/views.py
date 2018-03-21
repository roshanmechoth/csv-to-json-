import csv
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def create_sccode(request,sccode):
    csv_file ={}
    file_location="EQ200318.CSV"
    with open("EQ200318.CSV") as file:
        reader = csv.reader(file)
        reader.next()
        for SC_CODE in reader:
            if sccode == SC_CODE[0]:
                csv_file['SC_CODE']=SC_CODE[0]
                csv_file['SC_NAME']=SC_CODE[1]
                csv_file['OPEN']=SC_CODE[4]
                csv_file['HIGH']=SC_CODE[5]
                csv_file['LOW']=SC_CODE[6]
                csv_file['CLOSE']=SC_CODE[7]
                response_data=csv_file
            else:
                response_data={"code":"404", "message":"No data"}
    return HttpResponse(json.dumps(response_data), content_type="application/json")





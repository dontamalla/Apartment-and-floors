from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.rest_frameworkresponse import rest_frameworkresponse
from app.models import Apartments
from app.models import Floors
import JSON

@api_view(['GET'])
def +getFloorinfo(request,id1):
    if request.method == 'GET':
        x = Apartments.objects.filter (id=id1)
        d1={}
        if len(x) == 0:
            return HttpResponse(status=404)
        else:
            list1=[]
            l2=[]
            for i in x:
                d={}
                d["floor_name"]=i.floor_name
                d["floor_number"]=i.floor_number
                d["id"]=i.id
                d["facility_id"]=ifacility_id
                d["active"]=i.active
                list1.append(d)
    

            floor_json = json.dumps(list1)
            for j in Apartments:
                c={}
                c["facility_name"]=j.facility_name
                c["id"]=j.id
                c["facility_type"]=j.facility_type
                c["company"]=j.company
                c["floors"]=j.floor_json
                l2.append(c)
            d1["Building"]=l2
            return Response(status=200, data=d1)






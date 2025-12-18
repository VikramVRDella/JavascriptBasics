from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StudentModel
from .serializers import StudentSerializers

# Create your views here.

class StudentAPI(APIView):
    def get(self,request,id=None):
        if id == None:
            fetch_all = StudentModel.objects.all()
            student_data=StudentSerializers(fetch_all,many=True).data
            return Response(student_data)
        else:
            fetch_one= StudentModel.objects.get(id = id)
            one_student= StudentSerializers(fetch_one).data
            return Response(one_student)
    
    def post(self,request):
        get_student = StudentSerializers(data=request.data)
        if get_student.is_valid():
            get_student.save()
            return Response({"message":"Student Added"})
        else:
            return Response({"message":get_student.errors})
    
    def patch(self,request,id):
        fetch_id = StudentModel.objects.get( id = id)
        update_student = StudentSerializers(fetch_id,data=request.data,partial=True)
        if update_student.is_valid():
            update_student.save()
            return Response({"message": "Student Updated"})
        else:
            return Response({"message" : update_student.errors})
        
    def delete(self,request,id):
        delete_student = StudentModel.objects.get(id = id)
        delete_student.delete()
        return Response({"message":"Student Deleted"})

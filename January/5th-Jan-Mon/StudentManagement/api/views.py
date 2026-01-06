# from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StudentModel
from .serializers import StudentSerializer

class StudentView(APIView):
    def get(self,request,id=None):
        if id == None:
            students=StudentModel.objects.all()
            fetch_all=StudentSerializer(students,many=True).data
            return Response(fetch_all)
        else:
            student=StudentModel.objects.get(id=id)
            fetch_one=StudentSerializer(student).data
            return Response(fetch_one)

    
    def post(self,request):
        get_student=StudentSerializer(data=request.data)
        if get_student.is_valid():
            get_student.save()
            return Response("Student Created")
        else:
            return Response(get_student.errors)
        
    def patch(self,request,id):
        get_id=StudentModel.objects.get(id=id)
        update_student= StudentSerializer(get_id,data=request.data,partial=True)
        if update_student.is_valid():
            update_student.save()
            return Response("Student Updated")
        else:
            return Response(update_student.errors)

    def put(self,request,id):
        get_id=StudentModel.objects.get(id=id)
        update_student= StudentSerializer(get_id,data=request.data)
        if update_student.is_valid():
            update_student.save()
            return Response("Student Updated")
        else:
            return Response(update_student.errors)
    
    def delete(self,request,id):
        get_id=StudentModel.objects.get(id=id)
        get_id.delete()
        return Response("Student Deleted")


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StudentModel
from .serializers import StudentSerializers

class StudentAPI(APIView):
    def get(self,request,id=None):
        try:
            if id ==None:
                all_students=StudentModel.objects.all()
                fetch_students=StudentSerializers(all_students,many=True).data
                return Response(fetch_students)
            else:
                one_student=StudentModel.objects.get(id=id)
                fetch_student=StudentSerializers(one_student).data
                return Response(fetch_student)
        except Exception as e:
            return Response({"Error":str(e)})
    def post(self,request):
        try:
            input_students=StudentSerializers(data=request.data)
            if input_students.is_valid():
                input_students.save()
                return Response("New Student Created...")
            else:
                return Response(input_students.errors)
        except Exception as e:
            return Response({"Error":str(e)})
    def patch(self, request, id=None):
        try:
            fetch = StudentModel.objects.get(id=id)
            update_student = StudentSerializers(fetch, data=request.data, partial=True)
            if update_student.is_valid():
                update_student.save()
                return Response("Student Details Updated...")
            else:
                return Response(update_student.errors)
        except Exception as e:
            return Response({"Error":str(e)})

    def delete(self,request,id=None):
        try:
            delete_student=StudentModel.objects.get(id=id)
            delete_student.delete()
            return Response("Student Deleted...")
        except Exception as e:
            return Response({"Error":str(e)})
    


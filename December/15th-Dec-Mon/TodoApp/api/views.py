from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TodoModel
from .serializers import TodoSerializers

class TodoAPI(APIView):
    def get(self,request,id=None):
        if id ==None:
            tasks=TodoModel.objects.all()
            task_serializers=TodoSerializers(tasks,many=True).data
            return Response(task_serializers)
        else:
            one_task=TodoModel.objects.get(id=id)
            task_serializer=TodoSerializers(one_task).data
            return Response(task_serializer)
    def post(self,request):
        create_task=TodoSerializers(data=request.data)
        if create_task.is_valid():
            create_task.save()
            return Response("New Task Added...")
        else:
            return Response(create_task.errors)
    def patch(self,request,id=None):
        task=TodoModel.objects.get(id=id)
        update_task=TodoSerializers(task,data=request.data,partial=True)
        if update_task.is_valid():
            update_task.save()
            return Response("Existing Task Updated...")
        else:
            return Response(update_task.errors)
    def delete(self,request,id=None):
        delete_task=TodoModel.objects.get(id=id)
        delete_task.delete()
        return Response("Task Deleted...")
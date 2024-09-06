from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Files
from .serializers import FilesSerializer
from django.core.files.storage import default_storage
from django.http import HttpResponse

# Create your views here.

class FileViewSet(viewsets.ViewSet):
    def upload(self, request):
        try:
            file = request.FILES['file']
        except:
            return Response({"error": "File not provided in request."}, status=status.HTTP_400_BAD_REQUEST)
        
        file_name = file.name
        file_size = file.size
        file_type = file.content_type

        file_path = default_storage.save(file_name, file)

        file_instance = Files.objects.create(
            file_name=file_name, file_size=file_size, file_type=file_type, file_path=file_path
        )

        return Response({"file_id": file_instance.id, "file_name":file_name, "file_size": str(file_size//1024)+" KB"}, status=status.HTTP_201_CREATED)


    def retrieve(self, request, pk=None):
        try:
            file_instance = Files.objects.get(id=pk)
            file_data = default_storage.open(file_instance.file_path.name, 'rb').read()

            response = HttpResponse(file_data, content_type=file_instance.file_type, status=status.HTTP_200_OK)
            response['Content-Disposition'] = f'attachment; filename="{file_instance.file_name}"'

            return response
        
        except Files.DoesNotExist:
            return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)


    def update(self, request, pk=None):
        try:
            file_instance = Files.objects.get(id=pk)
            if 'file' in request.FILES:
                ## delete old file, only file
                file_instance.file_path.delete()  
                file = request.FILES['file']
                file_instance.file_path = default_storage.save(file.name, file)
                file_instance.file_name = file.name
                file_instance.save()

            elif 'file_name' in request.data:
                file_instance.file_name = request.data.get('file_name', file_instance.file_name)
                print(request.data.get('file_name'))
                file_instance.save()
            
            else:
                return Response({"error": "No updates povided.", "msg": "Either you can update the complete file or update the name only. Didn't got any of those updates."}, status=status.HTTP_400_BAD_REQUEST)

            return Response({"message": "File updated successfully"}, status=status.HTTP_200_OK)
        
        except Files.DoesNotExist:
            return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, pk=None):
        try:
            file_instance = Files.objects.get(id=pk)
            file_instance.file_path.delete()
            file_instance.delete()

            return Response({"message": f"File deleted with id {pk}"}, status=status.HTTP_200_OK)
        
        except Files.DoesNotExist:
            return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)


    def list_files(self, request):
        files = Files.objects.all()
        serializer = FilesSerializer(files, many=True)

        return Response(serializer.data)
    



def index(request):
    html = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Dropbox-Like Service</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 20px;
                        background-color: #f9f9f9;
                        text-align: center;
                        
                    }
                    h1 {
                        color: #333;
                        
                    }
                </style>
            </head>
            <body>

            <h1>Dropbox-Like Service</h1>
            <p>
            Backend Server is live now <br>
            APIs can be tested according to documentation.
            <p>
               
            </body>
            </html>
    """
    

    return HttpResponse(html)

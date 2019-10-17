from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import FileSerializer
from .docx import getText
from .pdf import getPdfText
from .txt import get_txt_word
class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
         
        filedata = {}

        file_serializer = FileSerializer(data=request.FILES)
        if file_serializer.is_valid():
            file = file_serializer.save()
            
            
            file1_path = file_serializer['file1'].value
            file2_path = file_serializer['file2'].value

            file1 = file_serializer.validated_data['file1']
            file2 = file_serializer.validated_data['file2']
            #   file1path = file_to_string(filetosave.file.path)

            file1_extension = file1.name.split('.')[1].lower()
            file2_extension = file2.name.split('.')[1].lower()


            try:
                if file1_extension == 'docx' :
                    filedata['file1']=getText(file1)
                if file1_extension == 'pdf':
                    filedata['file1']= getPdfText(file1_path)
                if file1_extension == 'txt':
                    filedata['file1'] = get_txt_word(file1_path)
                if file2_extension == 'docx' :
                    filedata['file2']= getText(file2)
                if file2_extension == 'pdf':
                    filedata['file2']= getPdfText(file2_path)
                if file2_extension == 'txt':
                    filedata['file2'] = get_txt_word(file2_path)
                else:
                    return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


                return Response(filedata)
            except:
                return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def my_first_api(request):
    return Response({
        "status":"Success",
        "message":"hurrah! i made my first API successfully."
    })
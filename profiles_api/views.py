from rest_framework.views import APIView
from rest_framework.views import Response


class HelloApiView(APIView):

  def get(self,request,fromat =None):

    an_apiview = [
      'Uses HTTP methods as function (get,put,post,patch,delete) ',
      'Is similar to traditional django view',
      'Gives you the most control over your logic',
    ]

    return Response({'message' : 'Helllo!','an_apiview' : an_apiview})


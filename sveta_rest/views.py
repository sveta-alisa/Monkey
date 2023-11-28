from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Profile
from .serializers import ProfileSerializer


# Create your views here.


@api_view(['GET'])
def get_api_page(request):
    profile = Profile.objects.all()
    serializer = ProfileSerializer(profile, many=True)
    # for i in profile:
    #     serializer = ProfileSerializer(i)
    return Response(serializer.data)

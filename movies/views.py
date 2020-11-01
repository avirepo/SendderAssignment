from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.helpers import get_movies_data


class MoviesList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'movies.html'

    def get(self, request, *args, **kwargs):
        movies = get_movies_data()
        return Response({'movies': movies})

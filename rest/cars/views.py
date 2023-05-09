from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .models import Car, Category
from .serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    """ Отображать домашнюю страницу и добавленные посты по id"""
    serializer_class = CarSerializer

    def get_queryset(self: object) -> Response:
        pk = self.kwargs.get('pk')
        if not pk:
            return Car.objects.all()[:2]
        return Car.objects.filter(pk=pk)

    @action(methods=['get'], detail=False)
    def category(self, request: object) -> Response:
        cats = Category.objects.all()

        return Response({'cats': [i.name for i in cats]})


class CarAPIViews(generics.RetrieveUpdateDestroyAPIView):
    """ Отображение списка на странице с возможностью добавления"""
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarAPIList(generics.ListCreateAPIView):
    """ Отображение списка на странице"""
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# def index_html(request):
#
#     ind = Car.objects.all()
#     return render(request, 'cars/index.html', {'ind': ind})

# def about(request):
#     data = request.GET.get('qwe')
#     print(data)
#     return render(request, 'cars/about.html')

class ProfileList(APIView):
    """ Отображение на странице"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cars/about.html'

    def get(self, request) -> Response:
        queryset = Car.objects.all()
        return Response({'profiles': queryset})

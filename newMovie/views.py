from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from .models import newMovieModel
from .serializers import MoviesSerializer
from newMovie.models import newMovieModel


# Homepage - localhost/index
#search with localhost/id
def index(request):
    return render(request, 'home.html')


# data with serialization, localhost/id=1,2..
def movies_review(request, pk):
    mov = newMovieModel.objects.get(id=pk)
    serializer = MoviesSerializer(mov)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

#search - local/index
def search(request):
    query = request.GET['query']
    allmovies = newMovieModel.objects.filter(name__icontains=query)
    params = {'allmovies': allmovies}
    return render(request, 'search.html',params)


def insertmovie(request):
    if request.method == 'POST':
        if request.POST.get('moviename') and request.POST.get('directorname') and request.POST.get(
                'genretype') and request.POST.get('movieratings') and request.POST.get('dateofrelease'):

                    New_Movie = newMovieModel()
                    New_Movie.name = request.POST.get('moviename')
                    New_Movie.director = request.POST.get('directorname')
                    New_Movie.genre = request.POST.get('genretype')
                    New_Movie.ratings = request.POST.get('movieratings')
                    New_Movie.date = request.POST.get('dateofrelease')
                    New_Movie.save()
        return render(request, 'home.html')
    else:
            return render(request, 'home.html')


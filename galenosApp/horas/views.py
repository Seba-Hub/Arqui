from django.shortcuts import render
# Create your views here.
posts = [
    {
        'hora': '13:00',
        'doctor': 'Felipe Barrios',
        'especialidad': 'Odontologia',
        'publicada_en': 'October 1, 2022'
    },
    {
        'hora': '13:30',
        'doctor': 'Javiera Barrios',
        'especialidad': 'Dermatologia',
        'publicada_en': 'October 1, 2022'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'horas/home.html', context)
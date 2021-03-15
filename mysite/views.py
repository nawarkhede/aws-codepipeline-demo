from django.http import HttpResponse


def index(request):
    return HttpResponse(
        "Hello world from Nawarkhede, AWS is awseome infrastructure. You should learn it."
    )

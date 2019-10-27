from django.shortcuts import render
from htmlmin.decorators import minified_response


@minified_response
def index(request):

    response = render(request, "core/index.html")
    response["Cache-Control"] = "public, max-age=300, stale-while-revalidate=2592000, stale-if-error=2592000"
    return response

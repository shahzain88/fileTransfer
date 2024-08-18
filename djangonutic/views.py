from django.http import HttpResponse
from django.shortcuts import render
from json import dumps


def view_robot_txt(request):
    return render(request, "robots.txt")


def view_manifest_json(request):
    responseData = data = {
        "in_the_allah_name": "بِسْمِٱللَّهِٱلرَّحْمَٰنِٱلرَّحِيمِ",
        "short_name": "Shinfuji",
        "name": "Shinfuji co ., ltd.",
        "icons": [
            {
                "src": "/static/logo.ico",
                "sizes": "64x64 32x32 24x24 16x16",
                "type": "image/x-icon"
            },
            {
                "src": "/static/logo.png",
                "type": "image/png",
                "sizes": "192x192"
            },
            {
                "src": "/static/logo.png",
                "type": "image/png",
                "sizes": "512x512"
            }
        ],
        "start_url": ".",
        "display": "standalone",
        "theme_color": "#000000",
        "background_color": "#ffffff"
    }

    return HttpResponse(dumps(responseData), content_type="application/json")


def view_404(request):
    return render(request, "404.html")


def homepage(request):
    # return HttpResponse("Home or / ")
    return render(request, "homepage.html")


def about(request):
    # return HttpResponse('About')
    return render(request, "about.html")

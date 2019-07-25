from django.shortcuts import render

def home_page(request):
    context = {
        "title": "Welcome",
        "header": "NEWASSETCMS Home",
        "subheader": "Which is a shortcut for New Asset Content Management System",
        "copyright": "Copyright © 2019 H.L.W. Smulders",
    }
    if request.user.is_authenticated:
        context["loggedin_content"] = "Content only visible when logged in ..."
    return render(request, 'home/index.html', context)

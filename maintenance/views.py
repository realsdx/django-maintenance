from django.shortcuts import render

# Create your views here.
def page_503(req):
    return render(req,'maintenance/503_page.html',{}, status=503)
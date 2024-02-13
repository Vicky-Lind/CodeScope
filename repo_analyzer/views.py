from django.shortcuts import render
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def index(request):
    url = ''
    if request.method == "POST":
        url = request.POST['url']
        print(url)
    return render(request, 'repo_analyzer/index.html', {'url': url})
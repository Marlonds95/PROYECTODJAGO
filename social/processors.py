from .models import Social

def ctx_dict(request):
    dict_urls={}
    urls= Social.objects.all()
    for url in urls:
        dict_urls[url.key]=url.url


    return dict_urls


from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Setting, Advertisement, Basement, Scheme, Scholarship, Article, Counselor, Student, Subscriber, Storage

def robots(request):
    lines = [
        "User-agent: *",
        "Allow: /static/",
        "Allow: /media/",
        "Disallow: /admin/",
        f"Sitemap: {request.build_absolute_uri('/sitemap.xml')}"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def index(request):
    setting = Setting.objects.first()
    scheme = Scheme.objects.filter(active=True).first()
    advertisement = scheme.advertisement.first() if scheme else None
    scholarship = Scholarship.objects.filter(active=True)
    article = Article.objects.filter(active=True)
    counselor = Counselor.objects.first()

    data = {
        'setting': setting,
        'ads': advertisement,
        'scheme': scheme,
        'scholarship': scholarship,
        'articles': article,
        'counselor': counselor
    }

    return render(request, 'index.html', data)


def scholarship(request, slug):
    
    setting = Setting.objects.first()
    scholar = get_object_or_404(Scholarship, slug=slug, active=True)
    advertisement = scholar.advertisement.first() if scholar else None
    scheme = Scheme.objects.filter(active=True).first()
    scholarship = Scholarship.objects.filter(active=True)
    article = Article.objects.filter(active=True)
    counselor = Counselor.objects.first()

    data = {
        'setting': setting,
        'ads': advertisement,
        'scheme': scheme,
        'scholarship': scholarship,
        'articles': article,
        'scholar': scholar,
        'counselor': counselor
    }

    return render (request, 'scholar.html', data)


def article(request, slug):
    
    setting = Setting.objects.first()
    arti = get_object_or_404(Article, slug=slug, active=True)
    advertisement = arti.advertisement.first() if arti else None
    scheme = Scheme.objects.filter(active=True).first()
    scholarship = Scholarship.objects.filter(active=True)
    article = Article.objects.filter(active=True)
    counselor = Counselor.objects.first()

    data = {
        'setting': setting,
        'ads': advertisement,
        'scheme': scheme,
        'scholarship': scholarship,
        'articles': article,
        'arti': arti,
        'counselor': counselor
    }

    return render (request, 'article.html', data)

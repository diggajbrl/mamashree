from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
    counselor = Counselor.objects.first()
    article = Article.objects.filter(active=True)
    scheme = Scheme.objects.filter(active=True).first()
    scholarship = Scholarship.objects.filter(active=True)
    advertisement = scheme.advertisement.first() if scheme else None

    data = {
        'scheme': scheme,
        'setting': setting,
        'articles': article,
        'ads': advertisement,
        'counselor': counselor,
        'scholarship': scholarship
    }

    return render(request, 'index.html', data)


def scholarship(request, slug):
    
    setting = Setting.objects.first()
    counselor = Counselor.objects.first()
    article = Article.objects.filter(active=True)
    scheme = Scheme.objects.filter(active=True).first()
    scholarship = Scholarship.objects.filter(active=True)
    scholar = get_object_or_404(Scholarship, slug=slug, active=True)
    advertisement = scholar.advertisement.first() if scholar else None

    data = {
        'scheme': scheme,
        'setting': setting,
        'scholar': scholar,
        'articles': article,
        'ads': advertisement,
        'counselor': counselor,
        'scholarship': scholarship
    }

    return render (request, 'scholar.html', data)


def article(request, slug):
    
    setting = Setting.objects.first()
    counselor = Counselor.objects.first()
    article = Article.objects.filter(active=True)
    scheme = Scheme.objects.filter(active=True).first()
    scholarship = Scholarship.objects.filter(active=True)
    arti = get_object_or_404(Article, slug=slug, active=True)
    advertisement = arti.advertisement.first() if arti else None

    data = {
        'arti': arti,
        'scheme': scheme,
        'setting': setting,
        'articles': article,
        'ads': advertisement,
        'counselor': counselor,
        'scholarship': scholarship
    }

    return render (request, 'article.html', data)

@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(f'Received email: {email}')

        if email:
            email = email.lower()
            try:
                subscriber = Subscriber.objects.get(email__iexact=email)
                return JsonResponse({'status': 'error', 'message': 'Email already exists'})
            except Subscriber.DoesNotExist:
                Subscriber.objects.create(email=email)
                return JsonResponse({'status': 'success', 'message': 'Successfully Subscribed'})

        return JsonResponse({'status': 'error', 'message': 'Invalid email address!'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method!'})
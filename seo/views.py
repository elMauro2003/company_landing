from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.template.loader import render_to_string
from apps.general.models import Services

def robots(request):
    return render(request, "txts/robots.txt", context={"domain_url": "https://example.com"}, content_type="text/plain")

def security(request):
    return render(request, "txts/security.txt", content_type="text/plain")

def humans(request):
    return render(request, "txts/humans.txt", content_type="text/plain")

def sitemap(request):
    """Sitemap txt"""
    # Get all published posts
    services = list(Services.objects.all())
    
    for service in services:
        print(service.title)
    
    services_all_urls = [service.get_absolute_url() for service in services]
    
    for url in services_all_urls:
        print(url)
    
    # Remove empty lines
    text_with_empty_lines = render_to_string(
        "sitemap.txt",
        {
            "posts": services_all_urls,
        },
    )
    text_without_empty_lines = "\n".join([line.strip() for line in text_with_empty_lines.splitlines() if line.strip()])
    # Render sitemap txt
    return HttpResponse(text_without_empty_lines, content_type="text/plain")

def handler404(request, *args, **argv):
    return render(request, "seo/404.html", status=404)

def handler500(request, *args, **argv):
    return render(request, "seo/500.html", status=500)
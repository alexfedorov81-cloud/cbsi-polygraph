# core/views.py
from django.shortcuts import render
from services.models import Service
from reviews.models import Review
from core.models import SiteSettings, PrivacyPolicy, ResearchInfo
import time

def home(request):
    settings = SiteSettings.objects.first()

    # Получаем данные
    services = Service.objects.filter(is_active=True).order_by('order')
    reviews = Review.objects.filter(is_published=True).order_by('-created_at')[:6]
    research_info = ResearchInfo.objects.filter(is_active=True).first()

    context = {
        'services': services,
        'reviews': reviews,
        'settings': settings,
        'research_info': research_info,
        # Добавляем специфичные версии для каждого блока
        'RESEARCH_VERSION': research_info.updated_at.timestamp() if research_info and hasattr(research_info,
                                                                                              'updated_at') else 0,
        'SERVICES_VERSION': services.last().updated_at.timestamp() if services.exists() and hasattr(services.last(),
                                                                                                    'updated_at') else 0,
        'REVIEWS_VERSION': reviews.first().created_at.timestamp() if reviews.exists() else 0,
    }

    return render(request, 'core/home.html', context)


def privacy_policy(request):
    policy = PrivacyPolicy.objects.first()
    settings = SiteSettings.objects.first()

    context = {
        'policy': policy,
        'settings': settings,
        'GLOBAL_VERSION': int(time.time()),
        'SITE_VERSION': settings.cache_version if settings else int(time.time()),
    }
    return render(request, 'includes/privacy_policy.html', context)

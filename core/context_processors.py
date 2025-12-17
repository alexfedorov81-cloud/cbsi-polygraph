import time

def static_version(request):
    timestamp = int(time.time())
    return {
        'STATIC_VERSION': f'v{timestamp}',
        'STATIC_TIMESTAMP': timestamp,
    }

def cache_versions(request):
    timestamp = int(time.time())
    return {
        'GLOBAL_VERSION': timestamp,
        'SITE_VERSION': timestamp,
        'CACHE_BUSTER': f'v{timestamp}',
        'RESEARCH_VERSION': timestamp,
        'SERVICES_VERSION': timestamp,
        'REVIEWS_VERSION': timestamp,
    }

# Add to INSTALLED_APPS:
INSTALLED_APPS = [
    ...
    'rest_framework',
    'corsheaders',
    'drf_yasg',
    'listings',
]

# Add middleware:
MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
]

# Add at bottom:
CORS_ALLOW_ALL_ORIGINS = True

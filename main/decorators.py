from django.utils import timezone

def log_request(func):
    def wrapper(request, *args, **kwargs):
        print(f"[{timezone.now()}] Request to {request.path} from {request.user}")
        return func(request, *args, **kwargs)
    return wrapper

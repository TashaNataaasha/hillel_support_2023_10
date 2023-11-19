from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import ActivationKey, User

@csrf_exempt
def activate_user(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        activation_key = get_object_or_404(ActivationKey, key=key)
        user = activation_key.user
        user.is_active = True
        user.save()
        activation_key.delete()

        send_mail(
            'Your email is successfully activated',
            'Your email is successfully activated',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

        return JsonResponse({'message': 'User activated successfully'})

    return JsonResponse({'message': 'Invalid request method'})
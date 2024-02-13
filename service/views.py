from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from .models import ReferralCode, Referrer
from .serializers import ReferralCodeSerializer, ReferrerSerializer
from authentication.models import CustomUser
from drfasyncview import AsyncAPIView
from django.http import JsonResponse
from asgiref.sync import sync_to_async


class ReferralCodeCreateAPIView(AsyncAPIView):
    serializer_class = ReferralCodeSerializer
    permission_classes = [IsAuthenticated]

    @sync_to_async
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)


class ReferralCodeUpdateAPIView(AsyncAPIView):
    serializer_class = ReferralCodeSerializer
    lookup_field = 'pk'
    partial = True
    permission_classes = [IsAuthenticated]


    @sync_to_async(thread_sensitive=False)
    def patch(self, request, *args, **kwargs):
        code = kwargs.get('code', None)

        access_token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        token = AccessToken(access_token)
        user_id = token.payload['user_id']
        owner_id = ReferralCode.objects.get(code=code).owner_id

        if not code:
            return JsonResponse({"error": f"There is no code for <{code}>"})

        if user_id == owner_id:
            instance = ReferralCode.objects.get(code=code)
            serializer = self.serializer_class(data=request.data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({"error": f"You do not have the rights to update {code}"},
                                status=status.HTTP_400_BAD_REQUEST)


class ReferralCodeDeleteAPIView(AsyncAPIView):
    permission_classes = [IsAuthenticated]

    @sync_to_async(thread_sensitive=False)
    def delete(self, request, *args, **kwargs):

        access_token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        token = AccessToken(access_token)
        user_id = token.payload['user_id']

        code = kwargs.get('code', None)
        owner_id = ReferralCode.objects.get(code=code).owner_id

        if not code:
            return JsonResponse({"error": f"There is no code for <{code}>"})

        if user_id == owner_id:
            ReferralCode.objects.get(code=code).delete()
            return JsonResponse({"delete": True}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"error": f"You do not have the rights to delete {code}"},
                                status=status.HTTP_400_BAD_REQUEST)


class ReferralCodeSearchAPIView(AsyncAPIView):
    permission_classes = [IsAuthenticated]
    @sync_to_async(thread_sensitive=False)
    def get(self, request, *args, **kwargs):
        email = self.request.query_params.get('email')
        user_id = CustomUser.objects.get(email=email).pk
        try:
            code = ReferralCode.objects.get(owner_id=user_id, is_active=True)
            return JsonResponse({'status': 'valid', 'code': f'{code}'}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({'status': 'invalid',
                                 'error': f'The user with {email} does not have active referral codes'},
                                status=status.HTTP_404_NOT_FOUND)


class ReferrerCreateAPIView(AsyncAPIView):
    serializer_class = ReferrerSerializer
    permission_classes = [IsAuthenticated]

    @sync_to_async(thread_sensitive=False)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)


class ReferrerSearchAPIView(AsyncAPIView):
    @sync_to_async(thread_sensitive=False)
    def get(self, request):
        referrer_id = self.request.query_params.get('referrer_id')
        referres = Referrer.objects.filter(owner_id=referrer_id).values()
        return JsonResponse(list(referres), safe=False)

from rest_framework.generics import DestroyAPIView, CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner


from .models import ReferralCode, Referrer
from .serializers import ReferralCodeSerializer, ReferrerSerializer
from authentication.models import CustomUser


class ReferralCodeCreateAPIView(CreateAPIView): # POST
    queryset = ReferralCode.objects.all()
    serializer_class = ReferralCodeSerializer
    # permission_classes = [IsAuthenticated]


class ReferralCodeUpdateAPIView(UpdateAPIView): #  PATCH
    queryset = ReferralCode.objects.all()
    serializer_class = ReferralCodeSerializer
    lookup_field = 'pk'
    partial = True
    permission_classes = [IsAuthenticated, IsOwner]


class ReferralCodeDeleteAPIView(DestroyAPIView): # DELETE
    queryset = ReferralCode.objects.all()
    serializer_class = ReferralCodeSerializer
    permission_classes = [IsAuthenticated, IsOwner]



class ReferralCodeSearchAPIView(ListAPIView):
    serializer_class = ReferralCodeSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email')
        user_id = CustomUser.objects.get(email=email).pk
        queryset = ReferralCode.objects.filter(owner_id=user_id, is_active=True)
        return queryset


class ReferrerCreateAPIView(CreateAPIView): # POST
    queryset = Referrer.objects.all()
    serializer_class = ReferrerSerializer


class ReferrerSearchAPIView(ListAPIView):
    serializer_class = ReferrerSerializer

    def get_queryset(self):
        referral_id = self.request.query_params.get('referral_id')
        queryset = Referrer.objects.filter(owner_id=referral_id)
        return queryset

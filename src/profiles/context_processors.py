from .models import Profile, Relationship

def profile_pic(request):
    if request.user.is_authenticated:
        try:
            profile_obj = Profile.objects.get(user__id=request.user.id)
        except Profile.DoesNotExist:
            return {}
        pic = profile_obj.avatar
        return {'picture':pic}
    return {}


def invatations_received_no(request):
    if request.user.is_authenticated:
        try:
            profile_obj = Profile.objects.get(user__id=request.user.id)
        except Profile.DoesNotExist:
            return {}
        qs_count = Relationship.objects.invatations_received(profile_obj).count()
        return {'invites_num':qs_count}
    return {}
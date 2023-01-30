


def even_number(value):
    if value % 2 != 0:
        raise serializers.ValidationError('This field must be an even number.')

    
def validateExists(user):
    try:

        employer=Employer.objects.get(user=user)
    except ObjectDoesNotExist:
        raise serializers.ValidationError('Employer not valid.') 

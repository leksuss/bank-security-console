from django.utils.timezone import localtime
from django.shortcuts import render

from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter import utils


def storage_information_view(request):

    visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []
    for visit in visits:
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': localtime(visit.entered_at),
                'duration': utils.format_duration(visit.get_duration()),
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter import utils


def passcard_info_view(request, passcode):

    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for visit in visits:
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': utils.format_duration(visit.get_duration()),
                'is_strange': utils.is_strange_visit(visit.get_duration()),
            },
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

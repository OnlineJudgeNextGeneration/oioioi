from django.core.urlresolvers import reverse
from oioioi.contests.models import ContestController

class DashboardDefaultViewMixin(object):
    def default_view(self, request):
        return reverse('contest_dashboard', kwargs={'contest_id': self.contest.id})
ContestController.mix_in(DashboardDefaultViewMixin)

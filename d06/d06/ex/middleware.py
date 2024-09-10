import random
from django.conf import settings
from django.utils import timezone
from datetime import timedelta

class RandomVisitorUsername:
    def __init__(self, get_response):
        self.get_response = get_response
        self.usernames = getattr(settings, 'USERNAMES')

    def __call__(self, request):
        # current_time = timezone.now()
        # last_assigned = request.session.get('last_assigned')
        # if last_assigned:
        #     last_assigned = timezone.datetime.fromisoformat(last_assigned)

        # # if no username given or assigned over 42s ago
        # if not last_assigned or (current_time - last_assigned) > timedelta(seconds=42):
        #     request.session['username'] = random.choice(self.usernames)
        #     request.session['last_assigned'] = current_time.isoformat()

        if not request.session.get('username'):
            request.session['username'] = random.choice(self.usernames)
            request.session.set_expiry(42)

        response = self.get_response(request)
        return response
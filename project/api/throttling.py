from rest_framework.throttling import AnonRateThrottle

class AnonaymousUserThrottle(AnonRateThrottle):
    scope = 'review'

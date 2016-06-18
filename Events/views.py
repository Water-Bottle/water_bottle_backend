import logging
import datetime
from django.shortcuts import render
from django.http import HttpResponse


# Global (file-specific) definitions
####################################
LOGGER = logging.getLogger(__name__)


def server_time(request):
    """
    Test view to return current time on server (to test if server
    is working ...)
    """
    current_time = str(datetime.datetime.now())
    LOGGER.info('time is ' + current_time)
    return HttpResponse(current_time)

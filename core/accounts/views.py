from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_page
from .tasks import sendEmail
import requests


def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Done Sending</h1>")


@cache_page(60)
def test(request):
    response = requests.get(
        "https://66eb931a-57a8-429d-9656-7a2029901d3b.mock.pstmn.io/test/delay/5"
    )
    return JsonResponse(response.json())

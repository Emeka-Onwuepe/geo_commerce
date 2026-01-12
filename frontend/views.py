from django.shortcuts import render

from frontend.load_location import get_outlets



# Create your views here.
def home(request):
    return render(request, "frontend/index.html")


def location(request):
    """Receive latitude/longitude via GET and return a small HTML snippet.

    HTMX will request this endpoint with query parameters `lat` and `lon`.
    """
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    if lon == 'NaN' and lat == "NaN":
        context = {'error':True}
        return render(request, "partials/outlets.html", context)    
    reg = get_outlets(lat,lon)

    context = {"lat": lat, "lon": lon,"error":False, 'regs':reg}
    return render(request, "partials/outlets.html", context)
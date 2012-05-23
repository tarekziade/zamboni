import jingo

from mkt.webapps.models import Webapp


def home(request):
    """The home page."""
    if not getattr(request, 'can_view_consumer', True):
        return jingo.render(request, 'home/home_walled.html')
    featured = Webapp.featured('home')[:3]
    popular = Webapp.popular()[:6]
    return jingo.render(request, 'home/home.html', {
        'featured': featured,
        'popular': popular
    })
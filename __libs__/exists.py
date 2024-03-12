

def shortlink_exists(url):
    """

    """
    from shortlink.models import ShortLink
    return ShortLink.objects.filter(original_link=url).exists()
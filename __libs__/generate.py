
from shortlink.__libs__.exists import shortlink_exists
import random

def __generate_path_shortcutlink(_in) -> str:
    """
    Generate the path for the shortlink.

    Args:
        _in: The shortlink interface.
    """
    characters = _in.characters
    length = 6
    return ''.join(random.choice(characters) for i in range(length))

def create_shortlink(_in, url: str) -> str:
    """
    Generate a shortlink.

    Args:
        interface: The shortlink interface.
        url: The url to shorten.
    """
    from shortlink.models import ShortLink
    from shortlink.rules.stack import SHORTLINK_RULESTACK

    dbShortlink = ShortLink.objects.filter(original_link=url)
    if dbShortlink.exists():
        return dbShortlink.first()
    
    while True:
        short_link = __generate_path_shortcutlink(_in)
        print (short_link)
        if ShortLink.objects.filter(short_link=short_link).exists():
            continue

        dbShortlink = ShortLink(
            interface=_in.label,
            original_link=url,
            short_link=short_link
        )
        dbShortlink.save()
        break
    return dbShortlink


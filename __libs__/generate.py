

def __generate_path_shortcutlink(_in) -> str:
    """
    Generate the path for the shortlink.

    Args:
        _in: The shortlink interface.
    """
    

def generate_shortlink(_in, url: str) -> str:
    """
    Generate a shortlink.

    Args:
        interface: The shortlink interface.
        url: The url to shorten.
    """
    from shortlink.models import Shortlink
    from shortlink.rules.stack import SHORTLINK_RULESTACK

    _in.event_before_generate(url)
    dbShortlink = Shortlink(
        label=_in.label,
        original_link=url,
        short_link=__generate_path_shortcutlink(_in)
    )
    dbShortlink.save()
    _in.event_after_generate(dbShortlink)

    return dbShortlink


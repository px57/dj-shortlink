


def redirect_shortlink(url: str, **kwargs) -> str:
    """
    Click on a shortlink.

    Args:
        url: The shortlink url.
        **save: Save the click -> load the link_manager.
    """
    from shortlink.models import Shortlink
    from shortlink.rules.stack import SHORTLINK_RULESTACK


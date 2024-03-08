
from shortlink.rules.stack import SHORTLINK_RULESTACK
from kernel.interfaces.interfaces import InterfaceManager

"""
Is an list of characters used by all the interface. 
"""
NUMBER_SHORT_LINK_GENERATED = {}

class DefaultRuleClass(InterfaceManager):
    """
    The default rule class. 
    """

    """
    The label to identify the rule interface.
    """
    label = 'DEFAULT'

    """
    The allow flag to enable or disable the rule.
    """
    allow = True

    """
    The list of characters to generate the short link.
    """
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    def __init__(self) -> None:
        """
        The constructor of the class.
        """
        super().__init__()

    def load_number_short_link_generated(self):
        """
        Load the number of used characters by interface.
        """
        global NUMBER_SHORT_LINK_GENERATED
        from shortlink.models import ShortLink
        if self.label not in NUMBER_SHORT_LINK_GENERATED:
            NUMBER_SHORT_LINK_GENERATED[self.label] = ShortLink.objects.filter(interface=self.label).count()
        return NUMBER_SHORT_LINK_GENERATED[self.label]
    
    def increment_number_short_link_generated(self):
        """
        Increment the number of used characters by interface.
        """
        global NUMBER_SHORT_LINK_GENERATED
        if self.label not in NUMBER_SHORT_LINK_GENERATED:
            self.load_number_short_link_generated()
        NUMBER_SHORT_LINK_GENERATED[self.label] += 1
        return NUMBER_SHORT_LINK_GENERATED[self.label]
    
    def get_number_short_link_generated(self):
        """
        Get the number of used characters by interface.
        """
        if self.label not in NUMBER_SHORT_LINK_GENERATED:
            return self.load_number_short_link_generated()
        return NUMBER_SHORT_LINK_GENERATED[self.label]
    
    def shortlink_length_now(self):
        """
        Get the number of characters to generate the new short link.
        """
        used = self.get_number_short_link_generated()
        characters_length = len(self.characters)

    def viewcreate__get_url(self):
        """
        Get the url to create the short link.
        """
        return self.request.POST.get('url', None)
    
SHORTLINK_RULESTACK.set_rule(DefaultRuleClass)
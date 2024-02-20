
from shortlink.rules.stack import SHORTCUT_RULESTACK
from kernel.interfaces.interfaces import InterfaceManager

"""
Is an list of characters used by all the interface. 
"""
NUMBER_USED_CHARACTERS_BY_INTERFACE = {}

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
        super().__init__()

    def load_number_used_characters_by_interface(self):
        """
        Load the number of used characters by interface.
        """
        global NUMBER_USED_CHARACTERS_BY_INTERFACE
        from shortlink.models import ShortLink
        if self.label not in NUMBER_USED_CHARACTERS_BY_INTERFACE:
            NUMBER_USED_CHARACTERS_BY_INTERFACE[self.label] = ShortLink.objects.filter(interface=self.label).count()
        return NUMBER_USED_CHARACTERS_BY_INTERFACE[self.label]
    
    def increment_number_used_characters_by_interface(self):
        """
        Increment the number of used characters by interface.
        """
        global NUMBER_USED_CHARACTERS_BY_INTERFACE
        if self.label not in NUMBER_USED_CHARACTERS_BY_INTERFACE:
            self.load_number_used_characters_by_interface()
        NUMBER_USED_CHARACTERS_BY_INTERFACE[self.label] += 1
        return NUMBER_USED_CHARACTERS_BY_INTERFACE[self.label]
    
    def get_number_used_characters_by_interface(self):
        """
        Get the number of used characters by interface.
        """
        if self.label not in NUMBER_USED_CHARACTERS_BY_INTERFACE:
            return self.load_number_used_characters_by_interface()
        return NUMBER_USED_CHARACTERS_BY_INTERFACE[self.label]
    

SHORTCUT_RULESTACK.set_rule(DefaultRuleClass())
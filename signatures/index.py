from dspy import Signature, InputField, OutputField

class GenerateTarotDescription(Signature):
    """Create a description of tarot card for given character."""
    universe_name = InputField(desc="Name of the universe where character belongs")
    charactor_name = InputField(desc="Name of the character to generate description for")
    person_name = InputField(desc="Name of the person for whom to generate tarod card description")
    tarot_card_description = OutputField(desc="detailed description of tarot card")

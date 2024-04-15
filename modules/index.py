import dspy
from signatures.index import GenerateTarotDescription

class RAG(dspy.Module):
    def __init__(self, num_passages=3):
        super().__init__()
        self.generate_tarot_description = dspy.ChainOfThought(GenerateTarotDescription)
    
    def forward(self, universe_name, charactor_name, person_name):
        # context = self.retrieve(question).passages
        tarot_description = self.generate_tarot_description(
            universe_name=universe_name, 
            charactor_name=charactor_name, 
            person_name=person_name
        )
        return dspy.Prediction(description=tarot_description.tarot_card_description)
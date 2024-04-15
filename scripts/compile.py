from dspy.teleprompt import BootstrapFewShot
from modules.index import RAG
from dspy import Example
import dspy
import json

# Using a with statement to ensure the file is properly closed after its suite finishes

ollama_model = dspy.OpenAI(api_base='http://localhost:11434/v1/', api_key='ollama', model='mistral:7b-instruct-v0.2-q6_K', stop='\n\n', model_type='chat')
dspy.settings.configure(lm=ollama_model)

with open('data/training_data.json', 'r') as file:
    dataset = json.load(file)
keys = set(dataset['inputs'][0].keys())
keys.remove('tarot_card_description')
examples = []
for example in dataset['inputs']:
    examples.append(Example(base=example).with_inputs(*keys))

teleprompter = BootstrapFewShot()
compiled_rag = teleprompter.compile(RAG(), trainset=examples)

compiled_rag.save("./data/compiled_data.json")

universe_name = "Harry Potter"
charactor_name = "Dumbledore"
person_name = "Mugdha Pawar"
tarot_card_description = compiled_rag(universe_name=universe_name, charactor_name=charactor_name, person_name=person_name)
print(tarot_card_description)









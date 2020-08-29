import pickle
from jina.executors.crafters.nlp.split import Sentencizer


class CustomSentencizer(Sentencizer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def craft(self, text, *args, **kwargs):
        with open("input_crafter.pkl", 'wb') as f:
            pickle.dump((text, args, kwargs), f)
        results = super().craft(text, *args, **kwargs)
        with open("output_crafter.pkl", 'wb') as f:
            pickle.dump(results, f)
        return results
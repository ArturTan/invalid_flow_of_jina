import pickle
from jina.executors.encoders.nlp.transformer import TransformerTorchEncoder


class CustomEncoder(TransformerTorchEncoder):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def encode(self, *args, **kwargs):
        with open(f"input_encoder.pkl", 'wb') as f:
            pickle.dump((args, kwargs), f)
        result = super().encode(*args, **kwargs)
        with open(f"output_encoder.pkl", 'wb') as f:
            pickle.dump(result, f)
        return result

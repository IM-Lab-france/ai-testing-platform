from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace

# Charger un tokenizer pré-entraîné ou entraîner un nouveau tokenizer
# Ici, nous utilisons un tokenizer BPE (Byte Pair Encoding) pour l'exemple
def get_tokenizer():
    tokenizer = Tokenizer(BPE())
    tokenizer.pre_tokenizer = Whitespace()
    # Entraîner le tokenizer sur un corpus (ici, un exemple simple)
    trainer = BpeTrainer(vocab_size=30000, show_progress=False)
    tokenizer.train_from_iterator(["This is a sample text for tokenizer training."], trainer=trainer)
    return tokenizer

tokenizer = get_tokenizer()

def count_tokens(text: str) -> int:
    """
    Compte le nombre de tokens dans un texte donné.

    - **text**: Le texte pour lequel compter les tokens.

    Retourne le nombre de tokens.
    """
    return len(tokenizer.encode(text).tokens)
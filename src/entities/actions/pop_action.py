from .action import Action
from ...utils import Utils
import random

class PopAction(Action):
    def __init__(self, you_or_thou, tone, punctuation='!') -> None:
        requirements = {'you_or_thou': you_or_thou, 'tone': tone}
        Utils.check_requirements(requirements)

        your = 'your' if you_or_thou == 'you' else 'thy'
        yourself = 'yourself' if you_or_thou == 'you' else 'thyself'
        
        positive_phrases = [
            f"Recall {your} beauty, my fine friend",
            f"Recall {your} good fortune",
            f"Recall {your} generosity, {your} highness",
            f"Recall {your} courage, brave knight"
            f"Recall {your} kindness, my good friend"
        ]

        neutral_phrases = [
            f"Recall {yourself}"
        ]

        negative_phrases = [
            f"Recall {your} idiocy, you half-witted hamster",
            f"Recall {your} greed, you filthy pig",
            f"Recall {your} sins and repent to God, you cursed rat",
            f"Recall {yourself} you miserable, fatherless, fat-kidneyed imbocile"
            f"Recall {yourself} you lousy human-being"
            f"Recall {your} theivery you lying, evil cockroach"
            f"Recall {your} cowardice, you fat, foul, fatherless bastard"
            f"Recall {your} adultery, you horrible devil",
            f"Recall {yourself} you stupid, horrid peasant"
        ]

        phrases = {
            'positive': positive_phrases,
            'negative': negative_phrases,
            'neutral': neutral_phrases + positive_phrases  # doing this bc only 1 neutral phrase
        }

        phrase = random.choice(phrases[tone])

        super().__init__(phrase, punctuation)
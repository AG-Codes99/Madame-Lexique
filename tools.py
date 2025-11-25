import json
import random
import difflib
import re

#add word

def load_vocab():
    try:
        with open("vocab_data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def save_vocab(data: dict):
    try:
        with open("vocab_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except:
        pass

def add_word(word: str, meaning: str) -> dict:
    data = load_vocab()
    data[word] = meaning
    save_vocab(data)
    return {"status": "success", "word": word, "meaning": meaning}

def get_meaning(word: str) -> dict:
    data = load_vocab()
    meaning = data.get(word)
    return {"status": "found" if meaning else "not_found", "word": word, "meaning": meaning}

# quiz

def normalize(s):
    return re.sub(r"\s+", " ", s.strip().lower())

def extract_answers(raw):
    if isinstance(raw, list):
        items = raw
    else:
        items = re.split(r"/|,|;|\bor\b", str(raw))

    return [normalize(x) for x in items if x.strip()]

def generate_quiz() -> dict:
    data = load_vocab()
    if not data:
        return {"status": "error", "message": "No vocabulary available."}

    word = random.choice(list(data))
    accepted = extract_answers(data[word])

    return {
        "quiz_word": word,
        "accepted_answers": accepted,
        "action": "model_should_conduct_quiz"
    }

#grammar

def conjugate_verb(verb: str) -> dict:
    return {
        "verb": verb,
        "action": "model_should_conjugate"
    }

def translate_sentence(text: str, target_lang: str = "fr") -> dict:
    return {
        "action": "model_should_translate",
        "text": text,
        "target_language": target_lang
    }

def detect_gender(noun: str) -> dict:
    return {
        "noun": noun,
        "gender": "model_should_decide",
        "confidence": "model"
    }




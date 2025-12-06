from transformers import pipeline
import streamlit as st

@st.cache_resource
def load_model(model_name="nlptown/bert-base-multilingual-uncased-sentiment"):
    return pipeline("sentiment-analysis", model=model_name, tokenizer=model_name)


def normalize_text(text):
    replacements = {
        " ko ": " không ",
        " k ": " không ",
        " dc ": " được ",
        " đc ": " được ",
        " hok ": " không ",
        " hum ": " hôm ",
        " mn ": " mọi người ",
        " vs ": " với ",
        " bt ": " bình thường ",
        " vl ": " rất ",
    }

    text = " " + text.lower() + " "
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text.strip()


def convert_label(label):
    star = int(label.split()[0])
    if star <= 2:
        return "NEGATIVE"
    elif star == 3:
        return "NEUTRAL"
    return "POSITIVE"

import spacy_streamlit


def main(models: str, default_text: str):
    models = [name.strip() for name in models.split(",")]
    spacy_streamlit.visualize(models, default_text, visualizers=["ner"])


if __name__ == "__main__":
    main(
        models="training/model-best",
        default_text="Nimetembelea sehemu kumi za vivutio hapa nchini Tanzania. ",
    )
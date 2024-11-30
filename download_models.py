import spacy

def download_models():
    try:
        spacy.load("en_core_web_sm")
        print("Model 'en_core_web_sm' already exists.")
    except OSError:
        print("Downloading 'en_core_web_sm' model...")
        spacy.cli.download("en_core_web_sm")
        print("Model downloaded successfully.")

if __name__ == "__main__":
    download_models()
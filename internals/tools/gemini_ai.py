import os
import google.generativeai as gemini

def get_gemini_model():
    """
    Get Gemini model

    Returns:
        _type_: _description_
    """

    gemini_key = os.getenv("GEMINI_KEY")

    gemini.configure(api_key=gemini_key)

    model = gemini.GenerativeModel("gemini-pro")
    return model

if __name__ == "__main__":
    gemini_key = os.getenv("GEMINI_KEY")

    gemini.configure(api_key=gemini_key)

    print(list(gemini.list_models()))
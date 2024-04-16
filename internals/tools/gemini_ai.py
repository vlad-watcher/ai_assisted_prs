import os
import google.generativeai as gemini

def get_gemini_model():
    """
    Get Gemini model

    Returns:
        _type_: _description_
    """

    gemini_key = os.getenv("GEMINI_KEY")

    if not gemini_key:
        print("Please set GEMINI_KEY environment variable")
        exit(-1)

    gemini.configure(api_key=gemini_key)
    
    model = gemini.GenerativeModel("gemini-pro")
    return model
"""
Gemini AI Analyzer
"""

from google import genai


# Add your Gemini API key
API_KEY = "AIzaSyAWSuOdhlVaLwNMRG76bXv_t3tRZFb0w1Q"


client = genai.Client(api_key=API_KEY)


def ai_analyze(text):

    try:

        prompt = f"""
        Analyze the following audit document.

        Identify:
        - suspicious activities
        - compliance risks
        - financial concerns

        Also provide:
        - a short professional summary

        Document:
        {text[:4000]}
        """

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as error:

        return f"AI Analysis Error: {error}"
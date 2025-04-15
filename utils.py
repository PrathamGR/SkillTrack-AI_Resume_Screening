import os
import groq

# Set up Groq API key
GROQ_API_KEY = os.getenv("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")

# Initialize Groq client
groq_client = groq.Client(api_key="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")

def groq_generate(prompt: str) -> str:
    """Send the prompt to Groq's API and get a response from Mixtral."""
    try:
        response = groq_client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=4096,
            top_p=0.9
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"
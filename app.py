from flask import Flask, render_template, request
import google.generativeai as genai

# Gemini API key (get from: https://makersuite.google.com/app/apikey)
genai.configure(api_key="AIzaSyB8B_rxhY-V3RV0jDr6LlDNEgMrWIXjBkE")  # ← yahan apna API key daalna

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    niche = request.form['niche']
    length = request.form['length']
    tone = request.form['tone']

    prompt = f"""
    Generate an Instagram reel idea based on:
    - Niche: {niche}
    - Tone: {tone}
    - Length: {length} seconds

    Provide:
    1. Hook (first 3 sec)
    2. Script (bullet points)
    3. Caption
    4. 10 Viral Hashtags
    """

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(prompt)

    return f"<h2>Generated Reel Idea:</h2><pre>{response.text}</pre><br><a href='/'>Back</a>"

if __name__ == '__main__':
    app.run(debug=True)

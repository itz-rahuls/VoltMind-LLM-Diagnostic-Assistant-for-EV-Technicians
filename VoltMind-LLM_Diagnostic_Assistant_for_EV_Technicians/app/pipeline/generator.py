import os
from google import genai
from dotenv import load_dotenv

# 1. Load API Key from .env
load_dotenv()

# 2. Initialize the Gemini Client
# We use v1beta because the Gemini 3 series (Preview) is currently 
# hosted on the beta endpoint.
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options={'api_version': 'v1beta'}
)

def generate_diagnosis(query, docs):
    """
    Takes the user query and retrieved documents to generate 
    a structured EV diagnostic report.
    """
    
    # 3. Create context from retrieved documents
    # Joins the first 300 characters of each relevant document 
    context = "\n\n".join([doc.page_content[:300] for doc in docs])

    # 4. Expert Prompt Construction
    prompt = f"""
You are an expert EV (Electric Vehicle) technician.
Analyze the user problem using the provided context and your internal knowledge.

User Query:
{query}

Retrieved Context:
{context}

Format your response exactly like this:

Affected System:
(Name the specific system like BMS, Inverter, Motor, etc.)

Possible Causes:
- (Cause 1)
- (Cause 2)

Suggested Fix:
- (Action 1)
- (Action 2)

Risk Level:
(Low/Medium/High)

Safety Precautions:
- (Crucial high-voltage safety steps)

Follow-up Questions:
- (What should the user check next?)
"""

    try:
        # 5. Generate Content using Gemini 3 Flash
        # Gemini 3 Flash offers flagship-level reasoning at high speed.
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )
        
        return response.text
        
    except Exception as e:
        return f"Error generating diagnosis: {str(e)}"
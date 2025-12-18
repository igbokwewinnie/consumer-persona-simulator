import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Define 3 consumer personas
PERSONAS = {
    "Tech Emma (24)": {
        "description": "Early adopter, values innovation, willing to pay premium",
        "system_prompt": """You are Emma, a 24-year-old tech enthusiast. You LOVE trying new technology and gadgets. 
        You're willing to pay more for innovative features. You get excited about apps, smart features, and connectivity.
        Keep responses enthusiastic but short (2-3 sentences max). Use casual language."""
    },
    "Budget Brian (35)": {
        "description": "Price-conscious, researches heavily, skeptical of trends",
        "system_prompt": """You are Brian, a 35-year-old who watches every dollar. You're skeptical of expensive products 
        unless they prove real value. You research everything before buying. You prefer practical over flashy.
        Keep responses short (2-3 sentences max). Be direct and pragmatic."""
    },
    "Busy Sarah (42)": {
        "description": "Suburban parent, values convenience, trusts recommendations",
        "system_prompt": """You are Sarah, a 42-year-old busy mom. You value convenience over everything else. 
        You don't have time for complicated setups. You trust recommendations from friends and reviews.
        Keep responses short (2-3 sentences max). Focus on time-saving and ease of use."""
    }
}

# Streamlit UI
st.title("🎭 Consumer Persona Simulator")
st.markdown("Ask a question about a product and see how different consumers respond!")

# Display persona cards
st.subheader("Our Consumer Personas:")
cols = st.columns(3)
for idx, (name, details) in enumerate(PERSONAS.items()):
    with cols[idx]:
        st.info(f"**{name}**\n\n{details['description']}")

# User input
st.markdown("---")
question = st.text_input(
    "Ask about a product:",
    placeholder="e.g., Would you buy a $300 AI-powered coffee maker?",
    help="Try questions like: 'Would you buy...?', 'What do you think of...?', 'Should I get...?'"
)

# Example questions
with st.expander("💡 Example Questions"):
    st.markdown("""
    - Would you buy a $300 AI-powered coffee maker?
    - What do you think of subscription services for groceries?
    - Should I get an electric vehicle or stick with gas?
    - Would you pay $50/month for a meal kit delivery service?
    - Is a smart home security system worth $500?
    """)

# Generate responses button
if st.button("Get Persona Responses", type="primary", disabled=not question):
    st.markdown("---")
    st.subheader("🗣️ How Each Persona Responds:")
    
    # Create columns for responses
    response_cols = st.columns(3)
    
    for idx, (name, details) in enumerate(PERSONAS.items()):
        with response_cols[idx]:
            st.markdown(f"### {name}")
            
            # Show loading spinner
            with st.spinner(f"Asking {name.split()[0]}..."):
                try:
                    # Call Groq API
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {
                                "role": "system",
                                "content": details["system_prompt"]
                            },
                            {
                                "role": "user",
                                "content": question
                            }
                        ],
                        model="llama-3.3-70b-versatile",
                        temperature=0.7,
                        max_tokens=150
                    )
                    
                    response = chat_completion.choices[0].message.content
                    st.success(response)
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
**Built for BluePill AI Application**  
Demonstrates multi-persona AI responses for consumer insights.

**Tech Stack:** Python, Streamlit, Groq LLM  
**Purpose:** Show how different consumer types respond to the same product question
""")
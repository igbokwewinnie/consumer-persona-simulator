# Consumer Persona Simulator

An AI-powered tool that simulates how different consumer personas respond to product questions. Built to demonstrate multi-persona AI systems for consumer insights.

## 🎯 Purpose

This project demonstrates how AI can simulate different consumer types (Tech Enthusiast, Budget-Conscious, Busy Parent) responding to the same product question, helping brands understand diverse consumer perspectives instantly.

**Built for:** BluePill AI application - showcasing understanding of consumer behavior AI and multi-agent systems.

## 🚀 Live Demo

[Add your Streamlit Cloud link here once deployed]

## 💡 Features

- 3 distinct AI consumer personas with different values and preferences
- Side-by-side response comparison
- Real-time AI-powered responses using Groq LLM
- Clean, intuitive Streamlit interface

## 🛠️ Tech Stack

- **Python** - Core programming language
- **Streamlit** - Web interface
- **Groq LLM** - AI responses (Llama 3.3)
- **Pydantic AI** concepts - Persona design

## 📦 Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/consumer-persona-simulator.git
cd consumer-persona-simulator
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Set up environment variables:
```
cp .env.example .env
```
Then edit `.env` and add your Groq API key.

4. Run the app:
```
streamlit run app.py
```

## 🔑 Getting a Groq API Key

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up/login
3. Navigate to "API Keys"
4. Create a new API key
5. Copy it to your `.env` file

## 🎭 The Personas

**Tech Emma (24)** - Early adopter who values innovation and is willing to pay premium for cutting-edge features

**Budget Brian (35)** - Price-conscious researcher who is skeptical of trends and prefers practical solutions

**Busy Sarah (42)** - Suburban parent who values convenience and trusts recommendations

## 📝 Example Questions

- Would you buy a $300 AI-powered coffee maker?
- What do you think of subscription services for groceries?
- Should I get an electric vehicle or stick with gas?
- Is a smart home security system worth $500?

## 🚀 Deployment

Deploy to Streamlit Cloud:
1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Select your repository
5. Add `GROQ_API_KEY` in Secrets
6. Deploy!


## 🙏 Acknowledgments

Built as part of application to BluePill AI to demonstrate understanding of consumer behavior simulation and multi-agent AI systems.
```

---

## **Your Folder Structure Should Look Like:**
```
bluepillproject/
├── app.py
├── requirements.txt
├── .env (NOT PUSHED)
├── .env.example (PUSHED)
├── .gitignore (PUSHED)
└── README.md (PUSHED)

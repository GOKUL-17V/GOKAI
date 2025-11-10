# 🧠 Gok AI – Smart AI Search Assistant

**Gok AI** is a personal AI-powered search app I built using **Streamlit**, **Groq’s Llama 3.1 model**, and **Tavily Search API**.  
It combines AI reasoning and real-time web search to deliver fast, intelligent, and up-to-date answers for any query.

---

## 🚀 Features
- 🤖 **AI-Powered Answers** – Uses Groq Llama 3.1 for natural language understanding.  
- 🔍 **Live Web Search** – Fetches latest info using Tavily’s intelligent search API.  
- ⚡ **Instant Summaries** – Merges reasoning + search results for concise insights.  
- 💬 **Interactive UI** – Simple, clean Streamlit interface for all users.  
- 🔐 **Secure API Setup** – Environment-based key management for safety.


## 🧭 How It Works
1. User enters a query in the Streamlit web app.  
2. The app sends it to an AI agent built with `pydantic-ai`.  
3. The agent uses **Tavily Search** to find real-time web data.  
4. **Groq Llama 3.1** processes and summarizes the results.  
5. Streamlit displays the final intelligent summary instantly.  


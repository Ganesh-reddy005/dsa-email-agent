# DSA-Mindset: The Socratic AI Agent 🤖📚

Most people fail DSA not because they can't code, but because they memorize solutions instead of logic patterns. **DSA-Mindset** is a headless AI agent that sends a personalized, daily "Thinking Brief" to your inbox every morning at 6 AM. [conversation_history:1]

It doesn't give you code. It gives you the **intuition** to solve the problem yourself. [conversation_history:1]

---

##  Features
- **Socratic Thinking Prompts:** Daily DSA problems (from Sean Prashad's patterns) delivered via email with guided logic questions instead of solutions. [conversation_history:1][web:41]
- **Daily LLM Intelligence:** A curated section on the latest in AI—covering Fine-tuning, RAG, and Agentic architectures. [conversation_history:1][web:115]
- **Adaptive Difficulty:** Integrated feedback loops (`Too Easy` / `Just Right` / `Too Hard`) that update your mastery score in MongoDB to adjust future problem selection. [web:23][web:25]
- **Zero-Cost Infrastructure:** Runs entirely on free-tier services (GitHub Actions, MongoDB Atlas, Groq API). [web:88][web:10]

---

##  Tech Stack
- **Language:** Python
- **LLM Engine:** Llama-3.3-70b-versatile via **Groq API** (high-speed inference). [conversation_history:1]
- **Orchestration:** **GitHub Actions** (Cron-scheduled at 00:30 UTC for 06:00 IST). [web:10]
- **Database:** **MongoDB Atlas** (M0 Free Tier) for tracking user state and pattern mastery. [web:87][web:88]
- **Communication:** **SMTP** for automated daily delivery to your inbox. [conversation_history:1]

---

##  Architecture
1. **The Selector:** Queries MongoDB to find the weakest pattern (e.g., "Dynamic Programming") and picks an unsolved problem from the `questions.json` dataset. [web:42]
2. **The Thinking Engine:** Prompts the LLM to generate "Mental Model" questions (e.g., "What condition triggers the window to shrink?") without revealing the solution. [web:14][web:65]
3. **The Curator:** Generates a technical deep-dive on an LLM topic specifically relevant to 2026 AI engineering trends. [web:111]
4. **The Dispatcher:** Formats a clean HTML email with dynamic feedback links and dispatches it via SMTP. [web:46][conversation_history:1]

---

## 🚀 Setup & Installation
1. **Clone the Repo:**
   ```bash
   git clone https://github.com/your-username/dsa-mindset-agent.git

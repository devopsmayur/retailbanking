
Built with ❤️ for privacy-conscious banking applications

🏦 Retail Banking Assistant (IBM Granite + Ollama)
This is a simple Python script that helps you get banking product recommendations and a risk analysis using the IBM Granite model locally via Ollama.

🧰 Requirements
🐍 Python 3.8+

🧠 Ollama installed and running

🧱 IBM Granite model pulled with:

bash
Copy
Edit
ollama pull granite
▶️ How to Run
🚀 Start Ollama:

bash
Copy
Edit
ollama serve
▶️ Run the script:

bash
Copy
Edit
python retail.py
💬 Enter customer details when asked. Example:

yaml
Copy
Edit
Age: 30, Salary: $90,000, Goal: Buy a house
✅ The script will show:

💡 Banking product recommendations

⚠️ Risk analysis of those recommendations

🔍 What It Does
Uses the IBM Granite LLM (locally via Ollama)

Step 1: Suggests products like savings, loans, credit cards

Step 2: Analyzes risks, limitations, and alternatives

🔒 Privacy Note
✅ 100% local processing (no cloud calls)

🛡️ Great for secure, private banking use cases


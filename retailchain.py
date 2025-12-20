# retail_banking_chain.py
import os
from dotenv import load_dotenv
from openai import OpenAI
import anthropic

# Load API keys from .env file
load_dotenv()

# Initialize clients properly
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
anthropic_client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def call_openai_gpt4(prompt: str) -> str:
    """Call OpenAI GPT-4 for banking product recommendations"""
    print("🔁 Calling OpenAI GPT-4...")
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4",
            temperature=0.7,
            messages=[
                {"role": "system", "content": "You are a retail banking advisor."},
                {"role": "user", "content": f"Given this customer info, suggest suitable banking products: {prompt}"}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error calling OpenAI: {e}")
        return "Unable to generate recommendations at this time."

def call_claude(prompt: str) -> str:
    """Call Claude for risk analysis of banking recommendations"""
    print("🔁 Calling Claude (Anthropic)...")
    try:
        response = anthropic_client.messages.create(
            model="claude-3-5-sonnet-20241022",  # Updated to current model
            max_tokens=800,
            temperature=0.7,
            messages=[
                {"role": "user", "content": f"Please review the following banking product suggestions and identify any potential risks, limitations, or customer concerns:\n\n{prompt}"}
            ]
        )
        return response.content[0].text.strip()
    except Exception as e:
        print(f"Error calling Claude: {e}")
        return "Unable to generate risk analysis at this time."

def validate_api_keys():
    """Validate that required API keys are present"""
    openai_key = os.getenv("OPENAI_API_KEY")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not openai_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    if not anthropic_key:
        raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
    
    print("✅ API keys loaded successfully")

def main():
    print("💬 Retail Banking Assistant - Prompt Chain")
    
    try:
        # Validate API keys first
        validate_api_keys()
        
        user_input = input("Enter customer details or query: ")
        
        if not user_input.strip():
            print("Please provide customer information to proceed.")
            return
        
        # Step 1: Call OpenAI for recommendations
        recommendations = call_openai_gpt4(user_input)
        print("\n✅ GPT-4 Product Recommendations:")
        print(recommendations)
        
        # Step 2: Pass to Claude for risk analysis
        risk_analysis = call_claude(recommendations)
        print("\n⚠️ Claude Risk Analys")
        print(risk_analysis)
        
    except Exception as e:
        print(f"Application error: {e}")

if __name__ == "__main__":
    main()

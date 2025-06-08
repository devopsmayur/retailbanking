# retail.py
import requests
import json

class OllamaClient:
    def __init__(self, base_url="http://localhost:11434"):
        self.base_url = base_url
    
    def generate(self, model: str, prompt: str, system_prompt: str = "", temperature: float = 0.7) -> str:
        """Generate response using Ollama API"""
        url = f"{self.base_url}/api/generate"
        
        # Combine system prompt with user prompt if system prompt exists
        if system_prompt:
            full_prompt = f"System: {system_prompt}\n\nUser: {prompt}"
        else:
            full_prompt = prompt
        
        data = {
            "model": model,
            "prompt": full_prompt,
            "stream": False,
            "options": {
                "temperature": temperature
            }
        }
        
        try:
            response = requests.post(url, json=data, timeout=120)
            response.raise_for_status()
            return response.json()["response"]
        except requests.exceptions.RequestException as e:
            print(f"Error calling Ollama: {e}")
            return "Unable to generate response at this time."

def call_ollama_for_recommendations(client: OllamaClient, model: str, prompt: str) -> str:
    """Call Ollama for banking product recommendations"""
    print(f"🔁 Calling Ollama ({model}) for recommendations...")
    
    system_prompt = """You are a retail banking advisor. Your role is to analyze customer information and suggest suitable banking products such as:
    - Savings accounts (regular, high-yield, etc.)
    - Checking accounts
    - Credit cards
    - Personal loans
    - Mortgages
    - Investment products
    - Insurance products
    
    Provide specific, actionable recommendations based on the customer's profile."""
    
    user_prompt = f"Given this customer info, suggest suitable banking products: {prompt}"
    
    return client.generate(model, user_prompt, system_prompt)

def call_ollama_for_risk_analysis(client: OllamaClient, model: str, recommendations: str) -> str:
    """Call Ollama for risk analysis of banking recommendations"""
    print(f"🔁 Calling Ollama ({model}) for risk analysis...")
    
    system_prompt = """You are a banking risk analyst. Review banking product recommendations and identify:
    - Potential risks for the customer
    - Limitations of suggested products
    - Regulatory considerations
    - Customer concerns or objections
    - Alternative options to consider
    
    Be thorough and objective in your analysis."""
    
    user_prompt = f"Please review the following banking product suggestions and identify any potential risks, limitations, or customer concerns:\n\n{recommendations}"
    
    return client.generate(model, user_prompt, system_prompt)

def check_ollama_connection(client: OllamaClient) -> bool:
    """Check if Ollama is running and accessible"""
    try:
        response = requests.get(f"{client.base_url}/api/tags", timeout=5)
        return response.status_code == 200
    except:
        return False

def list_available_models(client: OllamaClient) -> list:
    """List available models in Ollama"""
    try:
        response = requests.get(f"{client.base_url}/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get("models", [])
            return [model["name"] for model in models]
        return []
    except:
        return []

def main():
    print("💬 Retail Banking Assistant - Ollama Local Chain")
    
    # Initialize Ollama client
    client = OllamaClient()
    
    # Check if Ollama is running
    if not check_ollama_connection(client):
        print("❌ Error: Cannot connect to Ollama. Make sure Ollama is running on localhost:11434")
        print("   Start Ollama with: ollama serve")
        return
    
    print("✅ Connected to Ollama successfully")
    
    # List available models
    models = list_available_models(client)
    if not models:
        print("❌ No models found. Please install a model first.")
        print("   Example: ollama pull llama2")
        return
    
    print(f"📋 Available models: {', '.join(models)}")
    
    # Choose models for recommendations and risk analysis
    # You can use the same model for both or different models
    recommendation_model = models[0]  # Use first available model
    risk_analysis_model = models[0]   # Use first available model
    
    # If you have specific models, you can set them here:
    # recommendation_model = "llama2"  # or "mistral", "codellama", etc.
    # risk_analysis_model = "llama2"   # or use a different model
    
    print(f"🤖 Using {recommendation_model} for recommendations")
    print(f"🤖 Using {risk_analysis_model} for risk analysis")
    
    try:
        user_input = input("\nEnter customer details or query: ")
        
        if not user_input.strip():
            print("Please provide customer information to proceed.")
            return
        
        # Step 1: Call Ollama for recommendations
        recommendations = call_ollama_for_recommendations(client, recommendation_model, user_input)
        print(f"\n✅ {recommendation_model} Product Recommendations:")
        print(recommendations)
        
        # Step 2: Call Ollama for risk analysis
        risk_analysis = call_ollama_for_risk_analysis(client, risk_analysis_model, recommendations)
        print(f"\n⚠️ {risk_analysis_model} Risk Analysis:")
        print(risk_analysis)
        
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"Application error: {e}")

if __name__ == "__main__":
    main()

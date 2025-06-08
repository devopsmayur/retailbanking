# Retail Banking Assistant - Ollama Local Chain

A privacy-focused retail banking assistant that runs entirely on your local machine using Ollama. This application provides banking product recommendations and risk analysis without sending any data to external APIs.

## 🌟 Features

- **100% Local Processing**: No API keys or internet connection required
- **Dual-Model Chain**: Uses AI models for both product recommendations and risk analysis
- **Privacy-First**: All customer data stays on your machine
- **Model Flexibility**: Works with any Ollama-compatible model
- **Mac Optimized**: Specially tuned for Mac performance
```

Built with ❤️ for privacy-conscious banking applications

This Python application uses the Ollama local LLM runtime and the IBM Granite model to deliver banking product recommendations and associated risk analysis — securely and privately on your local machine.

✨ Features
🔐 Privacy-first: Runs entirely on your local machine using Ollama.

🤖 AI-Powered Advice: Uses IBM's Granite model for generating:

Retail banking product recommendations

In-depth risk analysis of those recommendations

🧠 Role-specific LLM guidance:

Role: Retail Banking Advisor

Role: Banking Risk Analyst

```

### 3. Set Up Python Environment

```bash
# Create project directory
mkdir ollama-banking
cd ollama-banking

# Create virtual environment
python3 -m venv banking_env
source banking_env/bin/activate

# Install dependencies
pip install requests
```

### 4. Download and Run

1. Save the `retail_banking_chain_ollama.py` file to your project directory
2. Ensure Ollama is running (check menu bar for Ollama icon)
3. Run the application:

```bash
python retail_banking_chain_ollama.py
```

## 📖 Usage

### Basic Usage

```bash
python retail_banking_chain_ollama.py
```

The application will:
1. Connect to your local Ollama instance
2. Display available models
3. Prompt for customer information
4. Generate banking product recommendations
5. Perform risk analysis on the recommendations

### Example Input

```
Enter customer details or query: 28-year-old teacher, $45k salary, wants to save for wedding in 2 years, has $5k in checking account, no debt, good credit score
```

### Example Output

```
✅ phi3:mini Product Recommendations:
Based on your profile, I recommend:
1. High-Yield Savings Account for wedding fund
2. Certificate of Deposit (24-month term)
3. Rewards Credit Card for daily expenses
[... detailed recommendations ...]

⚠️ phi3:mini Risk Analysis:
Potential considerations:
- Interest rate risk on CDs if rates rise
- Credit card spending discipline required
- Emergency fund should be separate from wedding savings
[... detailed risk analysis ...]
```

## 🔧 Configuration

### Model Selection

Edit the main function to specify different models:

```python
# Use different models for different tasks
recommendation_model = "mistral:7b"    # For product recommendations
risk_analysis_model = "llama2:7b"      # For risk analysis
```

### Custom Ollama Server

If running Ollama on a different port:

```python
client = OllamaClient(base_url="http://localhost:YOUR_PORT")
```

## 🖥️ Mac-Specific Recommendations

### Hardware Requirements

| Mac Configuration | Recommended Models | Expected Performance |
|------------------|-------------------|---------------------|
| MacBook Air M1/M2 (8GB) | `phi3:mini` | Fast, efficient |
| MacBook Pro M1/M2 (16GB) | `mistral:7b`, `llama2:7b` | Excellent balance |
| MacBook Pro M3 (32GB+) | `llama2:13b`, `codellama:13b` | Premium quality |

### Performance Tips

- **Close other memory-intensive applications** when running larger models
- **Use Activity Monitor** to check memory usage
- **M-series Macs perform significantly better** than Intel Macs due to unified memory
- **Start with smaller models** and upgrade as needed

## 🛠️ Troubleshooting

### Common Issues

**Ollama Connection Failed**
```bash
# Check if Ollama is running
ps aux | grep ollama

# Restart Ollama
pkill ollama
ollama serve
```

**No Models Available**
```bash
# List installed models
ollama list

# Install a model
ollama pull phi3:mini
```

**Slow Performance**
- Try smaller models (`phi3:mini` instead of `llama2:13b`)
- Close other applications
- Check available RAM in Activity Monitor

**Permission Errors**
```bash
# Make script executable
chmod +x retail_banking_chain_ollama.py
```

### System Requirements Check

```bash
# Check Python version
python3 --version

# Check available disk space (models need storage)
df -h

# Check memory
system_profiler SPHardwareDataType | grep Memory
```

## 🏗️ Project Structure

```
ollama-banking/
├── retail_banking_chain_ollama.py    # Main application
├── banking_env/                      # Python virtual environment
├── README.md                         # This file
└── requirements.txt                  # Python dependencies (optional)
```

## 📋 Requirements

Create a `requirements.txt` file:

```txt
requests>=2.31.0
```

Install with:
```bash
pip install -r requirements.txt
```

## 🔒 Privacy & Security

- **No data leaves your machine**: All processing is local
- **No API keys required**: No external service dependencies
- **Customer data protection**: Sensitive information never transmitted
- **Offline capable**: Works without internet connection

## 🤝 Contributing

This is a local-first application. To extend functionality:

1. **Add new banking products**: Modify system prompts
2. **Integrate new models**: Update model selection logic
3. **Add data persistence**: Extend with local file storage
4. **Create web interface**: Add Flask/FastAPI frontend

## 📜 License

[Add your preferred license here]

## 🆘 Support

### Getting Help

1. **Check Ollama Documentation**: [https://ollama.com/docs](https://ollama.com/docs)
2. **Model Performance Issues**: Try different models from the recommended list
3. **Mac-Specific Issues**: Check Activity Monitor for resource usage

### Useful Commands

```bash
# Check Ollama status
curl http://localhost:11434/api/tags

# Monitor model usage
ollama ps

# Update Ollama
brew upgrade ollama  # If installed via Homebrew

# List all available models online
ollama search banking  # Search for banking-specific models
```

---

**Built with ❤️ for privacy-conscious banking applications**

# Retail Banking Chain Application

A Python application that uses AI prompt chaining to provide comprehensive banking product recommendations and risk analysis. The application leverages both OpenAI's GPT-4 and Anthropic's Claude to deliver balanced, well-analyzed banking advice.

## Overview

This application implements a two-step AI prompt chain:
1. **GPT-4** analyzes customer information and suggests suitable banking products
2. **Claude** reviews the recommendations and provides risk analysis and potential concerns

## Features

- 🏦 **Banking Product Recommendations**: AI-powered suggestions based on customer profiles
- ⚠️ **Risk Analysis**: Comprehensive evaluation of recommended products
- 🔄 **Prompt Chaining**: Sequential AI model calls for enhanced analysis
- 🛡️ **Error Handling**: Robust error management for API failures
- ✅ **Input Validation**: Ensures proper data before processing

## Prerequisites

- Python 3.7+
- OpenAI API key
- Anthropic API key

## Installation

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd retail-banking-chain
   ```

2. **Install required dependencies**
   ```bash
   pip install openai anthropic python-dotenv
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```

## API Key Setup

### OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key to your `.env` file

### Anthropic API Key
1. Visit [Anthropic Console](https://console.anthropic.com/)
2. Sign up or log in to your account
3. Go to API Keys section
4. Generate a new API key
5. Copy the key to your `.env` file

## Usage

1. **Run the application**
   ```bash
   python retail_banking_chain.py
   ```

2. **Enter customer information** when prompted. Examples:
   - "25-year-old software engineer, salary $75,000, looking to buy first home"
   - "Retired couple, age 65, $500,000 in savings, conservative investment approach"
   - "Small business owner, revenue $200,000/year, needs business banking solutions"

3. **Review the output**:
   - GPT-4 will provide tailored banking product recommendations
   - Claude will analyze potential risks and concerns

## Example Output

```
💬 Retail Banking Assistant - Prompt Chain
✅ API keys loaded successfully
Enter customer details or query: 30-year-old teacher, salary $45,000, wants to start investing

🔁 Calling OpenAI GPT-4...

✅ GPT-4 Product Recommendations:
Based on your profile as a 30-year-old teacher with a $45,000 salary, here are suitable banking products:
[Detailed recommendations...]

🔁 Calling Claude (Anthropic)...

⚠️ Claude Risk Analysis:
Review of the banking recommendations reveals several considerations:
[Risk analysis and concerns...]
```

## Project Structure

```
retail-banking-chain/
├── retail_banking_chain.py    # Main application file
├── .env                       # Environment variables (create this)
├── README.md                  # This file
└── requirements.txt           # Python dependencies (optional)
```

## Configuration

### Model Settings
- **OpenAI Model**: `gpt-4`
- **Claude Model**: `claude-3-5-sonnet-20241022`
- **Temperature**: `0.7` (balanced creativity/consistency)
- **Max Tokens**: `800` for Claude responses

### Customization
You can modify the system prompts in the code to adjust the AI behavior:
- Banking advisor persona (OpenAI)
- Risk analysis focus (Claude)

## Error Handling

The application handles common scenarios:
- Missing or invalid API keys
- Network connectivity issues
- API rate limits or service unavailability
- Empty user inputs
- Malformed API responses

## Security Considerations

- ⚠️ **Never commit `.env` files** to version control
- 🔒 **Store API keys securely** and rotate them regularly
- 🛡️ **Validate user inputs** in production environments
- 📊 **Monitor API usage** to prevent unexpected charges

## Limitations

- Requires active internet connection
- Subject to API rate limits and costs
- AI responses are for informational purposes only
- Not a substitute for professional financial advice

## Troubleshooting

### Common Issues

1. **"API key not found" error**
   - Ensure `.env` file exists in project root
   - Verify API key names match exactly: `OPENAI_API_KEY` and `ANTHROPIC_API_KEY`

2. **"Unable to generate recommendations" error**
   - Check internet connection
   - Verify API keys are valid and have sufficient credits
   - Check API service status pages

3. **Import errors**
   - Ensure all dependencies are installed: `pip install openai anthropic python-dotenv`
   - Use the correct Python environment

### Getting Help

- Check the [OpenAI API Documentation](https://platform.openai.com/docs)
- Review [Anthropic API Documentation](https://docs.anthropic.com/)
- Verify your API key permissions and billing status

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is provided as-is for educational and demonstration purposes. Please ensure compliance with OpenAI and Anthropic terms of service when using their APIs.

## Disclaimer

This application provides AI-generated banking recommendations for informational purposes only. Always consult with qualified financial professionals before making banking or investment decisions.

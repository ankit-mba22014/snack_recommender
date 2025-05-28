# 🥤 PepsiCo Snack Mood Recommender

An AI-powered web application that recommends PepsiCo snacks based on your current mood. Built with Streamlit and HuggingFace Transformers for intelligent mood detection and personalized snack suggestions.

## 🌟 Features

- **Dual Input Methods**: Choose your mood manually or describe it in natural language
- **AI-Powered Mood Detection**: Uses HuggingFace transformers for sentiment analysis
- **Personalized Recommendations**: Get 1-5 tailored PepsiCo snack suggestions
- **Comprehensive Product Database**: Includes popular PepsiCo brands like Lay's, Doritos, Cheetos, Pepsi, Mountain Dew, and more
- **Beautiful UI**: Color-coded mood indicators with responsive design
- **Real-time Analysis**: Instant mood detection with confidence scores

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd pepsico-snack-recommender
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run streamlit_app.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

## 📱 How to Use

### Method 1: Manual Mood Selection
1. Select "Select from options" radio button
2. Choose your current mood from the dropdown:
   - 😊 Happy
   - 😢 Sad
   - 😰 Stressed
   - ⚡ Energetic
   - 😌 Relaxed
3. Adjust the number of recommendations (1-5)
4. View your personalized snack suggestions

### Method 2: AI Mood Detection
1. Select "Describe in your own words" radio button
2. Type how you're feeling in the text area
   - Example: "I'm having a great day and feeling amazing!"
   - Example: "I'm stressed about work and need comfort food"
3. The AI will analyze your text and detect your mood
4. Get recommendations based on the detected sentiment

## 🧠 AI Model

The application uses the `cardiffnlp/twitter-roberta-base-sentiment-latest` model from HuggingFace for sentiment analysis. This model:

- Trained on Twitter data for real-world language understanding
- Provides high accuracy for sentiment classification
- Returns confidence scores for transparent AI decisions
- Maps sentiments to appropriate mood categories

## 🍿 Snack Categories

The recommender includes authentic PepsiCo products across multiple categories:

- **Chips**: Lay's, Ruffles, Baked Lay's
- **Tortilla Chips**: Doritos, Tostitos
- **Cheese Snacks**: Cheetos varieties
- **Beverages**: Pepsi, Mountain Dew, Tropicana
- **Healthy Options**: Quaker products, SunChips
- **Specialty Items**: Smartfood Popcorn, Fritos

## 🎯 Mood-Snack Mapping

Each mood is carefully mapped to appropriate snack types:

- **Happy** 😊: Celebratory snacks with bold flavors
- **Sad** 😢: Comfort foods and mood-boosting options
- **Stressed** 😰: Light, healthy alternatives for mindful eating
- **Energetic** ⚡: Spicy, high-energy snacks and drinks
- **Relaxed** 😌: Mellow, easy-going snack options

## 🛠️ Technical Stack

- **Frontend**: Streamlit for interactive web interface
- **AI/ML**: HuggingFace Transformers for sentiment analysis
- **Backend**: Python with pandas for data management
- **Styling**: Custom CSS with mood-themed colors
- **Deployment**: Ready for Streamlit Cloud, Heroku, or local hosting

## 📁 Project Structure

```
pepsico-snack-recommender/
├── streamlit_app.py      # Main application file
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
└── .gitignore          # Git ignore file (optional)
```

## 🔧 Configuration

### Adding New Snacks
To add new PepsiCo products, edit the `PEPSICO_SNACKS` dictionary in `streamlit_app.py`:

```python
"mood_name": {
    "snacks": [
        {
            "name": "Product Name",
            "description": "Product description",
            "category": "Product Category"
        }
    ],
    "emoji": "😊",
    "color": "#HEX_COLOR"
}
```

### Customizing Moods
You can add new moods by:
1. Adding entries to the `PEPSICO_SNACKS` dictionary
2. Updating the mood mapping in `analyze_mood_from_text()` function
3. Adding corresponding UI options

## 🚀 Deployment

### Streamlit Cloud
1. Push your code to GitHub
2. Connect your repository to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy with one click

### Local Development
```bash
# Install in development mode
pip install -e .

# Run with auto-reload
streamlit run streamlit_app.py --server.runOnSave true
```

### Docker (Optional)
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- HuggingFace for providing excellent transformer models
- Streamlit for the amazing web framework
- PepsiCo for the delicious snack inspiration

## 📞 Support

If you encounter any issues or have questions:

1. Check the existing issues on GitHub
2. Create a new issue with detailed description
3. Include error messages and system information

## 🔮 Future Enhancements

- [ ] User preference learning
- [ ] Nutritional information display
- [ ] Integration with food delivery services
- [ ] Multi-language support
- [ ] Voice input for mood detection
- [ ] Social sharing features
- [ ] Recommendation history tracking

---

**Built with ❤️ using Streamlit and HuggingFace Transformers**

import streamlit as st
import pandas as pd
import numpy as np
from transformers import pipeline
import random

# Initialize the sentiment analysis pipeline
@st.cache_resource
def load_sentiment_model():
    return pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")

# PepsiCo snacks database with mood mappings
PEPSICO_SNACKS = {
    "happy": {
        "snacks": [
            {"name": "Lay's Classic", "description": "Crispy golden potato chips perfect for celebration", "category": "Chips"},
            {"name": "Cheetos Crunchy", "description": "Fun orange cheese puffs that make you smile", "category": "Cheese Snacks"},
            {"name": "Doritos Nacho Cheese", "description": "Bold nacho flavor for good times", "category": "Tortilla Chips"},
            {"name": "Pepsi Cola", "description": "Refreshing cola to complement your good mood", "category": "Beverages"},
            {"name": "Mountain Dew", "description": "Energizing citrus soda for active moments", "category": "Beverages"}
        ],
        "emoji": "😊",
        "color": "#FFD700"
    },
    "sad": {
        "snacks": [
            {"name": "Quaker Oats Cookies", "description": "Comforting oatmeal cookies for emotional support", "category": "Cookies"},
            {"name": "Lay's Kettle Cooked", "description": "Hearty, satisfying chips with extra crunch", "category": "Chips"},
            {"name": "Tropicana Orange Juice", "description": "Vitamin C boost to brighten your day", "category": "Beverages"},
            {"name": "Ruffles Original", "description": "Thick ridged chips perfect for comfort eating", "category": "Chips"},
            {"name": "Cheetos Puffs", "description": "Soft, melt-in-mouth comfort snack", "category": "Cheese Snacks"}
        ],
        "emoji": "😢",
        "color": "#87CEEB"
    },
    "stressed": {
        "snacks": [
            {"name": "Quaker Rice Cakes", "description": "Light, healthy option to ease tension", "category": "Rice Snacks"},
            {"name": "Baked Lay's", "description": "Lighter chips for mindful snacking", "category": "Chips"},
            {"name": "Pepsi Zero Sugar", "description": "Refreshing without the sugar crash", "category": "Beverages"},
            {"name": "SunChips Original", "description": "Whole grain goodness for sustained energy", "category": "Multigrain Chips"},
            {"name": "Aquafina Water", "description": "Pure hydration to help you reset", "category": "Water"}
        ],
        "emoji": "😰",
        "color": "#FFA07A"
    },
    "energetic": {
        "snacks": [
            {"name": "Doritos Flamin' Hot", "description": "Spicy kick to match your energy", "category": "Tortilla Chips"},
            {"name": "Mountain Dew Code Red", "description": "Cherry blast for high energy moments", "category": "Beverages"},
            {"name": "Cheetos Flamin' Hot", "description": "Fiery cheese snacks for bold moods", "category": "Cheese Snacks"},
            {"name": "Fritos Original", "description": "Corn chips with serious crunch power", "category": "Corn Chips"},
            {"name": "Pepsi Max", "description": "Maximum taste, maximum energy", "category": "Beverages"}
        ],
        "emoji": "⚡",
        "color": "#FF6347"
    },
    "relaxed": {
        "snacks": [
            {"name": "Tostitos Scoops", "description": "Perfect for leisurely dipping", "category": "Tortilla Chips"},
            {"name": "Lay's Wavy", "description": "Smooth waves for a chill vibe", "category": "Chips"},
            {"name": "Sierra Mist", "description": "Light, crisp lemon-lime refreshment", "category": "Beverages"},
            {"name": "SunChips Harvest Cheddar", "description": "Mellow cheese flavor for easy snacking", "category": "Multigrain Chips"},
            {"name": "Smartfood Popcorn", "description": "Light, airy snack for peaceful moments", "category": "Popcorn"}
        ],
        "emoji": "😌",
        "color": "#98FB98"
    }
}

def analyze_mood_from_text(text, sentiment_pipeline):
    """Analyze mood from user input text using HuggingFace model"""
    try:
        result = sentiment_pipeline(text)[0]
        label = result['label'].lower()
        confidence = result['score']
        
        # Map sentiment labels to moods
        mood_mapping = {
            'positive': 'happy',
            'negative': 'sad',
            'neutral': 'relaxed'
        }
        
        return mood_mapping.get(label, 'relaxed'), confidence
    except:
        return 'relaxed', 0.5

def get_recommendations(mood, num_recommendations=3):
    """Get snack recommendations based on mood"""
    if mood in PEPSICO_SNACKS:
        snacks = PEPSICO_SNACKS[mood]["snacks"]
        return random.sample(snacks, min(num_recommendations, len(snacks)))
    return []

def main():
    st.set_page_config(
        page_title="PepsiCo Snack Mood Recommender",
        page_icon="🥤",
        layout="wide"
    )
    
    # Load the sentiment model
    sentiment_pipeline = load_sentiment_model()
    
    # Header
    st.title("🥤 PepsiCo Snack Mood Recommender")
    st.markdown("*Discover the perfect PepsiCo snack based on how you're feeling!*")
    
    # Create two columns
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("How are you feeling?")
        
        # Method selection
        method = st.radio(
            "Choose how to tell us your mood:",
            ["Select from options", "Describe in your own words"]
        )
        
        if method == "Select from options":
            mood_options = {
                "😊 Happy": "happy",
                "😢 Sad": "sad", 
                "😰 Stressed": "stressed",
                "⚡ Energetic": "energetic",
                "😌 Relaxed": "relaxed"
            }
            
            selected_option = st.selectbox("Select your current mood:", list(mood_options.keys()))
            selected_mood = mood_options[selected_option]
            confidence = 1.0
            
        else:
            mood_text = st.text_area(
                "Describe how you're feeling:",
                placeholder="e.g., I'm having a great day and feeling amazing! or I'm stressed about work..."
            )
            
            if mood_text:
                selected_mood, confidence = analyze_mood_from_text(mood_text, sentiment_pipeline)
                st.info(f"Detected mood: **{selected_mood.title()}** (Confidence: {confidence:.2f})")
            else:
                selected_mood = "relaxed"
                confidence = 0.5
        
        # Number of recommendations
        num_recs = st.slider("Number of recommendations:", 1, 5, 3)
    
    with col2:
        st.header("Your Snack Recommendations")
        
        if selected_mood in PEPSICO_SNACKS:
            mood_data = PEPSICO_SNACKS[selected_mood]
            
            # Display mood indicator
            st.markdown(f"""
            <div style="text-align: center; padding: 20px; background-color: {mood_data['color']}; 
                        border-radius: 10px; margin-bottom: 20px;">
                <h2 style="color: white; margin: 0;">{mood_data['emoji']} {selected_mood.title()} Mood</h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Get recommendations
            recommendations = get_recommendations(selected_mood, num_recs)
            
            for i, snack in enumerate(recommendations, 1):
                with st.container():
                    st.markdown(f"""
                    <div style="border: 2px solid {mood_data['color']}; border-radius: 10px; 
                                padding: 15px; margin: 10px 0; background-color: #f9f9f9;">
                        <h4 style="color: #333; margin-top: 0;">{i}. {snack['name']}</h4>
                        <p style="color: #666; margin: 5px 0;"><strong>Category:</strong> {snack['category']}</p>
                        <p style="color: #555; margin-bottom: 0;">{snack['description']}</p>
                    </div>
                    """, unsafe_allow_html=True)
    
    # Additional features
    st.markdown("---")
    
    # Mood statistics
    col3, col4 = st.columns([1, 1])
    
    with col3:
        st.subheader("All Available Moods")
        for mood, data in PEPSICO_SNACKS.items():
            st.markdown(f"**{data['emoji']} {mood.title()}** - {len(data['snacks'])} snack options")
    
    with col4:
        st.subheader("About This Recommender")
        st.markdown("""
        This recommender uses advanced AI to analyze your mood and suggest the perfect PepsiCo snacks:
        
        - **AI-Powered**: Uses HuggingFace transformers for mood detection
        - **Personalized**: Tailored recommendations based on your feelings
        - **Diverse Options**: Covers chips, beverages, and healthy alternatives
        - **PepsiCo Products**: Only authentic PepsiCo brand snacks
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("*Built with ❤️ using Streamlit and HuggingFace Transformers*")

if __name__ == "__main__":
    main()

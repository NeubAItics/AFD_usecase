import streamlit as st
import base64
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env only if running locally
if not os.getenv("STREAMLIT_ENV"):  # STREAMLIT_ENV can be set to "production" in deployed environments
    load_dotenv()

# Access the API key from Streamlit secrets or environment
api_key = st.secrets.get("general", {}).get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

# Validate the API key
if not api_key:
    st.error("API key not found. Please check your Streamlit secrets or the `.env` file.")
    st.stop()

# Set custom background color for AI-themed appearance
page_bg = """
<style>
body {
    background-color: #060648FF;
    color: #0173CBFF;
}
h1, h3, h2 {
    color: #F4C807FF;
}
footer {
    color: #000E8CFF;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Ensure the correct path to the logo
logo_path = "logo/big-logo-3.jpg"  # Update to relative path if needed

# Display the logo if the file exists
if os.path.exists(logo_path):
    with open(logo_path, "rb") as file:
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                <img src="data:image/jpeg;base64,{base64.b64encode(file.read()).decode()}" alt="Company Logo" style="width: 200px;">
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.error("Logo file not found. Please ensure the correct path.")

# App title with styling
st.markdown("<h1>📊 Visual Finance Assistant</h1>", unsafe_allow_html=True)
st.markdown("Upload a balance sheet image and choose an analysis to get meaningful insights.")

# File uploader widget
uploaded_file = st.file_uploader("📁 Upload Image", type=['jpg', 'png', 'jpeg'])

# Display the uploaded image if the user uploads one
if uploaded_file:
    st.markdown("### 📄 Uploaded Image:")
    st.image(uploaded_file, caption="Uploaded Balance Sheet Image", use_container_width=True)

# Analysis options with brief descriptions
analysis_options = {
    "Debt to Asset Ratio": "Measures the percentage of assets financed by debt.",
    "Current Ratio": "Compares current assets to current liabilities to assess liquidity.",
    "Debt to Equity Ratio": "Measures financial leverage by comparing total liabilities to shareholders' equity.",
    "Net Profit Margin": "Indicates how much profit a company makes from its total revenue.",
    "Return on Assets (ROA)": "Measures a company's profitability by comparing net income to total assets.",
    "Return on Equity (ROE)": "Shows how much profit is generated from shareholders' equity.",
    "Working Capital Ratio": "Measures a company's operational efficiency by comparing current assets to current liabilities.",
    "Quick Ratio": "A liquidity ratio that excludes inventory to assess short-term financial health.",
    "Inventory Turnover Ratio": "Measures how efficiently inventory is being sold and replaced.",
    "Accounts Receivable Turnover": "Shows how efficiently a company collects revenue from its customers."
}

# Display options in a selectbox with descriptions
st.markdown("<h3>🔍 Select an Analysis</h3>", unsafe_allow_html=True)
selected_analysis = st.selectbox(
    "Choose an analysis option:",
    options=list(analysis_options.keys()),
    format_func=lambda x: f"{x} - {analysis_options[x]}"
)

# Input for year selection by user
st.markdown("<h3>📅 Select the Year for Analysis</h3>", unsafe_allow_html=True)
selected_year = st.number_input("Enter the year to analyze:", min_value=2000, max_value=2024, value=2023, step=1)

# Analyze on button press
if st.button("🚀 Analyze"):
    if not uploaded_file:
        st.error("Please upload an image before analyzing.")
    else:
        st.markdown("<h3 style='color: #673AB7;'>Processing...</h3>", unsafe_allow_html=True)
        progress_bar = st.progress(0)

        for i in range(1, 101):
            progress_bar.progress(i)

        # Create OpenAI request safely
        try:
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model='gpt-4-turbo',
                messages=[
                    {
                        "role": "user",
                        "content": f"You are a smart financial analyst who can determine calculations. "
                                   f"Using only the image provided, what is the {selected_analysis.lower()} in {int(selected_year)}? "
                                   "Explain if this is a good result or not to someone who knows little about finance."
                    }
                ],
                max_tokens=400
            )
            progress_bar.progress(100)
            st.success("Analysis Complete!")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error in analysis: {str(e)}")

import streamlit as st
import base64
from dotenv import load_dotenv
import os
from fpdf import FPDF  # For creating PDF
import unicodedata
import openai  # Ensure `openai` is correctly imported

# Load environment variables
load_dotenv()

# Get API key from environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("API key not found. Ensure you have a valid `.env` file with `OPENAI_API_KEY` set.")
    st.stop()

# Set OpenAI API key
openai.api_key = api_key

# Function to encode the image to base64
def encode_image(image_file):
    if image_file is None:
        raise ValueError("No image uploaded or the file is invalid")
    return base64.b64encode(image_file.read()).decode('utf-8')

# Function to clean text for PDF compatibility
def clean_text_for_pdf(text):
    """
    Removes or replaces characters not supported by the Latin-1 encoding
    used by FPDF.
    """
    return unicodedata.normalize('NFKD', text).encode('latin-1', 'replace').decode('latin-1')

# Function to create a PDF for downloading
def create_pdf(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Analyzed Results", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=10)
    content = clean_text_for_pdf(content)
    pdf.multi_cell(0, 10, content)
    return pdf

# Set custom background and styling
page_bg = """
<style>
body { background-color: #060648FF; color: #0173CBFF; }
h1, h3, h2 { color: #F4C807FF; }
footer { color: #000E8CFF; }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Logo path
logo_path = "big-logo-3.jpg"
if os.path.exists(logo_path):
    with open(logo_path, "rb") as file:
        st.markdown(
            f"""<div style="display: flex; justify-content: center; margin-bottom: 20px;">
            <img src="data:image/jpeg;base64,{base64.b64encode(file.read()).decode()}" alt="Company Logo" style="width: 200px;">
            </div>""",
            unsafe_allow_html=True
        )

# App title
st.markdown("<h1>📊 Visual Finance Assistant</h1>", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("📁 Upload Image", type=['jpg', 'png', 'jpeg'])

# Analysis options
analysis_options = {
    "Debt to Asset Ratio": "Measures the percentage of assets financed by debt.",
    "Current Ratio": "Compares current assets to current liabilities to assess liquidity.",
    # Add more options as needed
}
selected_analysis = st.selectbox("Choose an analysis:", list(analysis_options.keys()))

# Analyze button
if st.button("🚀 Analyze"):
    if not uploaded_file:
        st.error("Please upload an image before analyzing.")
        st.stop()

    st.markdown("<h3 style='color: #673AB7;'>Processing...</h3>", unsafe_allow_html=True)
    progress_bar = st.progress(0)

    try:
        # Simulate progress
        for i in range(1, 101):
            progress_bar.progress(i)
        
        # Create API request
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "user", "content": f"Analyze this image for {selected_analysis.lower()}."}
            ],
            max_tokens=800
        )
        
        # Extract results
        result_content = response['choices'][0]['message']['content']

        # Display results
        st.success("Analysis Complete!")
        st.markdown("<h3>📝 Results:</h3>", unsafe_allow_html=True)
        st.write(result_content)

        # Create downloadable PDF
        pdf = create_pdf(result_content)
        pdf_output = "analyzed_results.pdf"
        pdf.output(pdf_output)
        with open(pdf_output, "rb") as pdf_file:
            st.download_button("📥 Download Results as PDF", data=pdf_file, file_name="Analyzed_Results.pdf")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
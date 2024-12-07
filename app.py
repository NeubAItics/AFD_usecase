import streamlit as st
import base64
from openai import OpenAI
import os
from fpdf import FPDF  # For creating PDF
import unicodedata

# Set OpenAI API key (you should add your actual API key here)
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY", "")

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
    # Normalize Unicode characters to ASCII equivalents where possible
    return unicodedata.normalize('NFKD', text).encode('latin-1', 'replace').decode('latin-1')

# Function to create a PDF for downloading
def create_pdf(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Analyzed Results", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=10)
    
    # Clean content for PDF compatibility
    content = clean_text_for_pdf(content)
    pdf.multi_cell(0, 10, content)
    return pdf

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
logo_path = "big-logo-3.jpg"  # Update to the actual path if needed

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
    st.error("Logo file not found. Please check the file path.")

# App title with styling
st.markdown("<h1>📊 Visual Finance Assistant</h1>", unsafe_allow_html=True)
st.markdown("Upload a balance sheet image and choose an analysis to get meaningful insights.")

# File uploader widget
uploaded_file = st.file_uploader("📁 Upload Image", type=['jpg', 'png', 'jpeg'])

# Analysis options with brief descriptions
analysis_options = {
    "Debt to Asset Ratio": "Measures the percentage of assets financed by debt.",
    "Current Ratio": "Compares current assets to current liabilities to assess liquidity.",
    "Quick Ratio": "Examines short-term liquidity excluding inventory.",
    "Net Profit Margin": "Analyzes how much profit is generated per dollar of revenue.",
    "Return on Assets (ROA)": "Shows how efficiently assets are used to generate profit.",
    "Equity Ratio": "Indicates the proportion of assets financed by equity.",
    "Inventory Turnover": "Measures how often inventory is sold and replaced.",
    "Working Capital": "Calculates current assets minus current liabilities.",
    "Operating Cash Flow Ratio": "Shows the ability to cover liabilities with operating cash flow.",
    "Gross Profit Margin": "Measures the profitability of products sold."
}

# Display options in a selectbox with descriptions
st.markdown("<h3>🔍 Select an Analysis</h3>", unsafe_allow_html=True)
selected_analysis = st.selectbox(
    "Choose an analysis option:",
    options=list(analysis_options.keys()),
    format_func=lambda x: f"{x} - {analysis_options[x]}"
)

# Display uploaded image and details
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    st.markdown("<p style='color: #DE084FFF;'>Image successfully uploaded!</p>", unsafe_allow_html=True)

# Button to trigger analysis
if st.button("🚀 Analyze"):
    st.markdown("<h3 style='color: #673AB7;'>Processing...</h3>", unsafe_allow_html=True)
    progress_bar = st.progress(0)  # Initialize a progress bar
    
    # Simulate progress
    for i in range(1, 101):
        progress_bar.progress(i)
    
    # Initialize OpenAI client
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Create OpenAI request
    try:
        response = client.chat.completions.create(
            model='gpt-4-turbo',
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text",
                     "text": f"You are a smart financial analyst who can determine calculations. "
                             f"Using only the image provided, what is the {selected_analysis.lower()}? "
                             "Explain it in simple terms for someone new to finance."
                    },
                    {"type": "image_url",
                     "image_url": {"url": f"data:image/jpeg;base64,{encode_image(uploaded_file)}"}
                    }
                ]
            }],
            max_tokens=800  # Limit the response length
        )
    except Exception as e:
        st.error(f"Error in analyzing the image: {str(e)}")
        st.stop()
    
    # Extract results
    result_content = response.choices[0].message.content

    # Display results
    progress_bar.progress(100)
    st.success("Analysis Complete!")
    st.markdown("<h3>📝 Results:</h3>", unsafe_allow_html=True)
    st.write(result_content)

    # Add download button for PDF
    pdf = create_pdf(result_content)
    pdf_output = "analyzed_results.pdf"
    pdf.output(pdf_output)
    with open(pdf_output, "rb") as pdf_file:
        st.download_button(
            label="📥 Download Results as PDF",
            data=pdf_file,
            file_name="Analyzed_Results.pdf",
            mime="application/pdf"
        )

# Footer
st.markdown(
    "<footer style='text-align: center; margin-top: 50px;'>"
    "Developed with ❤️ by NeubAItics</footer>", 
    unsafe_allow_html=True
)

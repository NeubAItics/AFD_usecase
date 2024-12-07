# '''
# import streamlit as st
# import base64
# from openai import OpenAI
# import os
# from dotenv import load_dotenv
# load_dotenv()

# # Set OpenAI API key (you should add your actual API key here)
# os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY", "")
# # Function to encode the image to base64
# def encode_image(image_file):
#     return base64.b64encode(image_file.read()).decode('utf-8')
# # Streamlit app title
# st.title("Balance Sheet Calculator")
# # File uploader widget
# uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
# # Calculation options for the dropdown
# calculation_options = [
#     "Debt to Asset Ratio",
#     "Current Ratio",
#     "Quick Ratio"
# ]
# # Selectbox for choosing the calculation
# selected_calculation = st.selectbox("Select Calculation", calculation_options)
# # Display uploaded image
# if uploaded_file is not None:
#     st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
#     # Initialize OpenAI client
#     client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Using environment variable for security
#     # Button to trigger calculation
#     # Button to trigger calculation
# if st.button("Calculate"):
#     progress_bar = st.progress(0)  # Show a progress bar (optional, improves UX)
#     # Create the request to OpenAI
#     response = client.chat.completions.create(
#         model='gpt-4-turbo',
#         messages=[
#             {
#                 "role": "user",
#                 "content": [
#                     {"type": "text",
#                      "text": f"You are a smart financial analyst who can determine calculations."
#                              f"Using only the image provided, what is the {selected_calculation.lower()} in 2018? "
#                              "Explain if this is a good result or not to someone who knows little about finance. "
#                              "I work at fintech but I'm not an expert in financial documents."
#                     },
#                     {"type": "image_url",
#                      "image_url": {"url": f"data:image/jpeg;base64,{encode_image(uploaded_file)}"}
#                     }
#                 ]
#             }
#         ],
#         max_tokens=800  # Limit the response length
#     )
#     progress_bar.progress(100)  # Move this line inside the button's logic
#     st.write("response:")
#     st.write(response.choices[0].message.content)
# '''

# import streamlit as st
# import base64
# from openai import OpenAI
# import os
# from dotenv import load_dotenv

# # Load environment variables from the .env file
# load_dotenv()

# # Retrieve OpenAI API key from the environment variable
# api_key = os.getenv("OPENAI_API_KEY")
# if not api_key:
#     st.error("OpenAI API key not found. Please check your .env file.")

# # Function to encode the image to base64
# def encode_image(image_file):
#     return base64.b64encode(image_file.read()).decode('utf-8')

# # Streamlit app title
# st.title("Balance Sheet Calculator")

# # File uploader widget
# uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])

# # Calculation options for the dropdown
# calculation_options = [
#     "Debt to Asset Ratio",
#     "Current Ratio",
#     "Quick Ratio"
# ]

# # Selectbox for choosing the calculation
# selected_calculation = st.selectbox("Select Calculation", calculation_options)

# # Display uploaded image
# if uploaded_file is not None:
#     st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

# # Button to trigger calculation
# if st.button("Calculate"):
#     if not uploaded_file:
#         st.error("Please upload an image before calculating.")
#     else:
#         try:
#             # Show a progress bar
#             progress_bar = st.progress(0)

#             # Encode the uploaded image
#             image_data = encode_image(uploaded_file)

#             # Construct the OpenAI prompt
#             prompt = f"""
#             You are a financial analyst. Using the uploaded financial document image, 
#             calculate the {selected_calculation.lower()} for 2018. Provide a clear explanation 
#             of the result, suitable for someone with minimal financial knowledge.

#             Financial Document Image (Base64-Encoded):
#             data:image/jpeg;base64,{image_data}
#             """

#             # Initialize OpenAI client
#             client = OpenAI(api_key=api_key)

#             # OpenAI API Request
#             response = client.chat.completions.create(
#                 model='gpt-4-turbo',
#                 messages=[
#                     {"role": "user", "content": prompt}
#                 ],
#                 max_tokens=800  # Limit the response length
#             )

#             # Update the progress bar
#             progress_bar.progress(100)

#             # Extract and display the content from the response
#             st.subheader("Analysis Results:")
#             response_content = response.choices[0].message.content
#             st.write(response_content)

#         except Exception as e:
#             st.error(f"An error occurred: {e}")

# import streamlit as st
# import base64
# from openai import OpenAI
# import os
# # Set OpenAI API key (you should add your actual API key here)
# os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY", "")
# # Function to encode the image to base64
# def encode_image(image_file):
#     return base64.b64encode(image_file.read()).decode('utf-8')
# # Streamlit app title
# st.title("Balance Sheet Calculator")
# # File uploader widget
# uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
# # Calculation options for the dropdown
# calculation_options = [
#     "Debt to Asset Ratio",
#     "Current Ratio",
#     "Quick Ratio"
# ]
# # Selectbox for choosing the calculation
# selected_calculation = st.selectbox("Select Calculation", calculation_options)
# # Display uploaded image
# if uploaded_file is not None:
#     st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
#     # Initialize OpenAI client
#     client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Using environment variable for security
#     # Button to trigger calculation
#     # Button to trigger calculation
# if st.button("Calculate"):
#     progress_bar = st.progress(0)  # Show a progress bar (optional, improves UX)
#     # Create the request to OpenAI
#     response = client.chat.completions.create(
#         model='gpt-4-turbo',
#         messages=[
#             {
#                 "role": "user",
#                 "content": [
#                     {"type": "text",
#                      "text": f"You are a smart financial analyst who can determine calculations."
#                              f"Using only the image provided, what is the {selected_calculation.lower()} in 2018? "
#                              "Explain if this is a good result or not to someone who knows little about finance. "
#                              "I work at fintech but I'm not an expert in financial documents."
#                     },
#                     {"type": "image_url",
#                      "image_url": {"url": f"data:image/jpeg;base64,{encode_image(uploaded_file)}"}
#                     }
#                 ]
#             }
#         ],
#         max_tokens=800  # Limit the response length
#     )
#     progress_bar.progress(100)  # Move this line inside the button's logic
#     st.write("response:")
#     st.write(response.choices[0].message.content)


# import streamlit as st
# import base64
# from openai import OpenAI
# import os

# # Set OpenAI API key (you should add your actual API key here)
# os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY", "")

# # Function to encode the image to base64
# def encode_image(image_file):
#     return base64.b64encode(image_file.read()).decode('utf-8')

# # App title with styling
# st.markdown("<h1 style='color: #4CAF50;'>📊 Finanace Document Analyzer</h1>", unsafe_allow_html=True)
# st.markdown("Upload a balance sheet image and choose an analysis to get meaningful insights.")

# # File uploader widget
# uploaded_file = st.file_uploader("📁 Upload Image", type=['jpg', 'png', 'jpeg'])

# # Analysis options with brief descriptions
# analysis_options = {
#     "Debt to Asset Ratio": "Measures the percentage of assets financed by debt.",
#     "Current Ratio": "Compares current assets to current liabilities to assess liquidity.",
#     "Quick Ratio": "Examines short-term liquidity excluding inventory.",
#     "Net Profit Margin": "Analyzes how much profit is generated per dollar of revenue.",
#     "Return on Assets (ROA)": "Shows how efficiently assets are used to generate profit.",
#     "Equity Ratio": "Indicates the proportion of assets financed by equity.",
#     "Inventory Turnover": "Measures how often inventory is sold and replaced.",
#     "Working Capital": "Calculates current assets minus current liabilities.",
#     "Operating Cash Flow Ratio": "Shows the ability to cover liabilities with operating cash flow.",
#     "Gross Profit Margin": "Measures the profitability of products sold."
# }

# # Display options in a selectbox with descriptions
# st.markdown("<h3 style='color: #2196F3;'>🔍 Select an Analysis</h3>", unsafe_allow_html=True)
# selected_analysis = st.selectbox(
#     "Choose an analysis option:",
#     options=list(analysis_options.keys()),
#     format_func=lambda x: f"{x} - {analysis_options[x]}"
# )

# # Display uploaded image and details
# if uploaded_file is not None:
#     st.image(uploaded_file, caption="Uploaded Imagentainer=True)
#     st.markdown("<p style='color: #FF5722;'>Image successfully uploaded!</p>", unsafe_allow_html=True)

# # Button to trigger analysis
# if st.button("🚀 Analyze"):
#     st.markdown("<h3 style='color: #673AB7;'>Processing...</h3>", unsafe_allow_html=True)
#     progress_bar = st.progress(0)  # Initialize a progress bar
    
#     # Initialize OpenAI client
#     client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
#     # Simulate progress
#     for i in range(1, 101):
#         progress_bar.progress(i)
    
#     # Create OpenAI request
#     response = client.chat.completions.create(
#         model='gpt-4-turbo',
#         messages=[
#             {
#                 "role": "user",
#                 "content": [
#                     {"type": "text",
#                      "text": f"You are a smart financial analyst who can determine calculations. "
#                              f"Using only the image provided, what is the {selected_analysis.lower()}? "
#                              "Explain it in simple terms for someone new to finance."
#                     },
#                     {"type": "image_url",
#                      "image_url": {"url": f"data:image/jpeg;base64,{encode_image(uploaded_file)}"}
#                     }
#                 ]
#             }
#         ],
#         max_tokens=800  # Limit the response length
#     )
    
#     # Display results
#     progress_bar.progress(100)
#     st.success("Analysis Complete!")
#     st.markdown("<h3 style='color: #4CAF50;'>📝 Results:</h3>", unsafe_allow_html=True)
#     st.write(response.choices[0].message.content)

# # Footer
# st.markdown(
#     "<footer style='text-align: center; margin-top: 50px;'>"
#     "Developed with ❤️ by NeubAItics</footer>", 
#     unsafe_allow_html=True
# )




###############################################################################
import streamlit as st
import base64
from openai import OpenAI
import os
from fpdf import FPDF  # For creating PDF

# Set OpenAI API key (you should add your actual API key here)
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY", "")

# Function to encode the image to base64
def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

# Function to create a PDF for downloading
def create_pdf(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Analyzed Results", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=10)
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

import os

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
st.markdown("<h1>📊 Visual Finance Assitant</h1>", unsafe_allow_html=True)
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
    response = client.chat.completions.create(
        model='gpt-4-turbo',
        messages=[
            {
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
            }
        ],
        max_tokens=800  # Limit the response length
    )
    
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

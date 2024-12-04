import streamlit as st
import base64
from openai import OpenAI
import os
# Set OpenAI API key (you should add your actual API key here)
os.environ["OPENAI_API_KEY"] = "22"
# Function to encode the image to base64
def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')
# Streamlit app title
st.title("Balance Sheet Calculator")
# File uploader widget
uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
# Calculation options for the dropdown
calculation_options = [
    "Debt to Asset Ratio",
    "Current Ratio",
    "Quick Ratio"
]
# Selectbox for choosing the calculation
selected_calculation = st.selectbox("Select Calculation", calculation_options)
# Display uploaded image
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    # Initialize OpenAI client
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Using environment variable for security
    # Button to trigger calculation
    # Button to trigger calculation
if st.button("Calculate"):
    progress_bar = st.progress(0)  # Show a progress bar (optional, improves UX)
    # Create the request to OpenAI
    response = client.chat.completions.create(
        model='gpt-4-turbo',
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text",
                     "text": f"You are a smart financial analyst who can determine calculations."
                             f"Using only the image provided, what is the {selected_calculation.lower()} in 2018? "
                             "Explain if this is a good result or not to someone who knows little about finance. "
                             "I work at fintech but I'm not an expert in financial documents."
                    },
                    {"type": "image_url",
                     "image_url": {"url": f"data:image/jpeg;base64,{encode_image(uploaded_file)}"}
                    }
                ]
            }
        ],
        max_tokens=800  # Limit the response length
    )
    progress_bar.progress(100)  # Move this line inside the button's logic
    st.write("response:")
    st.write(response.choices[0].message.content)

# import streamlit as st
# import 64
# from openai import OpenAI
# import os 

# os.environ["OPENAI_API_KEY"] = "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"

# def encode_image(image_file):
#     return base64.b64encode(image_file.read().decode("utf-8"))

# st.title("Balance Sheet Calculator")

# uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

# calculation_option = ["debt to Asset ratio", "Current ratio", "Quick ratio"]

# selected_calculation = st.selectbox('select calculation', calculation_options)

# if uploaded_file is not None:
#     st.image(uploaded_file, caption='Upload Image', use_column_width = True)
#     client = OpenAI()
#     if st.button("Calculate"):
#         progress_bar =  st.progress(0)

# response = client.chat.completions.create(
#     model = "gpt-4-vision-preview",
#     messages=[
#         {
#             "role": "user",
#             "content": [
#                 {"type": "text", "text": f"You are a smart Financial Analyst who can determine calculate"}
#             ]
#         }
#     ]
# )


import streamlit as st
import base64
from openai import OpenAI
import os
# Set OpenAI API key (you should add your actual API key here)
os.environ["OPENAI_API_KEY"] = "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"
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

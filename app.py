# app.py
import streamlit as st
from generator import generate_description

st.set_page_config(page_title="Product Description Generator", page_icon="🛍️")

st.title("🛍️ Product Description Generator")
st.markdown("Generate compelling product descriptions using AI.")

# Input section
product_name = st.text_input("Product Name", placeholder="e.g. Ergonomic Office Chair")
tone = st.selectbox("Tone", ["professional", "casual", "luxury"])

# Session history
if "history" not in st.session_state:
    st.session_state.history = []

# Generate button
if st.button("Generate Description"):
    if not product_name.strip():
        st.warning("Please enter a product name.")
    else:
        with st.spinner("Generating..."):
            description = generate_description(product_name, tone)

        st.subheader("Generated Description")
        st.write(description)

        # Store in session history
        st.session_state.history.append({
            "product": product_name,
            "tone": tone,
            "description": description
        })

# Show session history
if st.session_state.history:
    st.divider()
    st.subheader("Previously Generated")
    for item in reversed(st.session_state.history):
        with st.expander(f"{item['product']} ({item['tone']})"):
            st.write(item["description"])
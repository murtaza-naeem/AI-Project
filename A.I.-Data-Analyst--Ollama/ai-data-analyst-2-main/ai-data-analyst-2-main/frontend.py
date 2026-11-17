#Step3: Build Streamlit frontend
import streamlit as st
from main import get_data_from_database
st.set_page_config(
    page_title="AI Data Analyst",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Data Analyst")
st.caption("Jeswin Joseph")
st.markdown("Ask questions about your data in natural language.")

user_query = st.text_area("💬 Enter your question:", placeholder="e.g., Total products sold in 2025")

if st.button("Analyze"):
    if user_query.strip() == "":
        st.warning("Please enter a question to analyze.")
    else:
        with st.spinner("Analyzing your query..."):
            database_response = get_data_from_database(user_query)
            fixed_answer = f"🔍 Here's the analysis for your query:\n\n**{database_response}**"

        st.success("Analysis complete!")
        st.markdown(fixed_answer)


st.markdown("""
    <style>
    .stApp {
#        background: linear-gradient(135deg, #000000 0%, #05010d 30%, #1a0b3d 65%, #4c1d95 100%);
#        background: radial-gradient(circle at center, #000000 0%, #0a0118 35%, #2d1b4e 70%, #4c1d95 100%);
         background: radial-gradient(circle at center, #000000 0%, #0a0118 40%, #0d1b3e 100%);
    }
    textarea {
        font-size: 16px !important;
    }
    </style>

""", unsafe_allow_html=True)



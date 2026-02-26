import streamlit as st
import requests

st.title("AI Code Reviewer")

code = st.text_area("Paste your code")

# Initialize session state
if "result" not in st.session_state:
    st.session_state.result = None

if st.button("Analyze"):
         response = requests.post(
        "https://codeanalyzer-fu5s.onrender.com/analyze",
        json={"code": code},
        timeout=60
    )

    if response.status_code == 200:
        st.session_state.result = response.json()
    else:
        st.error("Backend error. Check FastAPI terminal.")


# Display result only if available
if st.session_state.result:
    result = st.session_state.result

    st.subheader("📊 Complexity")
    st.write(result["complexity"])

    st.subheader("🐞 Bugs")
    for bug in result["bugs"]:
        st.write("•", bug)

    st.subheader("⚡ Improvements")
    for imp in result["improvements"]:
        st.write("•", imp)

    st.subheader("🚀 Better Approaches")
    for ba in result["better_approaches"]:
        st.write("•", ba)

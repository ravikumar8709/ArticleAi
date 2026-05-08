import streamlit as st
import requests

# Page config
st.set_page_config(page_title="AI Article Generator", page_icon="🧠")

st.title("🧠 AI Article Generator")
st.write("Generate detailed AI-powered articles instantly")

# Input
topic = st.text_input("Enter a topic")

# Button
if st.button("Generate Article"):

    if not topic.strip():
        st.warning("⚠️ Please enter a topic")
    else:
        with st.spinner("Generating article..."):

            try:
                res = requests.post(
                    "https://ravi40181.app.n8n.cloud/webhook/79ae0849-3477-417b-9c70-69cf5b08ef6a",
                    json={"topic": topic}
                )

                # Check response status
                if res.status_code != 200:
                    st.error(f"❌ API Error: {res.status_code}")
                    st.write(res.text)
                    st.stop()

                data = res.json()

                # Debug (optional)
                # st.write(data)

                # Handle both possible response formats
                if "article" in data:
                    article = data["article"]
                elif "choices" in data:
                    article = data["choices"][0]["message"]["content"]
                else:
                    st.error("❌ Unexpected response format")
                    st.write(data)
                    st.stop()

                # Show article
                st.subheader("📄 Generated Article")
                st.markdown(article)

                # Download button
                st.download_button(
                    label="⬇️ Download Article",
                    data=article,
                    file_name="article.txt"
                )

            except Exception as e:
                st.error(f"❌ Error: {e}")
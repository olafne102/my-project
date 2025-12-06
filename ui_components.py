import streamlit as st

# ============================
# COMPONENT 1: Pastel Header
# ============================
def pastel_header():
    st.markdown(
        """
        <div style="
            background: linear-gradient(90deg, #F8E8EE, #E3DFFD);
            padding: 22px;
            border-radius: 12px;
            text-align: center;
            margin-bottom: 25px;
        ">
            <h1 style="color:#5A4FCF; margin:0; font-size:36px;">
                🌸 Trợ Lý Phân Loại Cảm Xúc Tiếng Việt
            </h1>
            <p style="color:#444; margin-top:5px; font-size:16px;">
                Ứng dụng AI phân tích cảm xúc 🌸
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================
# COMPONENT 2: Input Box
# ============================
def input_box():
    st.markdown(
        """
        <style>
        .stTextArea textarea {
            border-radius: 12px !important;
            border: 2px solid #E3DFFD !important;
            background-color: #F8F9FA !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ============================
# COMPONENT 3: Sentiment Badge
# ============================
def sentiment_badge(sentiment):
    colors = {
        "POSITIVE": "#A3E4D7",
        "NEGATIVE": "#F5B7B1",
        "NEUTRAL": "#F9E79F",
    }

    st.markdown(
        f"""
        <div style="
            display:inline-block;
            padding:10px 20px;
            border-radius:20px;
            background-color:{colors.get(sentiment, '#EEE')};
            font-weight:bold;
            color:#333;
            font-size:18px;
        ">
            {sentiment}
        </div>
        """,
        unsafe_allow_html=True,
    )

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sentiment_utils import load_model, normalize_text, convert_label
from data_handler import save_history, get_history, clear_history, load_file
from ui_components import pastel_header, sentiment_badge, input_box

# ============================
# PAGE CONFIG
# ============================
st.set_page_config(
    page_title="Phân loại cảm xúc tiếng Việt",
    page_icon="🌿",
    layout="wide"
)

# ============================
# UI HEADER
# ============================
pastel_header()
input_box()

# ============================
# SIDEBAR – MODEL SELECTION
# ============================
st.sidebar.markdown("## 🌿 Tuỳ chọn mô hình AI")

model_choice = st.sidebar.selectbox(
    "Chọn mô hình Transformers:",
    [
        "nlptown/bert-base-multilingual-uncased-sentiment",
        "distilbert-base-multilingual-cased",
        "finiteautomata/bertweet-base-sentiment-analysis"
    ]
)

nlp = load_model(model_choice)

st.sidebar.markdown("---")
st.sidebar.markdown("### ⚙️ Cài đặt khác")
batch_mode = st.sidebar.checkbox("Kích hoạt phân tích nhiều câu")

st.sidebar.markdown("---")
if st.sidebar.button("🧹 Xoá toàn bộ lịch sử"):
    clear_history()
    st.sidebar.success("Đã xoá lịch sử phân loại!")

# ============================
# INPUT AREA
# ============================
st.markdown("### ✍️ Nhập câu hoặc đoạn văn tiếng Việt:")

user_text = st.text_area(
    "Nhập nội dung:",
    placeholder="Ví dụ: Hôm nay mình thấy rất vui và thoải mái...",
    height=150
)

col_run, col_reset = st.columns([1, 1])

run_btn = col_run.button("🌿 Phân tích cảm xúc", use_container_width=True)
col_reset.button("🔄 Xoá nội dung nhập", use_container_width=True)

# ============================
# HANDLE SINGLE SENTENCE MODE
# ============================
def classify_single(text):
    cleaned = normalize_text(text)
    res = nlp(cleaned)[0]
    senti = convert_label(res["label"])
    return senti, res["score"]


# ============================
# HANDLE MULTIPLE SENTENCES
# ============================
def classify_multiple(paragraph):
    sentences = [s.strip() for s in paragraph.split(".") if len(s.strip()) > 2]
    results = []

    for s in sentences:
        senti, score = classify_single(s)
        results.append([s, senti, score])
        save_history(s, senti)

    df = pd.DataFrame(results, columns=["Câu", "Cảm xúc", "Độ tự tin"])
    return df


# ============================
# MAIN PROCESSING
# ============================
if run_btn:
    if not user_text.strip():
        st.error("⚠️ Vui lòng nhập câu trước khi phân tích!")
    else:
        if batch_mode:
            st.markdown("### 🌿 Kết quả phân tích nhiều câu")
            df = classify_multiple(user_text)

            st.dataframe(df, use_container_width=True)

            # Draw chart
            st.markdown("### 📊 Biểu đồ cảm xúc")
            fig, ax = plt.subplots()

            df["Cảm xúc"].value_counts().plot(kind="bar", color=["#A3E4D7", "#F5B7B1", "#F9E79F"], ax=ax)
            ax.set_title("Phân bố cảm xúc")
            st.pyplot(fig)

            # Download results
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("⬇️ Tải kết quả CSV", csv, "ket_qua_cam_xuc.csv", "text/csv")

        else:
            senti, score = classify_single(user_text)
            st.markdown("### 🌿 Kết quả phân tích")
            sentiment_badge(senti)

            save_history(user_text, senti)

# ============================
# HISTORY SECTION
# ============================
st.markdown("---")
st.markdown("## 📜 Lịch sử phân loại gần đây")

history = get_history()

if len(history) == 0:
    st.info("🌿 Chưa có lịch sử.")
else:
    hist_df = pd.DataFrame(history, columns=["ID", "Câu", "Cảm xúc", "Thời gian"])
    st.dataframe(hist_df, use_container_width=True)

    # Chart history
    st.markdown("### 📊 Biểu đồ lịch sử cảm xúc")
    fig, ax = plt.subplots()
    
    hist_df["Cảm xúc"].value_counts().plot(kind="pie", autopct="%1.1f%%",
                                            colors=["#A3E4D7", "#F5B7B1", "#F9E79F"],
                                            ax=ax)
    ax.set_ylabel("")
    ax.set_title("Tỷ lệ cảm xúc trong lịch sử")

    st.pyplot(fig)

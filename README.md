Ứng dụng phân loại cảm xúc tiếng Việt sử dụng mô hình Transformer
Giới thiệu
Dự án này xây dựng một ứng dụng phân loại cảm xúc tiếng Việt dựa trên mô hình Transformer (BERT Multilingual).
Ứng dụng được phát triển bằng Python + Streamlit, cho phép người dùng phân tích cảm xúc của câu hoặc đoạn văn tiếng Việt theo 3 nhãn:
Positive
Neutral
Negative

Ngoài ra, ứng dụng hỗ trợ phân tích hàng loạt, lưu lịch sử phân tích vào SQLite và hiển thị biểu đồ thống kê cảm xúc.
Tính năng chính

🔹 1. Phân loại cảm xúc theo câu
Nhập câu tiếng Việt → Trả kết quả ngay.
Hỗ trợ cả câu có dấu, không dấu, teencode.
🔹 2. Phân tích nhiều câu trong đoạn văn
Tự động tách câu theo dấu chấm.
Phân tích từng câu độc lập.
🔹 3. Phân tích file dữ liệu
Hỗ trợ CSV / Excel.
Phân tích hàng loạt nhiều dòng cùng lúc.
Xuất file kết quả.
🔹 4. Lưu lịch sử bằng SQLite
Tự động lưu lại câu + nhãn + thời gian.
Hiển thị bảng lịch sử.
Có chức năng xóa toàn bộ lịch sử.
🔹 5. Biểu đồ trực quan
Biểu đồ cột (bar chart).
Biểu đồ tròn (pie chart).
🔹 6. Tuỳ chọn mô hình Transformer
nlptown/bert-base-multilingual-uncased-sentiment
distilbert-base-multilingual-cased

Cấu trúc dự án
viet_sentiment_app/
│
├── app.py                 # File giao diện chính Streamlit
├── sentiment_utils.py      # Xử lý mô hình + NLP
├── data_handler.py         # Quản lý SQLite
├── ui_components.py        # Component UI tái sử dụng
│
├── history.db              # CSDL lưu lịch sử phân tích
├── requirements.txt        # Danh sách thư viện
└── README.md               # Tài liệu dự án

Cài đặt & Chạy ứng dụng
📌 1. Clone repo
git clone https://github.com/<your-account>/<your-repo>.git
cd viet_sentiment_app
2. Tạo môi trường ảo
Window: python -m venv venv
venv\Scripts\activate
3. Cài đặt thư viện
pip install -r requirements.txt
4. Chạy ứng dụng
streamlit run app.py

Ứng dụng sẽ chạy tại:
👉 http://localhost:8501
Mô hình AI được sử dụng
Ứng dụng dựa trên các mô hình pre-trained từ HuggingFace:
| Model                                              | Mô tả                                                     |
| -------------------------------------------------- | --------------------------------------------------------- |
| `nlptown/bert-base-multilingual-uncased-sentiment` | Trả về nhãn 1–5 sao, sau đó được chuyển thành POS/NEU/NEG |
| `distilbert-base-multilingual-cased`               | Phiên bản compact, nhẹ hơn, chạy nhanh hơn                |

Quy trình xử lý:
Chuẩn hoá văn bản tiếng Việt
Loại bỏ teencode, viết tắt
Token hóa → Transformer
Chuyển kết quả sao → 3 nhãn cảm xúc
Lưu lịch sử
Hiển thị kết quả + biểu đồ

Lưu trữ lịch sử (SQLite)
CSDL: history.db
Bảng lịch sử:
| ID | Text | Sentiment | Time |
| -- | ---- | --------- | ---- |
Dữ liệu này được dùng để:
Hiển thị bảng lịch sử
Vẽ biểu đồ cảm xúc
- Requirements
streamlit
transformers
torch
sentencepiece
pandas
matplotlib
Hướng phát triển

Huấn luyện mô hình dành riêng cho tiếng Việt
Tích hợp API RESTful
Bổ sung phân tích đa cảm xúc (anger, joy, disgust…)
Tích hợp giọng nói → phân tích cảm xúc từ audio
Dashboard theo thời gian thực
Tác giả:
Sinh viên: Đinh Thị Lan Trinh

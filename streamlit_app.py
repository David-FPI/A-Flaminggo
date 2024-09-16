import streamlit as st

# Hàm để thiết lập hình nền
def set_bg_image():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.unsplash.com/photo-1568223288053-3cf3f6e915f3?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80");
            background-attachment: fixed;
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center center;
        }}
        /* Tùy chỉnh màu chữ và các thuộc tính khác nếu cần */
        .stApp {{
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_image()

# Tiêu đề của ứng dụng
st.title("🎈 A-Flamingo Club")

# CSS cho hình ảnh và mô tả
st.markdown(
    """
    <style>
    .container {
        display: flex;
        align-items: center;
        margin-top: 50px;
        background-color: rgba(0, 0, 0, 0.6); /* Nền trong suốt để nội dung nổi bật trên hình nền */
        padding: 20px;
        border-radius: 15px;
    }
    .icon {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        margin-right: 20px;
        border: 3px solid white;
        object-fit: cover;
    }
    .description {
        font-size: 22px;
        font-weight: bold;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Hiển thị hình ảnh và mô tả
st.markdown(
    """
    <div class="container">
        <img src="https://scontent.fsgn5-8.fna.fbcdn.net/v/t39.30808-6/447678075_767488495531324_3390405170555493979_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=xuaEcEZMd6sQ&_nc_ht=scontent.fsgn5-8.fna&oh=00_AfC8vxY3WdPcdMR6I6odqsR6d1yvJ9E7T8vUMiE6J7PUsw&oe=65282D9F" class="icon">
        <div class="description">
            <strong>California Housing Data</strong><br>
            Explore the housing data in California with visualizations and insights!
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Liên kết hỗ trợ
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

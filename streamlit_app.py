import streamlit as st

# Hình ảnh đầu tiên với kích thước lớn hơn
st.image(
    "https://scontent.fsgn5-3.fna.fbcdn.net/v/t39.30808-6/456808805_818729667073873_2821881578807023624_n.jpg?stp=dst-jpg_s960x960&_nc_cat=104&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=KFAuiixDV6AQ7kNvgE4kUXt&_nc_ht=scontent.fsgn5-3.fna&_nc_gid=AmAWqRZSaMovwE9p17qGNK_&oh=00_AYB-MMasH9o0I0XXGiZz2pKzLUiqJoSDJrHhFenJbtOXDQ&oe=66ED82B6",
    width=2000  # Kích thước lớn hơn cho hình ảnh đầu tiên
)

# Custom CSS để thiết lập nền galaxy và tràn viền
st.markdown(
    """
    <style>
    /* Đặt hình nền galaxy cho toàn bộ body */
    body {
        background-image: url('https://img.freepik.com/premium-photo/pastel-clouds-background-pastel-cloud-background-dreamy-clouds-background-pastel-sky-background-ai-generative_703884-13035.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;
    }

    /* Xóa bỏ mọi khoảng trống giữa các phần tử */
    .stApp {
        padding: 0;
        margin: 0;
        background-color: rgba(0, 0, 0, 0.7); /* Nền mờ tối cho phần nội dung */
        border-radius: 0;
        width: 100%;
        height: 100%;
    }

    /* Đảm bảo hình ảnh không có khoảng trống */
    img {
        margin: 0;
        padding: 0;
        width: 100%; /* Đặt hình ảnh tràn viền */
    }

    /* Thiết lập cho các tiêu đề */
    h1 {
        color: #ff69b4; /* Màu hồng sáng phù hợp với nền galaxy */
        text-shadow: 2px 2px 4px #000000;
    }

    /* Container chứa hình và mô tả */
    .container {
        display: flex;
        align-items: center;
        margin: 0px; /* Xóa bỏ khoảng trống giữa các phần tử */
        padding: 0px;
        background-color: rgba(255, 255, 255, 0.1); /* Nền mờ trắng cho phần container */
        width: 100%;
    }

    /* Hình ảnh tròn */
    .icon {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        margin-right: 20px;
        border: 3px solid white;
    }

    /* Văn bản mô tả */
    .description {
        font-size: 22px;
        font-weight: bold;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Hiển thị hình ảnh tròn và mô tả
st.markdown(
    """
    <div class="container">
        <img src="https://scontent.fsgn5-8.fna.fbcdn.net/v/t39.30808-6/447678075_767488495531324_3390405170555493979_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=xuaEcEZMd6sQ7kNvgHLiqBW&_nc_ht=scontent.fsgn5-8.fna&_nc_gid=AWVa4ylzPoVZW2g61tLsXxo&oh=00_AYCzt7Ed6xiewhnBUFT4nEFDwYj9gjdXoQBX_fyHNLYGEw&oe=66EDA697" class="icon">
        <div class="description">
            <strong>California Housing Data</strong><br>
            Explore the housing data in California with visualizations and insights!
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Liên kết hành động
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

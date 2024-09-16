import streamlit as st

# Custom CSS để làm cho hình nền và các hình ảnh khác tràn toàn màn hình
st.markdown(
    """
    <style>
    /* Xóa khoảng trống mặc định của trang */
    body, html {
        height: 100%;
        margin: 0;
        padding: 0;
        overflow: hidden;
    }

    /* Đặt hình ảnh nền chiếm toàn màn hình */
    .fullscreen-image {
        background-image: url('https://img.freepik.com/premium-photo/pastel-clouds-background-pastel-cloud-background-dreamy-clouds-background-pastel-sky-background-ai-generative_703884-13035.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh; /* Chiều cao 100% màn hình */
        width: 100vw; /* Chiều rộng 100% màn hình */
        position: absolute;
        top: 0;
        left: 0;
        z-index: -1; /* Đảm bảo hình nền ở dưới cùng */
    }
    
    /* Đảm bảo phần nội dung phía trên hình nền được hiển thị rõ ràng */
    .stApp {
        background-color: transparent;
        position: relative;
        z-index: 1; /* Đảm bảo nội dung phía trên hình nền */
        padding: 20px; /* Thêm khoảng cách cho nội dung */
    }

    /* Thiết lập cho tiêu đề chính */
    h1 {
        color: #ff69b4; /* Màu hồng sáng phù hợp với chủ đề galaxy */
        text-shadow: 2px 2px 4px #000000;
    }

    /* Container chứa hình và mô tả */
    .container {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 20px 0;
        background-color: rgba(255, 255, 255, 0.2); /* Nền mờ trắng cho phần container */
        padding: 20px;
        border-radius: 15px;
    }

    /* Hình ảnh tròn */
    .icon {
        border-radius: 50%;
        width: 200px; /* Kích thước lớn hơn cho hình ảnh */
        height: 200px;
        margin-right: 20px;
        border: 4px solid white;
    }

    /* Văn bản mô tả */
    .description {
        font-size: 24px;
        font-weight: bold;
        color: white;
    }

    /* Thêm padding và margin cho văn bản mô tả */
    .description strong {
        font-size: 26px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Hiển thị hình ảnh đầu tiên với kích thước lớn hơn
st.image(
    "https://scontent.fsgn5-3.fna.fbcdn.net/v/t39.30808-6/456808805_818729667073873_2821881578807023624_n.jpg?stp=dst-jpg_s960x960&_nc_cat=104&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=KFAuiixDV6AQ7kNvgE4kUXt&_nc_ht=scontent.fsgn5-3.fna&_nc_gid=AmAWqRZSaMovwE9p17qGNK_&oh=00_AYB-MMasH9o0I0XXGiZz2pKzLUiqJoSDJrHhFenJbtOXDQ&oe=66ED82B6",
    width=800  # Kích thước lớn hơn cho hình ảnh đầu tiên
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

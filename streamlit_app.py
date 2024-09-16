import streamlit as st

# Ẩn main menu và footer của Streamlit
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Custom CSS để thiết lập giao diện full màn hình không có khoảng trống
st.markdown(
    """
    <style>
    /* Reset toàn bộ margin và padding */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* Thiết lập body và .stApp để full màn hình */
    body, .stApp, .element-container, .css-1d391kg, .css-1v3fvcr, .css-dm3055, .css-1q1n0ol {
        width: 100vw !important;
        max-width: 100vw !important;
        padding: 0 !important;
        margin: 0 !important;
        overflow-x: hidden !important;
    }
    
    /* Ẩn thanh cuộn ngang */
    body::-webkit-scrollbar {
        display: none;
    }
    
    /* Thiết lập background */
    .stApp {
        background-image: url('https://img.freepik.com/premium-photo/pastel-clouds-background-pastel-cloud-background-dreamy-clouds-background-pastel-sky-background-ai-generative_703884-13035.jpg');
        background-size: cover;
        background-position: center;
        display: flex;
        flex-direction: column;
    }
    
    /* Styling cho container chính */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        min-height: 100vh;
        width: 100%;
        background-color: rgba(0, 0, 0, 0.6);
    }
    
    /* Styling cho hình ảnh */
    .full-width-image {
        width: 100%;
        height: auto;
        object-fit: cover;
    }
    
    /* Styling cho container chứa icon và mô tả */
    .icon-container {
        display: flex;
        align-items: flex-start;
        width: 100%;
        padding: 20px;
    }
    
    /* Circular image styling */
    .icon {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        margin-right: 20px;
        border: 3px solid white;
        flex-shrink: 0;
    }
    
    /* Styling cho phần mô tả */
    .description {
        color: white;
        font-size: 16px;
        display: flex;
        flex-direction: column;
    }
    
    /* Styling cho tiêu đề */
    .title {
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #ff69b4;
        display: flex;
        align-items: center;
    }
    
    /* Styling cho icon hồng hạc */
    .flamingo-icon {
        width: 40px;
        height: 40px;
        margin-right: 10px;
        fill: #ff69b4;
    }
    
    /* Styling cho caption */
    .caption {
        font-size: 14px;
        line-height: 1.5;
    }
    
    /* Styling cho link */
    .link-text {
        color: #ff69b4;
        font-size: 18px;
        margin-top: 20px;
        padding: 0 20px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML structure cho layout full màn hình với tiêu đề nổi bật và caption, bao gồm icon con hạc
st.markdown(
    """
    <div class="main-container">
        <img src="https://scontent.fsgn5-3.fna.fbcdn.net/v/t39.30808-6/456808805_818729667073873_2821881578807023624_n.jpg?stp=dst-jpg_s960x960&_nc_cat=104&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=KFAuiixDV6AQ7kNvgE4kUXt&_nc_ht=scontent.fsgn5-3.fna&_nc_gid=AmAWqRZSaMovwE9p17qGNK_&oh=00_AYB-MMasH9o0I0XXGiZz2pKzLUiqJoSDJrHhFenJbtOXDQ&oe=66ED82B6" class="full-width-image">
        <div class="icon-container">
            <img src="https://scontent.fsgn5-8.fna.fbcdn.net/v/t39.30808-6/447678075_767488495531324_3390405170555493979_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=xuaEcEZMd6sQ7kNvgHLiqBW&_nc_ht=scontent.fsgn5-8.fna&_nc_gid=AWVa4ylzPoVZW2g61tLsXxo&oh=00_AYCzt7Ed6xiewhnBUFT4nEFDwYj9gjdXoQBX_fyHNLYGEw&oe=66EDA697" class="icon">
            <div class="description">
                <div class="title">
                    <svg class="flamingo-icon" viewBox="0 0 512 512">
                        <path d="M183.253 36.323c1.38-2.374 3.287-4.44 5.622-6.203 7.819-5.89 18.854-6.618 28.24-2.315 38.942 17.859 61.731 36.458 73.847 55.202 13.424 20.723 13.529 41.625 10.027 58.277-3.538 16.816-11.683 29.366-18.132 36.72-6.495 7.406-13.994 13.259-19.855 16.906l1.112 2.456c7.47-1.986 15.034-5.24 21.912-10.201 13.45-9.712 28.022-38.282 34.992-75.397 1.96-10.438 11.947-17.312 22.395-15.38 10.441 1.932 17.34 11.952 15.409 22.393-8.92 47.598-28.214 85.351-53.548 103.374-12.865 9.157-26.43 13.73-39.498 15.318-3.808 11.482-5.735 23.814-5.626 36.504.244 28.244 18.325 47.387 41.658 58.992 48.217 23.994 133.294 24.742 193.594 8.766V144.895c0-9.603 3.763-18.628 10.606-25.471 8.903-8.903 21.707-12.164 33.675-8.62 11.967 3.544 20.424 13.89 21.631 26.434l12.377 128.741v197.698c0 26.51-21.49 48-48 48h-128c-8.548 0-16.583-2.258-23.532-6.208-60.384 20.49-143.893 21.972-199.946-5.591-38.952-19.097-68.782-52.675-69.19-99.915-.359-41.585 17.376-78.51 45.513-105.229-25.874-22.653-44.09-50.285-50.936-81.581-11.492-52.387 3.336-110.188 43.794-164.83zm265.081 243.354l-42.667-85.333c-3.094-6.196-1.21-13.696 4.44-17.672 5.649-3.976 13.397-3.089 18.148 2.079l64 69.333c4.753 5.148 4.763 13.138.025 18.299l-32 35.2c-4.737 5.217-12.795 5.79-18.219 1.312-5.421-4.478-6.515-12.48-2.484-18.218z"/>
                    </svg>
                    A-Flamingo Club
                </div>
                <div class="caption">
                    Câu lạc bộ âm nhạc A-Flamingo là nơi hội tụ của những tâm hồn yêu thích âm nhạc tại Trường Cao đẳng Anh Quốc BTEC FPT Hồ Chí Minh. Chúng tôi tự hào là một cộng đồng năng động và sáng tạo, nơi các thành viên có cơ hội thể hiện niềm đam mê âm nhạc của mình thông qua các buổi biểu diễn, workshop và các hoạt động giao lưu âm nhạc. A-Flamingo không chỉ là nơi luyện tập kỹ năng âm nhạc mà còn là môi trường lý tưởng để các bạn trẻ phát triển khả năng làm việc nhóm, sáng tạo và kết nối với những người có cùng sở thích. Hãy gia nhập chúng tôi để cùng nhau tạo nên những bản nhạc tuyệt vời và những kỷ niệm đáng nhớ
                </div>
            </div>
        </div>
        <div class="link-text">
            Let's start building! For help and inspiration, head over to <a href="https://docs.streamlit.io/" target="_blank">docs.streamlit.io</a>.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

import streamlit as st
import streamlit.components.v1 as components

# Create sidebar and allow users to select a topic
selected_topic = st.sidebar.selectbox("Chọn chủ đề", ["Giới thiệu", "Quá trình phát triển", "Cập nhật hoạt động mới"])

# Define the content for each topic
topics = {
    "Giới thiệu": """
    <div class="main-container">
        <div class="swiper-container">
            <div class="swiper-wrapper">
                <div class="swiper-slide"><img src="https://scontent.fsgn5-3.fna.fbcdn.net/v/t39.30808-6/456808805_818729667073873_2821881578807023624_n.jpg?stp=dst-jpg_s960x960&_nc_cat=104&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=KFAuiixDV6AQ7kNvgE4kUXt&_nc_ht=scontent.fsgn5-3.fna&_nc_gid=AmAWqRZSaMovwE9p17qGNK_&oh=00_AYB-MMasH9o0I0XXGiZz2pKzLUiqJoSDJrHhFenJbtOXDQ&oe=66ED82B6"></div>
                <div class="swiper-slide"><img src="https://scontent.fsgn5-8.fna.fbcdn.net/v/t39.30808-6/447678075_767488495531324_3390405170555493979_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=xuaEcEZMd6sQ7kNvgHLiqBW&_nc_ht=scontent.fsgn5-8.fna&_nc_gid=AWVa4ylzPoVZW2g61tLsXxo&oh=00_AYCzt7Ed6xiewhnBUFT4nEFDwYj9gjdXoQBX_fyHNLYGEw&oe=66EDA697"></div>
                <div class="swiper-slide"><img src="https://example.com/image3.jpg"></div>
                <div class="swiper-slide"><img src="https://example.com/image4.jpg"></div>
            </div>
            <div class="swiper-scrollbar"></div>
        </div>
        <div class="icon-container">
            <img src="https://scontent.fsgn5-8.fna.fbcdn.net/v/t39.30808-6/447678075_767488495531324_3390405170555493979_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=xuaEcEZMd6sQ7kNvgHLiqBW&_nc_ht=scontent.fsgn5-8.fna&_nc_gid=AWVa4ylzPoVZW2g61tLsXxo&oh=00_AYCzt7Ed6xiewhnBUFT4nEFDwYj9gjdXoQBX_fyHNLYGEw&oe=66EDA697" class="icon">
            <div class="description">
                <div class="title">
                    <img src="https://cdn-icons-png.flaticon.com/128/3807/3807146.png" alt="Icon flamingo" class="title-icon">
                    A-Flamingo Club
                </div>
                <div class="caption">
                    Câu lạc bộ âm nhạc A-Flamingo là nơi hội tụ của những tâm hồn yêu thích âm nhạc tại Trường Cao đẳng Anh Quốc BTEC FPT Hồ Chí Minh. 
                    Chúng tôi tự hào là một cộng đồng năng động và sáng tạo, nơi các thành viên có cơ hội thể hiện niềm đam mê âm nhạc của mình thông qua các buổi biểu diễn, 
                    workshop và các hoạt động giao lưu âm nhạc. A-Flamingo không chỉ là nơi luyện tập kỹ năng âm nhạc mà còn là môi trường lý tưởng để các bạn trẻ phát triển khả năng làm việc nhóm, 
                    sáng tạo và kết nối với những người có cùng sở thích. Hãy gia nhập chúng tôi để cùng nhau tạo nên những bản nhạc tuyệt vời và những kỷ niệm đáng nhớ.
                </div>
                <div class="slogan">
                    <i>A-Flamingo _ Kết nối đam mê _Tỏa sáng âm nhạc</i>
                </div>
            </div>
        </div>
    </div>
    """,
    "Quá trình phát triển": """
        <h2>Quá trình phát triển của A-Flamingo</h2>
        <p><b>Năm 2022:</b> Câu lạc bộ được thành lập và tổ chức các hoạt động nhỏ để giới thiệu đến các thành viên.</p>
        <p><b>Năm 2023:</b> A-Flamingo tổ chức thành công sự kiện âm nhạc lớn đầu tiên, thu hút sự quan tâm của đông đảo sinh viên.</p>
        <p><b>Năm 2024:</b> Chúng tôi đang lên kế hoạch cho nhiều hoạt động mới như workshop sáng tác nhạc, buổi biểu diễn kết hợp với các câu lạc bộ khác...</p>
    """,
    "Cập nhật hoạt động mới": """
        <h2>Hoạt động sắp tới</h2>
        <ul>
            <li>Workshop sáng tác nhạc: 15/04/2024</li>
            <li>Buổi biểu diễn kết hợp với câu lạc bộ nhảy: 30/04/2024</li>
            <li>Tham gia lễ hội âm nhạc trường: 15/05/2024</li>
        </ul>
    """
}

# Display the content for the selected topic
st.markdown(topics[selected_topic], unsafe_allow_html=True)

# Custom CSS for responsive design and Swiper
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    @import url('https://unpkg.com/swiper/swiper-bundle.min.css');

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    /* Fullscreen settings */
    body, .stApp, .element-container, .css-1d391kg, .css-1v3fvcr, .css-dm3055, .css-1q1n0ol {
        width: 100vw !important;
        max-width: 100vw !important;
        padding: 0 !important;
        margin: 0 !important;
        overflow-x: hidden !important;
    }

    /* Background setup */
    .stApp {
        background-image: url('https://img.freepik.com/premium-photo/pastel-clouds-background-pastel-cloud-background-dreamy-clouds-background-pastel-sky-background-ai-generative_703884-13035.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        display: flex;
        flex-direction: column;
    }

    .main-container, .main-container1 {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        min-height: 100vh;
        width: 100%;
        background-color: rgba(0, 0, 0, 0.6);
        padding: 20px;
    }

    .swiper-container {
        width: 100%;
        height: 50vh;
        margin-bottom: 20px;
    }

    .swiper-slide img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .swiper-scrollbar {
        opacity: 1;
        height: 10px;
        background-color: rgba(255, 255, 255, 0.3);
    }

    .swiper-scrollbar-drag {
        background-color: rgba(255, 255, 255, 0.8);
    }

    .icon-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        padding: 20px 0;
    }

    .icon {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        border: 3px solid white;
        margin-bottom: 20px;
    }

    .description {
        color: white;
        font-size: 16px;
        text-align: center;
    }

    .title {
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #ff69b4;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
    }

    .title-icon {
        width: 30px;
        height: 30px;
        margin-right: 10px;
    }

    .caption {
        font-size: 14px;
        line-height: 1.5;
        margin-bottom: 20px;
    }

    .slogan {
        font-family: 'Montserrat', sans-serif;
        font-size: 16px;
        font-weight: bold;
        color: #fff;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        animation: fadeIn 1s ease-in-out;
        letter-spacing: 2px;
        margin-top: 20px;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .icon-container {
            padding: 10px 0;
        }

        .icon {
            width: 100px;
            height: 100px;
        }

        .title {
            font-size: 24px;
        }

        .caption {
            font-size: 12px;
        }

        .slogan {
            font-size: 14px;
        }
    }

    @media (max-width: 480px) {
        .main-container, .main-container1 {
            padding: 10px;
        }

        .title {
            font-size: 20px;
        }

        .title-icon {
            width: 20px;
            height: 20px;
        }

        .caption {
            font-size: 10px;
        }

        .slogan {
            font-size: 12px;
        }
    }

    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>

    <script src="https://unpkg.com/swiper/swiper-bundle.min.js"></script>
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        new Swiper('.swiper-container', {
            direction: 'horizontal',
            slidesPerView: 1,
            spaceBetween: 30,
            loop: true,
            scrollbar: {
                el: '.swiper-scrollbar',
                hide: false,
                draggable: true,
            },
        });
    });
    </script>
""", unsafe_allow_html=True)

# Initialize Swiper
components.html(
    """
    <script>
    var swiper = new Swiper('.swiper-container', {
        direction: 'horizontal',
        slidesPerView: 1,
        spaceBetween: 30,
        loop: true,
        scrollbar: {
            el: '.swiper-scrollbar',
            hide: false,
            draggable: true,
        },
    });
    </script>
    """,
    height=0,
)

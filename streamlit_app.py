import streamlit as st

# Create sidebar and allow users to select a topic
selected_topic = st.sidebar.selectbox("Chọn chủ đề", ["Giới thiệu", "Quá trình phát triển", "Cập nhật hoạt động mới"])

# Define the content for each topic
topics = {
topics = {
    "Giới thiệu": """
    <div class="main-container">
        <img src="https://scontent.fsgn5-3.fna.fbcdn.net/v/t39.30808-6/456808805_818729667073873_2821881578807023624_n.jpg?stp=dst-jpg_s960x960&_nc_cat=104&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=KFAuiixDV6AQ7kNvgE4kUXt&_nc_ht=scontent.fsgn5-3.fna&_nc_gid=AmAWqRZSaMovwE9p17qGNK_&oh=00_AYB-MMasH9o0I0XXGiZz2pKzLUiqJoSDJrHhFenJbtOXDQ&oe=66ED82B6" class="full-width-image">
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
    <div class="main-container1">
        <div class="description">
            <div class="title">
                <img src="https://cdn-icons-png.flaticon.com/128/3807/3807146.png" alt="Icon flamingo" class="title-icon">
                Introduction
            </div>
            <p>🥳 Chào mừng bạn đến với CLB AFlamingo – ngôi nhà chung của sự sáng tạo và đam mê! 🦩🦩🦩🦩🦩</p>
            <p>🌻1. Mục tiêu và sứ mệnh:<br>
            CLB AFlamingo được thành lập với mục đích tạo nên một sân chơi sôi động cho các bạn sinh viên. Không cần có năng khiếu đặc biệt, chỉ cần bạn yêu thích trải nghiệm, khám phá và kết nối, AFlamingo luôn chào đón bạn. Đây không chỉ là nơi để bạn thể hiện bản thân mà còn là cơ hội để học hỏi, phát triển kỹ năng và xây dựng những mối quan hệ win-win.</p>
            <p>🌻2. Lịch sử hình thành và phát triển:<br>
            Được thành lập vào ngày 07.03.2019, CLB AFlamingo đã trải qua nhiều giai đoạn phát triển và ngày càng khẳng định vị thế của mình trong cộng đồng sinh viên. Với sự nhiệt huyết và sáng tạo, chúng tôi đã tổ chức nhiều hoạt động và sự kiện đáng nhớ, góp phần tạo nên một môi trường năng động và thân thiện.</p>
            <p>🌻3. Các hoạt động chính:<br>
            CLB AFlamingo luôn tự hào với nhiều hoạt động phong phú và đa dạng:<br>
            🔥 BSK: BAN SỰ KIỆN là người kiến tạo những khoảnh khắc đáng nhớ và trải nghiệm tuyệt vời cho các TV và SV, biến những ý tưởng sáng tạo thành hiện thực, mang đến những khoảnh khắc đáng nhớ. Không yêu cầu bạn có kỹ năng từ trước, chỉ cần sự nhiệt huyết, sẵn sàng gia nhập hội con nhà AFla, mọi thứ sẽ có AFla lo.<br>
            🔥 BNK: BAN NĂNG KHIẾU là nơi những tinh thần âm nhạc hội tụ, là sân chơi hoàn hảo cho những ai đam mê hát, đàn, diễn xuất và các loại hình nghệ thuật khác có thể thỏa sức đam mê, tỏa sáng tài năng trên sân khấu, hay xuất hiện trong những MV Cover chất như nước cất từ CLB. Quan trọng cũng không cần bạn phải quá xuất sắc, chỉ bạn thích là được. Một tinh thần vui vẻ, hòa đồng và không ngại thể hiện bản thân là điều mà Afla quan tâm.<br>
            🔥 BTT: BAN TRUYỀN THÔNG người kết nối của CLB là ngọn lửa luôn cháy rực để truyền đạt kết nối giữa CLB và các bạn SV, mang những thông điệp, giá trị và tinh thần của CLB đến gần hơn với mọi người. Như 2 ban trên cũng không cần bạn quá xuất sắc, Afla chỉ cần 1 chữ "muốn" từ bạn.<br>
            🔥 Ngoài ra, AFla còn tổ chức các workshop phát triển kỹ năng, talkshow giao lưu, dự án thiện nguyện ý nghĩa.</p>
        </div>
    </div>
    <div class="slideshow-container">
        <div class="mySlides fade">
            <img src="https://scontent.fsgn5-5.fna.fbcdn.net/v/t39.30808-6/456803149_818732327073607_4970075696503025209_n.jpg?stp=dst-jpg_s960x960&_nc_cat=101&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=KXtaTcf1npEAX8-3knF&_nc_ht=scontent.fsgn5-5.fna&_nc_gid=AWVa4y1mUkqMWT-1vXPPBDA&oh=00_AYR0qFchZT3BBGI4jVbQZ4TgUL3NGxHy1GOOtVx_vZnFg&oe=66ED83A3" style="width:100%">
        </div>

        <div class="mySlides fade">
            <img src="https://scontent.fsgn5-5.fna.fbcdn.net/v/t39.30808-6/456803881_818730157073824_1990864967045067246_n.jpg?stp=dst-jpg_s960x960&_nc_cat=107&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=bOgv8DWBuA0AX9SxSRc&_nc_ht=scontent.fsgn5-5.fna&_nc_gid=AWVa4y1mUkqMWT-1vXPPBDA&oh=00_AYbZg9cQFM01_LCz_VPSME7NckMQGCE-o_vN9_j0w5wZA&oe=66ED85A8" style="width:100%">
        </div>

        <div class="mySlides fade">
            <img src="https://scontent.fsgn5-5.fna.fbcdn.net/v/t39.30808-6/456802921_818731807073659_4774012907947636121_n.jpg?stp=dst-jpg_s960x960&_nc_cat=101&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=W2UZG1CSLv0AX9F7W_g&_nc_ht=scontent.fsgn5-5.fna&_nc_gid=AWVa4y1mUkqMWT-1vXPPBDA&oh=00_AYV68BMSH6g7MAvvQHpAlhtI0FvA1HLDD2J56tVw4-TPg&oe=66ED86B7" style="width:100%">
        </div>

        <div class="mySlides fade">
            <img src="https://scontent.fsgn5-5.fna.fbcdn.net/v/t39.30808-6/456806124_818730497073790_5654556726415976711_n.jpg?stp=dst-jpg_s960x960&_nc_cat=106&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=8Ve7Sx8aYQ0AX8tt9F8&_nc_ht=scontent.fsgn5-5.fna&_nc_gid=AWVa4y1mUkqMWT-1vXPPBDA&oh=00_AYdoRnbzj1i8zLTOJYZPFE7fZwIUk8ukpH8hxMXYEtgMw&oe=66ED8A3E" style="width:100%">
        </div>

        <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
        <a class="next" onclick="plusSlides(1)">&#10095;</a>
    </div>

    <br>

    <div style="text-align:center">
        <span class="dot" onclick="currentSlide(1)"></span>
        <span class="dot" onclick="currentSlide(2)"></span>
        <span class="dot" onclick="currentSlide(3)"></span>
        <span class="dot" onclick="currentSlide(4)"></span>
    </div>

    <style>
        .slideshow-container {
            position: relative;
            margin: auto;
        }

        .mySlides {
            display: none;
        }

        img {
            max-width: 100%;
            height: auto;
        }

        .prev, .next {
            cursor: pointer;
            position: absolute;
            top: 50%;
            width: auto;
            padding: 16px;
            color: white;
            font-weight: bold;
            font-size: 18px;
            transition: 0.6s ease;
            border-radius: 0 3px 3px 0;
            user-select: none;
        }

        .next {
            right: 0;
            border-radius: 3px 0 0 3px;
        }

        .prev:hover, .next:hover {
            background-color: rgba(0,0,0,0.8);
        }

        .dot {
            cursor: pointer;
            height: 15px;
            width: 15px;
            margin: 0 2px;
            background-color: #bbb;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.6s ease;
        }

        .active, .dot:hover {
            background-color: #717171;
        }
    </style>

    <script>
        let slideIndex = 1;
        showSlides(slideIndex);

        function plusSlides(n) {
            showSlides(slideIndex += n);
        }

        function currentSlide(n) {
            showSlides(slideIndex = n);
        }

        function showSlides(n) {
            let i;
            const slides = document.getElementsByClassName("mySlides");
            const dots = document.getElementsByClassName("dot");
            if (n > slides.length) {slideIndex = 1}
            if (n < 1) {slideIndex = slides.length}
            for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";
            }
            for (i = 0; i < dots.length; i++) {
                dots[i].className = dots[i].className.replace(" active", "");
            }
            slides[slideIndex - 1].style.display = "block";
            dots[slideIndex - 1].className += " active";
        }
    </script>
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
if selected_topic in topics:
    st.markdown(topics[selected_topic], unsafe_allow_html=True)


# Custom CSS for responsive design
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

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

    .full-width-image {
        width: 100%;
        height: auto;
        object-fit: cover;
        max-height: 50vh;
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
""", unsafe_allow_html=True)









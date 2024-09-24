import streamlit as st

# Tạo ứng dụng Streamlit
st.title("Trình Chiếu Ảnh Tự Động và Chuyển Đổi Thủ Công")

# HTML/CSS/JS cho trình chiếu ảnh
html_code = """
<div class="slideshow-container">
    <div class="mySlides">

HÌNH TÔI ĐANG BỊ THIẾU CHIỀU DÀI, CÓ LẼ DO CHIỀU DÀI KHÔNG ĐỦ. TÔI MUỐN NÓ HIỆN ĐẦY ĐỦ HÌNH CỦA TÔI GỬI VÔ ĐÂY THÌ LÀM SAO
 
        <img src="https://scontent.fsgn5-5.fna.fbcdn.net/v/t39.30808-6/460061948_832852265661613_8913271978209387416_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=833d8c&_nc_ohc=gfNVneYypqwQ7kNvgF74e-h&_nc_ht=scontent.fsgn5-5.fna&_nc_gid=AMROi6wX0JaFxqDkP6gHCYf&oh=00_AYBPBkddWBc_I9HOhW_y9Hj8ZXRhbhyDkqSK9X9oto3PNA&oe=66F820AA" alt="Flamingo 1" style="width:100%">
    </div>

    <div class="mySlides">
        <img src="https://scontent.fsgn5-10.fna.fbcdn.net/v/t39.30808-6/459943077_832852345661605_8993942302002378369_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=833d8c&_nc_ohc=AvY194xsmoAQ7kNvgH4tO45&_nc_ht=scontent.fsgn5-10.fna&oh=00_AYAf-kFZOjo3mIbtB2fmD1BhYHby0ZHM6-YbExTzg3-67A&oe=66F81E98" style="width:100%">
    </div>

    <div class="mySlides">
        <img src="https://scontent.fsgn5-10.fna.fbcdn.net/v/t39.30808-6/460266368_832852305661609_5459532278893249240_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=833d8c&_nc_ohc=CL9O5Ul_-4UQ7kNvgEanIxv&_nc_ht=scontent.fsgn5-10.fna&_nc_gid=A1i4o7mOIOcTMSUpHM5AKt5&oh=00_AYCIA14-omyhs2RI2Dfcb29MrS8LorJ97PXocHjq9YB0XQ&oe=66F837D5" style="width:100%">
    </div>

    <!-- Nút mũi tên -->
    <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
    <a class="next" onclick="plusSlides(1)">&#10095;</a>
</div>

<script>
    let slideIndex = 0;
    showSlides(slideIndex);

    function plusSlides(n) {
        showSlides(slideIndex += n);
    }

    function showSlides(n) {
        let slides = document.getElementsByClassName("mySlides");
        if (n >= slides.length) { slideIndex = 0 }
        if (n < 0) { slideIndex = slides.length - 1 }
        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        slides[slideIndex].style.display = "block";
    }

    // Tự động chuyển ảnh sau mỗi 3 giây
    setInterval(function() {
        plusSlides(1);
    }, 3000);
</script>

<style>
    .slideshow-container {
        max-width: 500px;
        position: relative;
        margin: auto;
    }

    .mySlides {
        display: none;
    }

    img {
        width: 100%;
        height: 100vh; /* Chiều cao chiếm 100% màn hình */
        object-fit: cover; /* Đảm bảo ảnh bao phủ toàn bộ không gian */
    }

    .prev, .next {
        cursor: pointer;
        position: absolute;
        top: 50%;
        width: auto;
        padding: 16px;
        margin-top: -22px;
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
</style>

"""

# Sử dụng Streamlit để hiển thị HTML/JS/CSS
st.components.v1.html(html_code, height=400)

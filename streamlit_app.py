import streamlit as st

# Title of the app
st.title(" A-Flamingo Club")

# Custom CSS to set the galaxy background with pink highlights
st.markdown(
    """
    <style>
    /* Set the background image to a galaxy with pink tones */
    body {
        background-image: url('https://images.unsplash.com/photo-1568223288053-3cf3f6e915f3?ixlib=rb-4.0.3&auto=format&fit=crop&w=1740&q=80');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }
    /* Add custom styling to the content box */
    .container {
        display: flex;
        align-items: center;
        margin-top: 50px;
    }
    /* Make the image circular and add a white border */
    .icon {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        margin-right: 20px;
        border: 3px solid white;
    }
    /* Set text font and size for the description */
    .description {
        font-size: 22px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the image and description in a container
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

# Call to action link
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

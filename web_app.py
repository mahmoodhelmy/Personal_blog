def webapp():
    import streamlit as st
    st.set_page_config(
        page_title="Nerdy Beardy Blog",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={'About': "# MY personal Blog"}

    )
    st.title("The Nerdy Beardy Blog")

    t1, t2, t3, t4, t5, t6 = st.tabs(['Home', 'Projects', 'Languages', 'Way of life', 'Hobbies', 'streamlit testing'])

    with t1:
        st.header("Welcome my personal page :)", divider=True)
        st.write("Hello Everyone and nice to see you here , you will find here on the home page a lot of "
                 "unorganized thoughts, it has been intended originally to be for my programming projects ,"
                 "Thanks to God it will have a lot of topics Like Religous ,politics, programming , linguistics"
                 ",and even hobbies and anime.")
        st.write("Enjoy your stay.")
        st.header("Latest Important thing:", divider=True)

        c1, c2 = st.columns([1, 1])
        with c1:
            try:
                st.image(
                    'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpeaceproject.com%2Fwp-content%2Fuploads%2FS521_FreePalestine.jpg&f=1&nofb=1&ipt=54363d8677a08adc85480431c9a9c385aea5eb3d285af018ed4814d949f223bc&ipo=images',
                    caption="Free Palestine ", width=400)
            except:
                st.write('Image file not found')

        with c2:
            st.header("")
            st.subheader("Freedom for Palestine \n Nothing to be said anymore")

    with t2:
        st.subheader("Power Point  "
                     ""
                     "\n ", divider=True)
        ct00, ct01, ct02, ct03, ct04 = st.columns([1, 1, 1, 1, 1])
        with ct00:
            gal = st.button('Galaxy project')
        with ct01:
            Story = st.button("Kids story")
        if gal:
            ct1, ct2 = st.columns([1, 1])
            with ct1:
                st.image("pages/MGP.png", width=300)
            with ct2:
                st.write("This is my Galaxy educational project for kids")
        elif Story:
            ct1, ct2 = st.columns([1, 1])

            with ct2:
                st.write("This Project is under construction")

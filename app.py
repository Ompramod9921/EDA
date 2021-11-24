import pandas as pd
import pandas_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
import sweetviz as sv

st.set_page_config(page_title='EDA with streamlit components',page_icon='👽')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
	content:'Made with ❤️ by om pramod'; 
	visibility: visible ;
}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.sidebar.success("Exploratory Data Analysis")

choice = st.sidebar.selectbox("Menu",["Pandas Profiling","Sweetviz"])

if choice == "Pandas Profiling" :
    st.title("Pandas Profiling")
    st.caption("Thanks to streamlit , I ❤️ streamlit")
    st.markdown("****")

    file = st.file_uploader("Upload An file",type=['csv'])

    st.markdown("****")
        
    if file is not None:
        df = pd.read_csv(file,encoding='unicode_escape')
        st.dataframe(df)
        if st.button("submit"):
            pr = df.profile_report()
            st_profile_report(pr)

elif choice == "Sweetviz" :
    st.title("Sweetviz Report")
    st.caption("Thanks to streamlit , I ❤️ streamlit")
    st.markdown("****")

    data_file = st.file_uploader("upload csv file",type=['csv'])

    st.markdown("****")

    if data_file is not None:
        df = pd.read_csv(data_file,encoding='unicode_escape')
        st.dataframe(df)
        if st.button("Generate sweetviz Report"):
            report = sv.analyze(df)
            report.show_html()


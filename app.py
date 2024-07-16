import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
from streamlit_option_menu import option_menu
#import plotly_express as px
from PIL import Image

st.set_page_config(page_title="NHL Dashboard", page_icon=":ice_hockey_stick_and_puck:", layout="wide", initial_sidebar_state="auto")

st.write('<style>div.block-container{padding-top:5rem;}</style>', unsafe_allow_html=True)
st.title("NHL Team Statistics Dashboard")

NHL_Logo=Image.open("NHL_Logo.png")

# Define function to load and display data
def load_and_display_data(file_path, image_path):
    try:
        df = pd.read_csv(file_path)
        st.dataframe(df, hide_index=True)
        with st.container():
            main, margin = st.columns((0.75, 0.25))
            with main:
                st.image(image_path)
        st.write(len(df))
    except FileNotFoundError:
        st.error("File not found. Please check the file path.")
    except Exception as e:
        st.error(f"An error occurred: {e}")


def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 20px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "linkedin": "https://img.icons8.com/ios-filled/100/000000/linkedin.png",
                "github": "https://img.icons8.com/ios-filled/100/000000/github--v2.png",
                "email": "https://img.icons8.com/ios-filled/100/000000/filled-message.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html

# def interactive_plot(dataframe):
#     x_axis_val=st.selectbox("Select X-Axis Value", options=df.columns)
#     y_axis_val=st.selectbox("Select Y-Axis Value", options=df.columns)

#     plot=px.scatter(dataframe, x=x_axis_val, y=y_axis_val)
#     st.plotly_chart(plot)

# Sidebar: If using streamlit_option_menu
with st.sidebar:
    with st.container():
        l, m, r = st.columns((1,3,1))
        with l:
            st.empty()
        with m:
            st.image(NHL_Logo,width=175)
        with r:
            st.empty()
    
    choose = option_menu(
                        "National Hockey League", 
                        ["Teams", "Standings"],
                         icons=['person fill', 'book half', ],
                         menu_icon="bar-chart-line-fill", 
                         default_index=0,
                         styles={
        "container": {"padding": "0!important", "background-color": "#44475a"},
        "icon": {"color": "#000000", "font-size": "20px"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#bd93f9", "color": "#000000"},
        "nav-link-selected": {"background-color": "#bd93f9", "color": "#000000"},
        "menu-title": {"color": "#000000", "font-size": "19px"}
    }
    )
  
    linkedin_url = "https://www.linkedin.com/in/nick-sofianakos/"
    github_url = "https://github.com/Nick3429"
    email_url = "mailto:nsofianakos@gmail.com"
    with st.container():
        l, m, r = st.columns((0.11,2,0.1))
        with l:
            st.empty()
        with m:
            st.markdown(
                social_icons(30, 30, LinkedIn=linkedin_url, GitHub=github_url,  Email=email_url),
                unsafe_allow_html=True)
        with r:
            st.empty()






if choose=="Teams":
     st.header("Teams")
     st.subheader("A Way to visualize the current status of your team in respect to the rest of the league")
     situation_options = ["All Strengths", "Even Strength", "5v5", "5v5 Score & Venue Adjusted", 
                        ]
     score_options = ["All Scores", "Tied", "Leading", "Trailing", "Within 1", "Up 1", "Down 1", 
                        ]
     with st.container():
         left, right = st.columns(2)
         with left:
             sit_selected = st.selectbox("Pick a situation", options = situation_options)
         with right:
             score_selected = st.selectbox("Pick a Score option", options = score_options)
     if sit_selected=="All Strengths" and score_selected== "All Scores":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/AllStrengthsAllScoresCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ASAS.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/AllStrengthsAllScoresCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ASAS.png")
       #      #st.dataframe(df_teamlogos,hide_index=True)
       #      #interactive_plot(df)
       #      st.write(len(df))
     if sit_selected=="All Strengths" and score_selected== "Tied":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/AllStrengthsTiedCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ASTied.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/AllStrengthsTiedCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ASTied.png")
       #      #interactive_plot(df)
       #      st.write(len(df))
     if sit_selected=="All Strengths" and score_selected== "Leading":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/AllStrengthsLeadingCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ASLeading.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/AllStrengthsLeadingCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ASLeading.png")
       #     # interactive_plot(df)
       #      st.write(len(df))
     if sit_selected=="All Strengths" and score_selected== "Trailing":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/AllStrengthsTrailingCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ASTrailing.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/AllStrengthsTrailingCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ASTrailing.png")
       #      #interactive_plot(df)
       #      st.write(len(df))
     if sit_selected=="All Strengths" and score_selected== "Within 1":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/AllStrengthsWithinOneCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ASW1.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/AllStrengthsWithinOneCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ASW1.png")
       #      #interactive_plot(df)
       #      st.write(len(df))
     if sit_selected=="All Strengths" and score_selected== "Up 1":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/AllStrengthsUpOneCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ASU1.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/AllStrengthsUpOneCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ASU1.png")
       #      #interactive_plot(df)
       #      st.write(len(df))
     if sit_selected=="All Strengths" and score_selected== "Down 1":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/AllStrengthsDownOneCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ASD1.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/AllStrengthsDownOneCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ASD1.png")
       #      #interactive_plot(df)
       #      st.write(len(df))
     if sit_selected=="Even Strength" and score_selected== "All Scores":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/EvenStrengthAllScoresCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_EVAS.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/EvenStrengthAllScoresCounts.csv")           
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_EVAS.png")
       #      #interactive_plot(df)
       #      st.write(len(df))      
     if sit_selected=="Even Strength" and score_selected== "Tied":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/EvenStrengthTiedCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_EVTied.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/EvenStrengthTiedCounts.csv")  
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_EVTied.png") 
       #      #interactive_plot(df)
       #      st.write(len(df))
     if sit_selected=="Even Strength" and score_selected== "Leading":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/EvenStrengthLeadingCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_EVLeading.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/EvenStrengthLeadingCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_EVLeading.png") 
       #      #interactive_plot(df)
       #      st.write(len(df)) 
     if sit_selected=="Even Strength" and score_selected== "Trailing":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/EvenStrengthTrailingCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_EVTrailing.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/EvenStrengthTrailingCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_EVTrailing.png") 
       #      #interactive_plot(df)
       #      st.write(len(df))   
     if sit_selected=="Even Strength" and score_selected== "Within 1":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/EvenStrengthWithinOneCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_EVW1.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/EvenStrengthWithinOneCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_EVW1.png") 
       #      #interactive_plot(df)
       #      st.write(len(df))
     if sit_selected=="Even Strength" and score_selected== "Up 1":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/EvenStrengthUpOneCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_EVU1.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/EvenStrengthUpOneCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_EVU1.png") 
       #      #interactive_plot(df)
       #      st.write(len(df))
     if sit_selected=="Even Strength" and score_selected== "Down 1":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/EvenStrengthDownOneCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_EVD1.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/EvenStrengthDownOneCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_EVD1.png") 
       #      #interactive_plot(df)
       #      st.write(len(df))
     if sit_selected=="5v5" and score_selected== "All Scores":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/5v5AllScoresCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_5v5AS.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/5v5AllScoresCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_5v5AS.png") 
       #      #interactive_plot(df)
       #      st.write(len(df))       
     if sit_selected=="5v5" and score_selected== "Tied":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/5v5TiedCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_5v5Tied.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/5v5TiedCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_5v5Tied.png") 
       #      #interactive_plot(df)
       #      st.write(len(df)) 
     if sit_selected=="5v5" and score_selected== "Leading":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/5v5LeadingCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_5v5Leading.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/5v5LeadingCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_5v5Leading.png") 
       #      #interactive_plot(df)
       #      st.write(len(df))  
     if sit_selected=="5v5" and score_selected== "Trailing":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/5v5TrailingCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_5v5Trailing.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/5v5TrailingCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_5v5Trailing.png") 
       #      #interactive_plot(df)
       #      st.write(len(df))  
     if sit_selected=="5v5" and score_selected== "Within 1":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/5v5WithinOneCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_5v5W1.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/5v5WithinOneCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_5v5W1.png") 
       #      #interactive_plot(df)
       #      st.write(len(df))  
     if sit_selected=="5v5" and score_selected== "Up 1":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/5v5UpOneCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_5v5U1.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/5v5UpOneCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_5v5U1.png") 
       #      #interactive_plot(df)
       #      st.write(len(df))
     if sit_selected=="5v5" and score_selected== "Down 1":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/5v5DownOneCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_5v5D1.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/5v5DownOneCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_5v5D1.png") 
       #      #interactive_plot(df)
       #      st.write(len(df))    
     if sit_selected=="5v5 Score & Venue Adjusted" and score_selected== "All Scores":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/Adj5v5AllScoresCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ADJ5v5AS.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/Adj5v5AllScoresCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ADJ5v5AS.png") 
       #      #interactive_plot(df)
       #      st.write(len(df))      
     if sit_selected=="5v5 Score & Venue Adjusted" and score_selected== "Tied":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/Adj5v5TiedCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ADJ5v5Tied.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/Adj5v5TiedCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ADJ5v5Tied.png") 
       #      #interactive_plot(df)
       #      st.write(len(df))
     if sit_selected=="5v5 Score & Venue Adjusted" and score_selected== "Leading":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/Adj5v5LeadingCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ADJ5v5Leading.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/Adj5v5LeadingCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ADJ5v5Leading.png") 
       #      #interactive_plot(df)
       #      st.write(len(df))
     if sit_selected=="5v5 Score & Venue Adjusted" and score_selected== "Trailing":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/Adj5v5TrailingCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ADJ5v5Trailing.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/Adj5v5TrailingCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ADJ5v5Trailing.png") 
       #      #interactive_plot(df)
       #      st.write(len(df))   
     if sit_selected=="5v5 Score & Venue Adjusted" and score_selected== "Within 1":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/Adj5v5WithinOneCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ADJ5v5W1.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/Adj5v5WithinOneCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ADJ5v5W1.png") 
       #      #interactive_plot(df)
       #      st.write(len(df)) 
     if sit_selected=="5v5 Score & Venue Adjusted" and score_selected== "Up 1":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/Adj5v5UpOneCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ADJ5v5U1.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/Adj5v5UpOneCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ADJ5v5U1.png") 
       #      #interactive_plot(df)
       #      st.write(len(df)) 
     if sit_selected=="5v5 Score & Venue Adjusted" and score_selected== "Down 1":
          load_and_display_data("https://raw.githubusercontent.com/Nick3429/NHLDashboard/main/NHL%20Dashboard%20Graphs/Adj5v5DownOneCounts.csv","C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ADJ5v5D1.png")
       #      df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/Adj5v5DownOneCounts.csv")
       #      st.dataframe(df,hide_index=True)
       #      with st.container():
       #        main,margin= st.columns((0.75,0.25))
       #        with main:
       #               st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ADJ5v5D1.png") 
       #      #interactive_plot(df)
       #      st.write(len(df))

if choose=="Standings":
     st.header("Standings")
     df=pd.read_csv("Standings.csv")
     st.dataframe(df, hide_index=True)

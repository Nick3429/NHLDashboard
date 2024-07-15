import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
from streamlit_option_menu import option_menu
import plotly_express as px

st.set_page_config(page_title="NHL Dashboard", page_icon=":ice_hockey_stick_and_puck:", layout="wide", initial_sidebar_state="auto")

st.write('<style>div.block-container{padding-top:5rem;}</style>', unsafe_allow_html=True)
st.title("NHL Team Statistics Dashboard")





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
            st.empty()
        with r:
            st.empty()
    
    choose = option_menu(
                        "National Hockey League", 
                        ["Teams", "Players", "Leaderboard", "Standings"],
                         icons=['person fill',  'person fill', 'tools', 'book half', ],
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
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/AllStrengthsAllScoresCounts.csv")
            st.dataframe(df,hide_index=True)
            st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ASAS.png")
            #st.dataframe(df_teamlogos,hide_index=True)
            #interactive_plot(df)
            st.write(len(df))
     if sit_selected=="All Strengths" and score_selected== "Tied":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/AllStrengthsTiedCounts.csv")
            st.dataframe(df,hide_index=True)
            st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ASTied.png")
            #interactive_plot(df)
            st.write(len(df))
     if sit_selected=="All Strengths" and score_selected== "Leading":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/AllStrengthsLeadingCounts.csv")
            st.dataframe(df,hide_index=True)
            st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ASLeading.png")
           # interactive_plot(df)
            st.write(len(df))
     if sit_selected=="All Strengths" and score_selected== "Trailing":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/AllStrengthsTrailingCounts.csv")
            st.dataframe(df,hide_index=True)
            st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ASTrailing.png")
            #interactive_plot(df)
            st.write(len(df))
     if sit_selected=="All Strengths" and score_selected== "Within 1":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/AllStrengthsWithinOneCounts.csv")
            st.dataframe(df,hide_index=True)
            st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ASW1.png")
            #interactive_plot(df)
            st.write(len(df))
     if sit_selected=="All Strengths" and score_selected== "Up 1":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/AllStrengthsUpOneCounts.csv")
            st.dataframe(df,hide_index=True)
            st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ASU1.png")
            #interactive_plot(df)
            st.write(len(df))
     if sit_selected=="All Strengths" and score_selected== "Down 1":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/AllStrengthsDownOneCounts.csv")
            st.dataframe(df,hide_index=True)
            st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_ASD1.png")
            #interactive_plot(df)
            st.write(len(df))
     if sit_selected=="Even Strength" and score_selected== "All Scores":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/EvenStrengthAllScoresCounts.csv")           
            st.dataframe(df,hide_index=True)
            st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_EVAS.png")
            #interactive_plot(df)
            st.write(len(df))      
     if sit_selected=="Even Strength" and score_selected== "Tied":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/EvenStrengthTiedCounts.csv")  
            st.dataframe(df,hide_index=True)
            st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_EVTied.png") 
            #interactive_plot(df)
            st.write(len(df))
     if sit_selected=="Even Strength" and score_selected== "Leading":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/EvenStrengthLeadingCounts.csv")
            st.dataframe(df,hide_index=True)
            st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_EVLeading.png") 
            #interactive_plot(df)
            st.write(len(df)) 
     if sit_selected=="Even Strength" and score_selected== "Trailing":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/EvenStrengthTrailingCounts.csv")
            st.dataframe(df,hide_index=True)
            st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_EVTrailing.png") 
            #interactive_plot(df)
            st.write(len(df))   
     if sit_selected=="Even Strength" and score_selected== "Within 1":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/EvenStrengthWithinOneCounts.csv")
            st.dataframe(df,hide_index=True)
            st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_EVW1.png") 
            #interactive_plot(df)
            st.write(len(df))
     if sit_selected=="Even Strength" and score_selected== "Up 1":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/EvenStrengthUpOneCounts.csv")
            st.dataframe(df,hide_index=True)
            st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_EVU1.png") 
            #interactive_plot(df)
            st.write(len(df))
     if sit_selected=="Even Strength" and score_selected== "Down 1":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/EvenStrengthDownOneCounts.csv")
            st.dataframe(df,hide_index=True)
            st.image("C:/NHL Streamlit Dashboard/NHLDashboard/NHL Dashboard Graphs/nhl_2023_2024_EVD1.png") 
            #interactive_plot(df)
            st.write(len(df))
     if sit_selected=="5v5" and score_selected== "All Scores":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/5v5AllScoresCounts.csv")
            st.dataframe(df,hide_index=True)
            #interactive_plot(df)
            st.write(len(df))       
     if sit_selected=="5v5" and score_selected== "Tied":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/5v5TiedCounts.csv")
            st.dataframe(df,hide_index=True)
            #interactive_plot(df)
            st.write(len(df)) 
     if sit_selected=="5v5" and score_selected== "Leading":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/5v5LeadingCounts.csv")
            st.dataframe(df,hide_index=True)
            #interactive_plot(df)
            st.write(len(df))  
     if sit_selected=="5v5" and score_selected== "Trailing":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/5v5TrailingCounts.csv")
            st.dataframe(df,hide_index=True)
            #interactive_plot(df)
            st.write(len(df))  
     if sit_selected=="5v5" and score_selected== "Within 1":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/5v5WithinOneCounts.csv")
            st.dataframe(df,hide_index=True)
            #interactive_plot(df)
            st.write(len(df))  
     if sit_selected=="5v5" and score_selected== "Up 1":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/5v5UpOneCounts.csv")
            st.dataframe(df,hide_index=True)
            #interactive_plot(df)
            st.write(len(df))
     if sit_selected=="5v5" and score_selected== "Down 1":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/5v5DownOneCounts.csv")
            st.dataframe(df,hide_index=True)
            #interactive_plot(df)
            st.write(len(df))    
     if sit_selected=="5v5 Score & Venue Adjusted" and score_selected== "All Scores":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/Adj5v5AllScoresCounts.csv")
            st.dataframe(df,hide_index=True)
            #interactive_plot(df)
            st.write(len(df))      
     if sit_selected=="5v5 Score & Venue Adjusted" and score_selected== "Tied":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/Adj5v5TiedCounts.csv")
            st.dataframe(df,hide_index=True)
            #interactive_plot(df)
            st.write(len(df))
     if sit_selected=="5v5 Score & Venue Adjusted" and score_selected== "Leading":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/Adj5v5LeadingCounts.csv")
            st.dataframe(df,hide_index=True)
            #interactive_plot(df)
            st.write(len(df))
     if sit_selected=="5v5 Score & Venue Adjusted" and score_selected== "Trailing":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/Adj5v5TrailingCounts.csv")
            st.dataframe(df,hide_index=True)
            #interactive_plot(df)
            st.write(len(df))   
     if sit_selected=="5v5 Score & Venue Adjusted" and score_selected== "Within 1":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/Adj5v5WithinOneCounts.csv")
            st.dataframe(df,hide_index=True)
            #interactive_plot(df)
            st.write(len(df)) 
     if sit_selected=="5v5 Score & Venue Adjusted" and score_selected== "Up 1":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/Adj5v5UpOneCounts.csv")
            st.dataframe(df,hide_index=True)
            #interactive_plot(df)
            st.write(len(df)) 
     if sit_selected=="5v5 Score & Venue Adjusted" and score_selected== "Down 1":
            df=pd.read_csv("C:/NHL Streamlit Dashboard/Regular Season 2023-24 Season CSV's/Adj5v5DownOneCounts.csv")
            st.dataframe(df,hide_index=True)
            #interactive_plot(df)
            st.write(len(df))
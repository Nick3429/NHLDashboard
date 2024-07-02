import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from streamlit_option_menu import option_menu

st.set_page_config(page_title="NHL Dashboard", page_icon=":ice_hockey_stick_and_puck:", layout="wide", initial_sidebar_state="auto")

st.write('<style>div.block-container{padding-top:5rem;}</style>', unsafe_allow_html=True)
st.title("NHL Team Statistics Dashboard")
st.subheader("A Way to visualize the current status of your team in respect to the rest of the league")


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
     situation_options = ["All Strengths", "Even Strength", "5v5", "5v5 Score & Venue Adjusted", "Power Play","5 on 4 PP", "Penalty Kill", "4 on 5 PK", "3 on 3", "With Empty Net", "Against Empty Net", 
                        ]
     score_options = ["All Scores", "Tied", "Leading", "Trailing", "Within 1", "Up 1", "Down 1", "3 on 3", 
                        ]
     type_options = ["Counts", "Rates"]
     with st.container():
         left, middle, right = st.columns(3)
         with left:
             sit_selected = st.selectbox("Pick a situation", options = situation_options)
         with middle:
             score_selected = st.selectbox("Pick a Score option", options = score_options)
         with right:
             sit_selected = st.selectbox("Pick a stat type", options = type_options)
             

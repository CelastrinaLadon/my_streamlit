import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Profile data
PROFILE_IMAGE_URL = "https://media.licdn.com/dms/image/v2/D5603AQGbcev-HCcG-g/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1731941595917?e=1743638400&v=beta&t=pe_D_gahkyunXEBnpXSC8RTHbC3oCQL-i_Y0lYjooLY"
NAME = "Thotsaphon Sirikutta"
TITLE = "Full-Stack Data Dude"
EMAIL = "t.sirikutta@gmail.com"
LOCATION = "Bangkok, Thailand"
SUMMARY = (
'''Results-driven Development Manager with a foundation in economics and a strong focus on leveraging data engineering, analytics, and full-stack development to drive business growth. Proven expertise in cloud technologies, DevOps, and system architecture design, with a track record of leading teams to build scalable, data-driven platforms. Adept at aligning technical initiatives with strategic goals, optimizing business processes, and implementing industry best practices. Skilled in market analysis, economic forecasting, and distribution strategy optimization.'''
)

# Streamlit App
st.set_page_config(page_title="Thotsaphon Sirikutta Profile", page_icon=":wave:", layout="centered")
col1, col2 = st.columns([0.8, 0.2])

with col2:
    # Profile Image and Header
    if PROFILE_IMAGE_URL:
        response = requests.get(PROFILE_IMAGE_URL)
        image = Image.open(BytesIO(response.content))
        st.image(image, width=20, use_container_width=True)

with col1:
    st.title(NAME)
    st.subheader(TITLE)
    col_t1, col_t2 = st.columns([0.5, 0.5])
    with col_t1:
        st.write(f":link: [LinkedIn](https://www.linkedin.com/in/thotsaphon-sirikutta-82511a154/)")
        st.write(f":email: [EMAIL](mailto:{EMAIL})")
        st.write(f":round_pushpin: {LOCATION}")
    with col_t2:
        st.write(f":link: [Download CV](https://www.linkedin.com/in/thotsaphon-sirikutta-82511a154/)")
    
    

# Summary Section
st.divider()

con_1 =  st.container(border=False)
with con_1:
    st.header("About Me")
    st.write(SUMMARY)

#     # Skills Section
#     st.markdown("---")
#     st.header("Key Skills")
#     st.write(
#         "- Leadership and team management\n"
#         "- Data engineering and development\n"
#         "- Cloud technologies and DevOps\n"
#         "- Programming and software development\n"
#         "- Data analytics and visualization\n"
#         "- Standards and compliance\n"
#         "- Strategic and analytical thinking"
#     )

lst_exp = [
    {
        'roles':'Development Manager',
        'company':'MEDCury Co., Ltd.',
        'start':'Nov 2021',
        'end':'Present',
        'location': 'Bangkok, Thailand',
        'details':[
            "- Lead a team of 10 engineers to manage the flagship data platform, MEDConnext, optimizing cloud infrastructure and streamlining operations across all products. \n"
            "- Implemented real-time streaming data pipelines from Centrix (HIS) and standardized dashboards for data-driven decision-making.\n"
            "- Designed and implemented a data quality detection system to proactively identify pipeline risks, ensuring seamless operations.\n"
            "- Standardized logging protocols and monitoring tools (Prometheus, Grafana) for comprehensive environment visibility.\n"
            "- Championed CI/CD pipelines with quality gates, supporting Test-Driven Development (TDD) practices across teams.\n"
        ]
    },
    {
        'roles':'Assistant Manager Data Engineer',
        'company':'Intage (Thailand) Co., Ltd.',
        'start':'Apr 2021',
        'end':'Nov 2021',
        'location': 'Bangkok, Thailand',
        'details':[
            "- Designed advanced analytics solutions incorporating predictive models and machine learning techniques. \n"
            "- Improved internal controls by analyzing complex data and identifying trends, risks, and anomalies.  \n"
            "- Developed and maintained data analytics protocols and documentation to ensure process consistency. \n"
        ]
    },
    {
        'roles':'Senior Data Engineer',
        'company':'Intage (Thailand) Co., Ltd.',
        'start':'Jan 2019',
        'end':'Mar 2021',
        'location': 'Bangkok, Thailand',
        'details':[
            "- Led data engineering and backend teams to automate processes and enhance system efficiency. \n"
            "- Introduced Apache Airflow, transforming legacy automation workflows for ETL pipelines. \n"
            "- Built scalable APIs for calculating scores based on complex market research formulas. \n"
        ]
    },
]

st.divider()
st.header("Professional Experience")
for data in lst_exp:
    second_line = f"{data.get('company', '')} – {data.get('location', '')} | {data.get('start', '')} – {data.get('end', '')}"
    with st.container(border=True):
        st.subheader(data['roles'])
        st.write(second_line)
        st.write(*data['details'])
        st.write('\n')

# Footer
st.divider()
st.markdown(
    "<small>Built with ❤️ using [Streamlit](https://streamlit.io)</small>",
    unsafe_allow_html=True
)

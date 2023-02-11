from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
profile_pic = current_dir / "assets" / "profile-pic.jpeg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Portfolio | Sara Essahli"
PAGE_ICON = "👩‍💻"
NAME = "Sara Essahli"
DESCRIPTION = """
Currently a Student looking forward to gaining more expertise.
"""
EMAIL = "sara.essahli09@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "👾 First Project": "https://github.com/Asurite/First-project",
    "👾 Streamlit Portfolio Project": "https://github.com/Asurite/Streamlit-Project",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS AND PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write(EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- QUALIFICATIONS ---
st.write('\n')
st.subheader("Qualifications")
st.write(
    """
- /Strong hands-on experience and understanding of prevalent modern technologies with fast adaptation.
- /Excellent team player with a strong sense of initiative when it comes to tasks.
- /Maintains work balance while remaining organized to completing tasks and projects on time.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 🟩 HTML, CSS, JavaScript, Python 
- 🟩 Adobe Photoshop, Adobe Illustrator
- 🟩 Self-taught Photographer and filmmaker
"""
)
 


# --- Projects ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")



    



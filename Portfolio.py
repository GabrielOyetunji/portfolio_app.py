import streamlit as st
from PIL import Image

# --- Page setup ---
st.set_page_config(page_title="Gabriel Oyetunji | Portfolio", layout="wide")

# --- Load profile image ---
profile_image = Image.open("images/profile.jpg")

# --- Custom CSS ---
st.markdown("""
    <style>
    body {
        background-color: #000000;
        color: #E0E0E0;
        font-family: 'Segoe UI', sans-serif;
    }
    .main {
        padding: 0rem 3rem;
    }
    .rounded-image {
        border-radius: 50%;
    }
    .section-title {
        font-size: 28px;
        font-weight: 800;
        margin-top: 3rem;
        margin-bottom: 1rem;
        color: #FFFFFF;
    }
    .project-card {
        background-color: #111111;
        padding: 1.5rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0px 0px 10px rgba(255,255,255,0.05);
    }
    .project-title {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #ffffff;
    }
    .project-description {
        font-size: 16px;
        line-height: 1.6;
    }
    .tool-tag {
        background-color: #3b82f6;
        color: white;
        padding: 5px 10px;
        border-radius: 10px;
        margin-right: 6px;
        font-size: 13px;
        display: inline-block;
    }
    .contact-link {
        color: #60a5fa;
        text-decoration: none;
        font-weight: bold;
    }
    hr {
        border: none;
        height: 1px;
        background-color: #333;
        margin: 3rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
col1, col2 = st.columns([1, 4])
with col1:
    st.image(profile_image, width=140)
with col2:
    st.markdown("## **Gabriel Oyetunji**")
    st.markdown("#### Data Analyst | Data Scientist")
    st.markdown("📊 *Turning raw data into sharp insights.*")

st.markdown("<hr>", unsafe_allow_html=True)

# --- About Me ---
with st.expander("🧾 About Me", expanded=False):
    st.write("""
    I'm a Data Analyst & Data Scientist focused on clarity, efficiency, and impact.  
    I use Python, SQL, Power BI, and Excel to clean data, build automated workflows,
    and design dashboards that guide better decisions — not just prettier reports.
    """)

# --- Certifications ---
with st.expander("📑 Certifications", expanded=False):
    st.markdown("- ✅ [Data Analyst – DataCamp (April 2025)](https://www.datacamp.com/certificate/DA0022509689479)")

# --- Project Renderer ---
def render_project(project):
    with st.container():
        st.markdown("<div class='project-card'>", unsafe_allow_html=True)
        st.markdown(f"<div class='project-title'>{project['title']}</div>", unsafe_allow_html=True)
        
        try:
            img = Image.open(project["image"])
            st.image(img, use_container_width=True)
        except:
            st.warning(f"⚠️ Could not load image: {project['image']}")

        st.markdown(" ".join([f"<span class='tool-tag'>{tool}</span>" for tool in project["tools"]]), unsafe_allow_html=True)
        st.markdown(f"<div class='project-description'>{project['project_excerpt']}</div>", unsafe_allow_html=True)
        st.write(project['full_description'])

        cols = st.columns([1, 1])
        with cols[0]:
            if project["github_url"]:
                st.markdown(f"[🔗 GitHub]({project['github_url']})", unsafe_allow_html=True)
        with cols[1]:
            if project["demo_url"]:
                st.markdown(f"[▶️ Watch Demo]({project['demo_url']})", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

# --- Projects ---
st.markdown("### 🗂️ Projects", unsafe_allow_html=True)

projects = [
    {
        "title": "NovaTech Sales Dashboard",
        "tools": ["Excel"],
        "project_excerpt": "Recorded walkthrough showing slicers, KPIs, and regional sales insights.",
        "full_description": """This interactive Excel dashboard uses slicers, charts, and conditional formatting to show sales vs target performance across regions.

NovaTech Distributors needed a clear view of its 2025 sales performance to inform decisions. Using Excel, I built:
- KPI cards for total sales and target variance
- Monthly and regional breakdowns
- Top/bottom product rankings
- Segmentation by customer type

The dashboard revealed that only 47% of targets were met, highlighting regional underperformance and guiding strategy refinement.
""",
        "image": "images/nova.png",
        "demo_url": "https://www.loom.com/share/19461c0fd60b408a80d9675aa1ff0de2?sid=417d9f22-4104-4c15-ad32-c6a63c0a2911",
        "github_url": ""
    },
    {
        "title": "Interactive UV-Vis Spectra Trimmer with Python & Streamlit",
        "tools": ["Python", "Streamlit", "Pandas"],
        "project_excerpt": "Built for a PhD researcher working on UV-Vis spectrophotometry data. Handles large, messy CSV files and enables interactive trimming and export.",
        "full_description": """🧹 **Data Cleaning Scripts**: Automates header removal, type conversion, and wavelength filtering.

📁 **Batch Processing**: Script processes 240+ samples and exports cleaned CSV files.

🌐 **Streamlit App**: Users can upload raw CSVs, preview spectra, adjust wavelength range, and export — no coding needed.""",
        "image": "images/uv.app.png",
        "demo_url": "https://www.loom.com/share/e372774ab4f74a1db40446944c25fa72?sid=3b9c31a3-ab27-469c-ae60-fe394d46f401",
        "github_url": "https://github.com/GabrielOyetunji/uvvis-spectrophotometer-app"
    }
]

for project in projects:
    render_project(project)

# --- Contact ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("### 📬 Contact Me")
st.markdown("""
- 📧 Email: [gabrieloyetunji25@gmail.com](mailto:gabrieloyetunji25@gmail.com)
- 🧠 GitHub: [github.com/gabrieloyetunji](https://github.com/gabrieloyetunji)
- 💼 LinkedIn: [linkedin.com/in/gabriel-oyetunji-a7aa9513b](https://www.linkedin.com/in/gabriel-oyetunji-a7aa9513b)
""", unsafe_allow_html=True)

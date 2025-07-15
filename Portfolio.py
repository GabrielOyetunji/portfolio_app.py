import streamlit as st
from PIL import Image

# Page setup
st.set_page_config(page_title="Gabriel Oyetunji | Portfolio", layout="wide")

# Load profile image
profile_image = Image.open("images/profile.jpg")

# Custom CSS (inspired by Reshama, with dark mode + modern font)
st.markdown("""
    <style>
    body {
        background-color: #000000;
        color: #E0E0E0;
        font-family: 'Segoe UI', sans-serif;
    }
    .main {
        background-color: #000000;
        padding: 0rem 3rem;
    }
    .rounded-image {
        border-radius: 50%;
    }
    .section-title {
        font-size: 26px;
        font-weight: 700;
        margin-top: 40px;
        color: #FFFFFF;
    }
    .project-title {
        font-size: 22px;
        font-weight: 600;
        color: #ffffff;
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
    hr {
        border: none;
        height: 1px;
        background-color: #222;
        margin: 3rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
col1, col2 = st.columns([1, 4])
with col1:
    st.image(profile_image, width=140)
with col2:
    st.markdown("## **Gabriel Oyetunji**")
    st.markdown("#### Data Analyst | Data Scientist")
    st.markdown("📊 *Turning raw data into sharp insights.*")

st.markdown("<hr>", unsafe_allow_html=True)

# --- About Me
with st.expander("🧾 About Me", expanded=False):
    st.write("""
    I'm a Data Analyst & Data Scientist focused on clarity, efficiency, and impact.  
    I use Python, SQL, Power BI, and Excel to clean data, build automated workflows,
    and design dashboards that guide better decisions — not just prettier reports.
    """)

# --- Certifications
with st.expander("📑 Certifications", expanded=False):
    certifications = [
        "✅ [Data Analyst – DataCamp (April 2025)](https://www.datacamp.com/certificate/DA0022509689479)"
    ]
    for cert in certifications:
        st.markdown(f"- {cert}", unsafe_allow_html=True)

# --- Projects Section
with st.expander("🗂️ Projects", expanded=True):
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
            "project_excerpt": "This project was developed for a PhD researcher working on UV-Vis spectrophotometry data. The core challenge was handling large, messy CSV files generated from the CARY 50 spectrophotometer — which contained hundreds of paired columns for wavelength and absorbance readings.",
            "full_description": """🧹 Data Cleaning Scripts: Python scripts that automate the removal of redundant headers, convert string values to numeric types, and filter the wavelength range (typically between 400–600 nm).

📁 Batch Processing: A script that processes all 240 samples at once and exports a cleaned, trimmed CSV file for downstream analysis.

🌐 Streamlit Web App: An interactive app allowing users to upload their raw CSV files, preview a sample spectrum, adjust wavelength range with sliders, and export the trimmed dataset — no coding required.""",
            "image": "images/project2.png",
            "demo_url": "https://www.loom.com/share/e372774ab4f74a1db40446944c25fa72?sid=3b9c31a3-ab27-469c-ae60-fe394d46f401",
            "github_url": "https://github.com/GabrielOyetunji/uvvis-spectrophotometer-app"
        }
    ]

    for project in projects:
        with st.expander(project["title"], expanded=False):
            try:
                img = Image.open(project["image"])
                st.image(img, use_container_width=True)
            except FileNotFoundError:
                st.warning(f"⚠️ Could not load image: {project['image']}")

            st.markdown(f"<p>{project['project_excerpt']}</p>", unsafe_allow_html=True)
            st.markdown(" ".join([f"<span class='tool-tag'>{tool}</span>" for tool in project["tools"]]), unsafe_allow_html=True)
            st.write(project["full_description"])

            if project["github_url"]:
                st.markdown(f"[🔗 GitHub]({project['github_url']})", unsafe_allow_html=True)
            if project["demo_url"]:
                st.markdown(f"[▶️ Watch Demo]({project['demo_url']})", unsafe_allow_html=True)

# --- Contact Section
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("### 📬 Contact Me")
st.markdown("- 📧 Email: [gabrieloyetunji25@gmail.com](mailto:gabrieloyetunji25@gmail.com)")
st.markdown("- 🧠 GitHub: [github.com/gabrieloyetunji](https://github.com/gabrieloyetunji)")
st.markdown("- 💼 LinkedIn: [linkedin.com/in/gabrieloyetunji](https://linkedin.com/in/gabrieloyetunji)")

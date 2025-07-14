import streamlit as st
from PIL import Image

# Setup page
st.set_page_config(page_title="Gabriel Oyetunji | Portfolio", layout="centered")

# Load profile image
profile_image = Image.open("images/profile.jpg")

# Custom dark theme
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    .main {
        background-color: #0e1117;
    }
    .project-card {
        background-color: #1c1e24;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    .project-title {
        font-size: 24px;
        font-weight: bold;
        color: #facc15;
    }
    .tool-tag {
        background-color: #374151;
        color: white;
        padding: 4px 8px;
        border-radius: 8px;
        margin-right: 5px;
        font-size: 13px;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.image(profile_image, width=120)
st.title("Gabriel Oyetunji")
st.subheader("Data Analyst | Power BI | Python | SQL")
st.markdown("📊 *Turning raw data into sharp insights.*")

# About Me
st.markdown("### 🧾 About Me")
st.write("""
Data Analyst & Data Scientist focused on clarity, efficiency, and impact. 
I use Python, SQL, Power BI, and Excel to clean data, build automated workflows,
and design dashboards that guide better decisions — not just prettier reports.
""")

# Certifications
st.markdown("### 📑 Certifications")
certifications = [
    "✅ Data Analyst – DataCamp (April 2025)"
]
for cert in certifications:
    st.markdown(f"- {cert}")

# Projects
st.markdown("### 🗂️ Projects")

projects = [
    {
        "title": "NovaTech Sales Dashboard",
        "description": "Excel dashboard tracking sales vs targets.",
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
        "title": "F1 Podium Prediction (2023)",
        "description": "Machine learning model predicting Top 3 drivers using logistic regression.",
        "tools": ["Python", "Scikit-learn", "Pandas"],
        "project_excerpt": "Built a predictive model for podium finishes based on driver/race features using logistic regression.",
        "full_description": "Trained on 2023 F1 data to classify if a driver will finish in the top 3. Features included qualifying position, constructor, race circuit, weather, and driver stats.",
        "image": "images/project2.png",
        "demo_url": "",
        "github_url": "https://github.com/gabrieloyetunji/f1-podium-predictor"
    }
]

# Display project cards
for project in projects:
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown(f"<div class='project-title'>{project['title']}</div>", unsafe_allow_html=True)
    st.markdown(f"<p>{project['project_excerpt']}</p>", unsafe_allow_html=True)

    # Expand full description
    with st.expander("📘 Read More"):
        st.write(project["full_description"])

    # Tags
    st.markdown(" ".join([f"<span class='tool-tag'>{tool}</span>" for tool in project["tools"]]), unsafe_allow_html=True)

    # Project image
    try:
        image = Image.open(project["image"])
        st.image(image, use_container_width=True)
    except FileNotFoundError:
        st.warning(f"⚠️ Could not load image: {project['image']}")

    # Links
    if project["github_url"]:
        st.markdown(f"[🔗 GitHub]({project['github_url']})", unsafe_allow_html=True)
    if project["demo_url"]:
        st.markdown(f"[▶️ Watch Dashboard Demo]({project['demo_url']})", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# Contact
st.markdown("### 📬 Contact Me")
st.markdown("- 📧 Email: [gabrieloyetunji25@gmail.com](mailto:gabrieloyetunji25@gmail.com)")
st.markdown("- 🧠 GitHub: [github.com/gabrieloyetunji](https://github.com/gabrieloyetunji)")
st.markdown("- 💼 LinkedIn: [linkedin.com/in/gabrieloyetunji](https://linkedin.com/in/gabrieloyetunji)")

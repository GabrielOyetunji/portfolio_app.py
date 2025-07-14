import streamlit as st
from PIL import Image

# -------------------------------
# ⬆️ Load your images (Profile + Project Screenshots)
# -------------------------------
profile_image = Image.open("images/profile.jpg")
st.set_page_config(page_title="Gabriel Oyetunji | Portfolio", layout="centered")

# -------------------------------
# 🎨 Custom Dark Theme CSS
# -------------------------------
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

# -------------------------------
# 🙋 Your Name and Info
# -------------------------------
st.image(profile_image, width=120)
st.title("Gabriel Oyetunji")
st.subheader("Data Analyst | Power BI | Python | SQL")
st.markdown("📊 *Turning raw data into sharp insights.*")

# -------------------------------
# 🧑‍💼 About Me
# -------------------------------
about_me = """
Data Analyst & Data Scientist focused on clarity, efficiency, and impact. 
I use Python, SQL, Power BI, and Excel to clean data, build automated workflows,
and design dashboards that guide better decisions — not just prettier reports.
"""
st.markdown("### 🧾 About Me")
st.write(about_me)

# -------------------------------
# 📜 Certifications
# -------------------------------
certifications = [
    "✅ Data Analyst – DataCamp (April 2025)"
]

st.markdown("### 📑 Certifications")
for cert in certifications:
    st.markdown(f"- {cert}")

# -------------------------------
# 📁 Projects Section
# -------------------------------
st.markdown("### 🗂️ Projects")

projects = [
    {
        "title": "NovaTech Regional Sales Dashboard",
        "description": "Interactive Excel dashboard tracking monthly sales vs targets across four key regions.",
        "tools": ["Excel"],
        "project_excerpt": "Created an Excel dashboard analyzing 2025 sales vs targets across four regions, highlighting performance gaps and key insights for leadership.",
        "full_description": """NovaTech Distributors, a growing Canadian tech wholesaler, needed a clear view of its 2025 sales performance to inform strategic decisions.

This project involved analyzing actual vs. target sales across four regions, identifying revenue leaders and laggards among products, and segmenting customers by region and type.

Using Excel, I designed a clean, interactive dashboard that:
- Highlights key performance indicators (KPIs) like total sales, variance, and % target met
- Visualizes monthly trends and regional performance fluctuations
- Ranks top and bottom products by revenue
- Segments customers into Retail, Online, and Wholesale categories

The dashboard revealed that only 47% of targets were met, signaling critical gaps in certain regions and product lines. These insights support leadership in refining their sales strategies and resource allocation.
""",
        "image": "images/nova.png"
    },
    {
        "title": "F1 Podium Prediction (2023)",
        "description": "Machine learning model predicting Top 3 drivers using logistic regression.",
        "tools": ["Python", "Scikit-learn", "Pandas"],
        "project_excerpt": "Built a predictive model for podium finishes based on driver/race features using logistic regression.",
        "full_description": "Trained on 2023 F1 data to classify if a driver will finish in the top 3. Features included qualifying position, constructor, race circuit, weather, and driver stats.",
        "image": "images/project2.png",
        "github_url": "https://github.com/gabrieloyetunji/f1-podium-predictor",
        "demo_url": ""
    }
]

# -------------------------------
# 💼 Render Each Project
# -------------------------------
for project in projects:
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown(f"<div class='project-title'>{project['title']}</div>", unsafe_allow_html=True)

    # Project excerpt
    if "project_excerpt" in project:
        st.markdown(f"<p>{project['project_excerpt']}</p>", unsafe_allow_html=True)

    # Full description inside expander
    if "full_description" in project:
        with st.expander("📘 Read More"):
            st.markdown(project["full_description"])

    # Tool tags
    tool_tags = " ".join([f"<span class='tool-tag'>{tool}</span>" for tool in project["tools"]])
    st.markdown(tool_tags, unsafe_allow_html=True)

    # Project image
    try:
        image = Image.open(project["image"])
        st.image(image, use_container_width=True)
    except FileNotFoundError:
        st.warning(f"⚠️ Could not load image: {project['image']}")

    # GitHub & Demo links
    if project.get("github_url"):
        if project["github_url"]:
            st.markdown(f"[🔗 GitHub]({project['github_url']})", unsafe_allow_html=True)
    if project.get("demo_url"):
        if project["demo_url"]:
            st.markdown(f"[🌐 Live Demo]({project['demo_url']})", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------
# 📬 Contact Section
# -------------------------------
st.markdown("### 📬 Contact Me")
st.markdown("- 📧 Email: [gabrieloyetunji25@gmail.com](mailto:gabrieloyetunji25@gmail.com)")
st.markdown("- 🧠 GitHub: [github.com/gabrieloyetunji](https://github.com/gabrieloyetunji)")
st.markdown("- 💼 LinkedIn: [linkedin.com/in/gabrieloyetunji](https://linkedin.com/in/gabrieloyetunji)")

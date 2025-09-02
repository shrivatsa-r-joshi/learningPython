# app.py
# High‑fidelity Streamlit website in a single file
# Run with: streamlit run app.py

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime, timedelta

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Hi‑Fi Streamlit Site",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------
# Utilities & State
# ----------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "dark"  # "light" or "dark"

if "notifications" not in st.session_state:
    st.session_state.notifications = [
        {"title": "Welcome!", "time": "Just now", "body": "Explore the tabs and upload data."},
        {"title": "Tip", "time": "1 min", "body": "Toggle theme from the header."},
    ]


def set_theme(mode: str):
    st.session_state.theme = mode


# ----------------------------
# Global Styles (CSS)
# ----------------------------
common_css = """
<style>
:root {
  --bg: #0b0c10;
  --panel: #111218;
  --panel-2: #171825;
  --text: #e6e6e6;
  --muted: #a3a3a3;
  --brand: #7c3aed; /* violet-600 */
  --brand-2: #22c55e; /* green-500 */
  --ring: rgba(124, 58, 237, 0.5);
  --card-radius: 18px;
  --shadow: 0 6px 28px rgba(0,0,0,.35);
}

.light {
  --bg: #fafafa;
  --panel: #ffffff;
  --panel-2: #f4f4f5;
  --text: #0f172a;
  --muted: #334155;
  --brand: #7c3aed;
  --brand-2: #16a34a;
  --ring: rgba(124, 58, 237, .35);
  --card-radius: 18px;
  --shadow: 0 10px 28px rgba(2,6,23,.08);
}

/* Apply theme to the main block */
html, body, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stToolbar"] {
  background: var(--bg) !important;
}

* { font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Inter, Helvetica, Arial, Noto Sans, "Apple Color Emoji", "Segoe UI Emoji"; }

/* Header bar */
.header {
  display:flex;align-items:center;justify-content:space-between;gap:1rem;
  padding: 14px 22px;position:sticky;top:0;z-index:999;
  background: linear-gradient(180deg, rgba(0,0,0,0.35), rgba(0,0,0,0)) , var(--bg);
  margin-bottom: 4px;border-bottom: 1px solid rgba(255,255,255,.05);
}
.brand {
  display:flex;align-items:center;gap:.75rem;color:var(--text);
}
.brand .logo {width:36px;height:36px;border-radius:12px;background:linear-gradient(135deg,var(--brand),var(--brand-2));box-shadow: var(--shadow);} 
.brand .title {font-weight:800;font-size:1.15rem;letter-spacing:.2px}

/* Buttons */
.btn {
  border:1px solid transparent;border-radius:14px;padding:10px 14px;cursor:pointer;font-weight:600;
  background:var(--panel);
  color:var(--text);
  transition:.18s ease all;box-shadow: var(--shadow);
}
.btn:hover { transform: translateY(-1px); border-color: var(--ring); box-shadow:0 12px 30px rgba(124,58,237,.18); }
.btn-primary { background: linear-gradient(135deg, var(--brand), var(--brand-2)); color:white; }

/* Cards */
.card { background:var(--panel); border:1px solid rgba(255,255,255,.06); border-radius: var(--card-radius); padding:18px; box-shadow: var(--shadow); }
.card h3 { margin:0 0 6px 0; }
.card .muted { color: var(--muted); font-size:.9rem; }

/* Metric grid */
.metrics { display:grid;grid-template-columns:repeat(4, minmax(0,1fr)); gap:16px; }
.metric { background:var(--panel-2); border:1px solid rgba(255,255,255,.06); border-radius:16px; padding:16px; }
.metric .label { color:var(--muted); font-size:.85rem; }
.metric .value { font-size:1.6rem; font-weight:800; }

/* Tabs tweak */
[data-baseweb="tab-list"] { border-bottom: 1px dashed rgba(255,255,255,.08) !important; }

/* Tables */
tbody tr:hover { background: rgba(124,58,237,.06) }

/* Pills */
.pill { display:inline-flex; gap:.35rem; align-items:center; padding:6px 10px; border-radius:16px; background:rgba(124,58,237,.15); color:#fff; font-weight:700; font-size:.8rem }

/* Footer */
.footer { margin-top:40px; padding: 20px; opacity:.8; font-size:.9rem; text-align:center; color:var(--muted); }
</style>
"""

# Theme root wrapper
wrapper_open = f"<div class='{ 'light' if st.session_state.theme == 'light' else '' }'>"
wrapper_close = "</div>"

st.markdown(common_css, unsafe_allow_html=True)
st.markdown(wrapper_open, unsafe_allow_html=True)

# ----------------------------
# Header (custom HTML inside Streamlit)
# ----------------------------
col1, col2, col3 = st.columns([3, 2, 2])
with col1:
    st.markdown(
        """
        <div class='header card'>
          <div class='brand'>
            <div class='logo'></div>
            <div class='title'>Hi‑Fi Streamlit</div>
            <span class='pill'>✨ Modern</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col2:
    pass
with col3:
    tcol1, tcol2 = st.columns([1,1])
    with tcol1:
        if st.session_state.theme == "dark":
            if st.button("🌞 Light Mode", use_container_width=True):
                set_theme("light")
                st.rerun()
        else:
            if st.button("🌙 Dark Mode", use_container_width=True):
                set_theme("dark")
                st.rerun()
    with tcol2:
        st.download_button(
            "⬇️ Download Sample CSV",
            data=(pd.DataFrame({
                "date": pd.date_range(datetime.today() - timedelta(days=29), periods=30),
                "visitors": np.random.randint(50, 350, size=30),
                "signups": np.random.randint(0, 60, size=30)
            }).to_csv(index=False).encode("utf-8")),
            file_name="sample_data.csv",
            mime="text/csv",
            use_container_width=True,
        )

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.image(
    "https://dummyimage.com/600x200/7c3aed/ffffff&text=Hi‑Fi+Streamlit",
    use_column_width=True,
)
st.sidebar.markdown("### Navigation")
page = st.sidebar.radio("", ["Overview", "Analytics", "Data", "Gallery", "Contact"], index=0)

st.sidebar.markdown("---")
with st.sidebar:
    st.markdown("#### Notifications")
    for n in st.session_state.notifications:
        with st.container(border=True):
            st.write(f"**{n['title']}**  ·  {n['time']}")
            st.caption(n["body"]) 

# ----------------------------
# Demo Data
# ----------------------------
np.random.seed(7)
dates = pd.date_range(datetime.today() - timedelta(days=60), periods=61)
traffic = pd.DataFrame({
    "date": dates,
    "visitors": np.random.randint(80, 450, len(dates)),
    "bounce": np.random.uniform(25, 65, len(dates)),
    "ctr": np.random.uniform(0.8, 6.2, len(dates)),
})
traffic["signups"] = (traffic["visitors"] * np.random.uniform(0.05, 0.18, len(dates))).astype(int)

# ----------------------------
# Overview Page
# ----------------------------
if page == "Overview":
    st.markdown("## Overview")
    st.caption("A polished Streamlit site with theming, cards, charts, tables, forms, and file uploads.")

    # KPI Metrics
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown("<div class='metric'><div class='label'>Visitors (7d)</div><div class='value'>"+str(int(traffic.tail(7)["visitors"].sum()))+"</div></div>", unsafe_allow_html=True)
    with m2:
        st.markdown("<div class='metric'><div class='label'>Signups (7d)</div><div class='value'>"+str(int(traffic.tail(7)["signups"].sum()))+"</div></div>", unsafe_allow_html=True)
    with m3:
        st.markdown("<div class='metric'><div class='label'>Avg Bounce</div><div class='value'>"+f"{traffic['bounce'].tail(7).mean():.1f}%"+"</div></div>", unsafe_allow_html=True)
    with m4:
        st.markdown("<div class='metric'><div class='label'>Avg CTR</div><div class='value'>"+f"{traffic['ctr'].tail(7).mean():.2f}%"+"</div></div>", unsafe_allow_html=True)

    st.markdown("### Traffic Snapshot")
    base = alt.Chart(traffic.tail(30)).encode(x=alt.X('date:T', title='Date'))
    line1 = base.mark_line(point=True).encode(y=alt.Y('visitors:Q', title='Visitors'))
    line2 = base.mark_area(opacity=0.25).encode(y='signups:Q')
    chart = alt.layer(line1, line2).resolve_scale(y='independent').properties(height=320)
    st.altair_chart(chart, use_container_width=True)

    c1, c2 = st.columns([2,1])
    with c1:
        st.markdown("### Activity Feed")
        with st.container(border=True):
            for i in range(6):
                st.write(f"**Update** · { (datetime.now()- timedelta(minutes=i*7)).strftime('%H:%M') }")
                st.caption("System processed new analytics and refreshed the dashboard.")
                st.divider()
    with c2:
        st.markdown("### Quick Actions")
        st.button("🚀 Publish Report", use_container_width=True)
        st.button("📥 Import Data", use_container_width=True)
        st.button("⚙️ Settings", use_container_width=True)

# ----------------------------
# Analytics Page
# ----------------------------
elif page == "Analytics":
    st.markdown("## Analytics")
    time_window = st.slider("Select days", 7, 60, 30)
    filtered = traffic.tail(time_window)

    t1, t2 = st.tabs(["Trends", "Distributions"])
    with t1:
        st.markdown("#### Visitors vs Signups")
        chart1 = alt.Chart(filtered).transform_fold([
            'visitors','signups'
        ]).mark_line(point=True).encode(
            x='date:T', y='value:Q', color='key:N'
        ).properties(height=360)
        st.altair_chart(chart1, use_container_width=True)

        st.markdown("#### Bounce Rate & CTR")
        left, right = st.columns(2)
        with left:
            c_bounce = alt.Chart(filtered).mark_area().encode(x='date:T', y=alt.Y('bounce:Q', title='Bounce %'))
            st.altair_chart(c_bounce, use_container_width=True)
        with right:
            c_ctr = alt.Chart(filtered).mark_bar().encode(x='date:T', y=alt.Y('ctr:Q', title='CTR %'))
            st.altair_chart(c_ctr, use_container_width=True)

    with t2:
        st.markdown("#### Distribution of Visitors")
        st.altair_chart(alt.Chart(filtered).mark_bar().encode(x=alt.X('visitors:Q', bin=True), y='count()'), use_container_width=True)

        st.markdown("#### Signups vs Visitors (scatter)")
        st.altair_chart(alt.Chart(filtered).mark_circle(size=120).encode(x='visitors', y='signups', tooltip=['date','visitors','signups']), use_container_width=True)

# ----------------------------
# Data Page
# ----------------------------
elif page == "Data":
    st.markdown("## Data")
    st.caption("Upload a CSV to preview, profile, and download a cleaned version.")

    uploaded = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded:
        df = pd.read_csv(uploaded)
        st.success(f"Loaded **{df.shape[0]}** rows, **{df.shape[1]}** columns")

        with st.expander("Preview", expanded=True):
            st.dataframe(df, use_container_width=True)

        with st.expander("Quick Profile"):
            st.write("Shape:", df.shape)
            st.write("Columns:", list(df.columns))
            st.write("Nulls per column:")
            st.write(df.isna().sum())

        # Example cleaning: drop duplicate rows, fill numeric nulls with median
        clean_df = df.copy()
        before = len(clean_df)
        clean_df.drop_duplicates(inplace=True)
        num_cols = clean_df.select_dtypes(include=[np.number]).columns
        for c in num_cols:
            if clean_df[c].isna().any():
                clean_df[c] = clean_df[c].fillna(clean_df[c].median())
        after = len(clean_df)

        st.info(f"Removed {before - after} duplicate rows. Filled nulls in numeric columns with median values.")

        st.download_button(
            "⬇️ Download Clean CSV",
            data=clean_df.to_csv(index=False).encode("utf-8"),
            file_name="clean_data.csv",
            mime="text/csv",
        )
    else:
        st.warning("No file uploaded yet. Use the Sample CSV from the header if you need data.")

# ----------------------------
# Gallery Page
# ----------------------------
elif page == "Gallery":
    st.markdown("## Gallery")
    st.caption("Drop images to view them in a responsive grid.")

    images = st.file_uploader("Upload images", type=["png","jpg","jpeg"], accept_multiple_files=True)

    if images:
        n = len(images)
        cols = st.columns(3)
        for i, img in enumerate(images):
            with cols[i % 3]:
                st.image(img, use_column_width=True)
    else:
        c = st.container()
        with c:
            st.info("No images uploaded yet. Try dragging a few images here ✨")

# ----------------------------
# Contact Page
# ----------------------------
elif page == "Contact":
    st.markdown("## Contact")
    st.caption("Send a message. The form simulates submit and echoes your entry.")

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your Name")
        email = st.text_input("Email")
        topic = st.selectbox("Topic", ["General", "Support", "Partnership", "Feedback"]) 
        msg = st.text_area("Message", height=150)
        col_a, col_b = st.columns([1,1])
        with col_a:
            subscribe = st.checkbox("Subscribe to updates")
        with col_b:
            priority = st.slider("Priority", 1, 5, 3)
        submitted = st.form_submit_button("Send", use_container_width=True)

    if submitted:
        with st.container(border=True):
            st.success("Message received! Here's what you sent:")
            st.write({
                "name": name,
                "email": email,
                "topic": topic,
                "message": msg,
                "subscribe": subscribe,
                "priority": priority,
                "time": datetime.now().isoformat(timespec='seconds')
            })
        st.balloons()

# ----------------------------
# Footer
# ----------------------------
st.markdown("""
<div class='footer'>
  Built with <strong>Streamlit</strong> · Themeable · Responsive · Single‑file demo. 
  <br/>Pro tip: use the sidebar to navigate and the header to switch themes.
</div>
""", unsafe_allow_html=True)

st.markdown(wrapper_close, unsafe_allow_html=True)

# 🎵 Apple iTunes Business Intelligence Suite

**An end-to-end Full-Stack Analytics application for digital music sales.**

## 📌 Project Overview

This project transforms the raw Apple iTunes relational dataset into a functional Business Intelligence (BI) tool. It features a custom-built **Python/Flask API**, a **SQLite relational database**, and a responsive **"Apple Music" styled dashboard** for real-time data exploration.

The goal was to solve a realistic business problem: *How can a global music retailer identify top-performing assets and underserved markets using relational data?*

## 🛠️ Technical Architecture

The system is built using a modern 3-tier architecture:

* **Database Layer:** Relational schema implemented in SQLite/MySQL with 11 interconnected tables.
* **Application Layer:** A RESTful API built with **Python & Flask** to handle complex SQL joins and data filtering.
* **Presentation Layer:** A dynamic UI built with **JavaScript (ES6)** and **CSS3**, featuring interactive sorting, global search, and master-detail views.

---

## 🚀 Key Features

* **Dynamic Data Exploration:** Users can search and sort through thousands of artists with zero-latency client-side filtering.
* **Master-Detail Drilldown:** Clicking an artist triggers a targeted SQL query to fetch real-time album stats and track counts.
* **Relational Integrity:** Successfully modeled complex relationships (One-to-Many and Many-to-Many) between Artists, Albums, and Tracks.
* **Mobile-Responsive Design:** "Apple Dark Mode" interface optimized for all screen sizes.

## 📊 Business Insights Uncovered

1. **Genre Dominance:** Rock and Latin music represent over 50% of the total revenue, suggesting a shift in inventory focus.
2. **Market Reach:** Identified North America as the primary revenue hub while highlighting growth potential in European markets.
3. **Efficiency:** Mapped employee-to-customer ratios to identify high-performing support representatives.

---

## 📂 Installation & Setup

To run this project locally, follow these steps:

1. **Clone the Repository:**
```bash
git clone https:/faizaanbhati95719-beep/github.com//itunes-bi-dashboard.git

```


2. **Install Dependencies:**
```bash
pip install -r requirements.txt

```


3. **Run the Application:**
```bash
python app.py

```


4. **Access the Dashboard:**
Open `http://127.0.0.1:5000` in your browser.

---

## 🧠 Challenges Overcome

* **SQL Logic Optimization:** Implemented `INNER JOIN` strategies to connect the `Artist` table to `Track` counts through the `Album` bridge.
* **State Management:** Managed UI states for the detail modals without the need for heavy frameworks like React.
* **Data Type Integrity:** Resolved SQL errors related to String-vs-Integer comparisons during the search logic.

---

### 📬 Contact

**Faizan**  – faizaanbhati95719@gmail.com

**Project Link:** - [ https://github.com/faizaanbhati95719-beep/iTune](https://github.com/faizaanbhati95719-beep/iTunes-Music-Store-Analysis-/edit/main)

---

**Would you like me to add a section specifically for the "Power BI" part of the project so you can show off your visualization skills too?**

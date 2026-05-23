<!-- ====== HEADER BANNER ====== -->
<h1 align="center"> Link Lens </h2>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Press+Start+2P&size=14&duration=3500&pause=1500&color=60A3BC&center=true&vCenter=true&width=1000&lines=From+broken+links+to+automated+collections.;One+scraper+to+find+them+all." />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-1e1e1e?style=for-the-badge&logo=python&logoColor=60A3BC&labelColor=0a3d62&color=0a3d62" alt="Python" />
  <img src="https://img.shields.io/badge/Status-Early_Development-1e1e1e?style=for-the-badge&logo=statuspal&logoColor=60A3BC&labelColor=0a3d62&color=0a3d62" alt="Status" />
  <img src="https://img.shields.io/badge/License-MIT-1e1e1e?style=for-the-badge&logo=opensourceinitiative&logoColor=60A3BC&labelColor=0a3d62&color=0a3d62" alt="License" />
</p>


<!-- ====== THE STORY ====== -->
<!-- ====== THE STORY ====== -->
<h2 align="center">💡 Why LinkLens?</h2>

<p align="justify">
It started with a 5TB drive and a shared obsession: collecting movies, series, and games — not just hoarding, but actually watching and playing them.  

At first, every download meant clicking links one by one. Then we got smarter: copy links into a text file, feed them to IDM with scheduling.  

The real pain came later. When Iran's internet restrictions forced our go‑to site to change domains overnight, <b>over 300 hand‑collected links became useless in an instant.</b>  

Nobody wanted to do that again. So we asked: <i>"What if a tool could handle this for us?"</i>  

That question became LinkLens — a Python project born from real frustration, built to automate link collection, survive domain changes, and grow into a full download manager. What started as a personal fix between two people is now evolving into a serious engineering portfolio project.
</p>

<!-- ====== WHAT THIS IS (RIGHT NOW) ====== -->
<h2 align="center">🔧 Current State</h2>

<p align="justify">
LinkLens is in <b>early development</b>. The first milestone is a CLI tool that takes a URL, extracts all download links (filtered by file type), and saves them to a text file — ready for your download manager.  

Later phases will add concurrent downloads, queue persistence, and link health monitoring. But right now, it solves one problem well: <b>never copy a download link by hand again.</b>
</p>

<!-- ====== PROJECT STRUCTURE ====== -->
<h2 align="center">📁 Project Structure</h2>

```
linklens/
├── pyproject.toml
├── config.yaml
├── README.md
│
├── linklens/
│ ├── init.py
│ ├── main.py
│ ├── core/
│ │ ├── init.py
│ │ ├── base_collector.py
│ │ └── filters.py
│ ├── collectors/
│ │ ├── init.py
│ │ ├── factory.py
│ │ └── generic.py
│ ├── infrastructure/
│ │ ├── init.py
│ │ ├── http_client.py
│ │ └── file_io.py
│ └── utils/
│ ├── init.py
│ └── url_utils.py
│
└── tests/
├── init.py
├── conftest.py
├── test_base_collector.py
└── test_generic.py
```

<p align="center"><sub>█▓▒░░░░░░░░░░░░░░░░░░░░░░░▒▓█</sub></p>

<div align="center">
  <sub>Early days. Clean structure. Big plans.</sub>
</div>

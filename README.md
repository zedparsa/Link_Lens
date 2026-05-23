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
<h2 align="center">💡 Why LinkLens?</h2>

<p align="justify">
I have a external hard drive and a habit of collecting movies, series, and games.  
Not just hoarding — I actually watch and play them.  

For a long time, this meant manually clicking download links. Then I got smarter: copy links into a text file, feed them to IDM with scheduling.  

Then the nightmare came. The site I relied on changed its domain overnight. <b>Over 300 hand‑collected links became useless.</b>  

I couldn't face doing that again. So I asked: <i>"What if a script could do this for me?"</i>  

That question became LinkLens — a Python project that started as a personal fix and is growing into a serious engineering portfolio piece.
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

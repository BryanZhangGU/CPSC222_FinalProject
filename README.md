# YouTube + Mood Analysis: Quantified Self Project

## 📌 Overview
This project analyzes the relationship between daily YouTube viewing behavior and self-reported mood scores. Data was collected over a 2-month period using the YouTube V2 API and daily mood journaling. The goal is to classify whether a given day had a positive mood based on viewing patterns.

## 📁 Project Files
- `youtube_mood_analysis_final.ipynb`: The main Jupyter Notebook (analysis + report)
- `utils.py`: Utility functions for data loading, processing, and modeling
- `youtube_data.csv`: Simulated viewing data (hour, category, watch time, etc.)
- `mood_data.csv`: Simulated mood scores (1–5 scale)
- `keys.json`: Contains API key (excluded from repo via `.gitignore`)
- `.gitignore`: Ensures `keys.json` is not tracked by Git

## 🚀 How to Run
1. Install dependencies:
    ```bash
    pip install pandas matplotlib seaborn scikit-learn
    ```

2. Run the notebook:
    ```bash
    jupyter notebook youtube_mood_analysis_final.ipynb
    ```

## 🔐 API Key Handling
Store your YouTube V2 API key in a `keys.json` file:
```json
{
  "youtube_api_key": "My_API"
}
```
Make sure this file is ignored by Git via `.gitignore`.

## 📊 Data Sources
- YouTube V2 API
- Self-recorded mood journal (CSV)

## 🧑‍💻 Author & Acknowledgments
- Author: Bryan Zhang
- Gonzaga University, CPSC 222 - Spring 2025
- Thanks to Dr. Gina Sprint


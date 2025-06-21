# 🎬 Movie Recommendation System

## 📅 Project Timeline
**December 2024**

---

## 📌 Overview

This project is a **Content-Based Movie Recommendation System** that suggests similar movies based on user-selected input. It utilizes **cosine similarity** over **TF-IDF vectorized features** extracted from movie metadata such as genres, overviews, and keywords.

---

## 🎯 Objectives

- Recommend top 5 similar movies to a given movie title.
- Improve the relevance of recommendations through effective feature engineering.
- Deliver a user-friendly interface to explore movie suggestions interactively.

---

## 🧪 Methodology

1. **Data Preprocessing**:
   - Cleaned and standardized movie metadata.
   - Extracted features: genres, overview, keywords.
   - Removed missing and irrelevant entries.

2. **Feature Engineering**:
   - Combined multiple fields (genres + keywords + overview) into a single textual corpus.
   - Applied text normalization (lowercasing, punctuation removal, etc.).

3. **Vectorization**:
   - Used `TfidfVectorizer` from scikit-learn.
   - Converted the text corpus into TF-IDF vectors.

4. **Similarity Computation**:
   - Computed cosine similarity between movies using their TF-IDF vector representations.

5. **Recommendation Logic**:
   - Given a movie title, the system retrieves top 5 most similar movies based on cosine similarity scores.

6. **User Interface**:
   - Built an interactive UI to accept input and display recommendations (using Streamlit or Flask).

---

## 💡 Features

- **Top 5 Movie Suggestions** based on selected input.
- **Genre and Keyword Matching** for improved personalization.
- **Lightweight & Fast** — real-time recommendations using precomputed vectors.

---

## 🧠 Tools & Technologies

- Python
- Pandas, NumPy
- scikit-learn (TF-IDF, cosine similarity)
- Streamlit or Flask (for UI)
- Pickle (for model persistence)

---

> **Author**: Amarjeet  
> **Project**: Movie Recommendation System

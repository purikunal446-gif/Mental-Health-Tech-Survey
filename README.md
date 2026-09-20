# Mental Health in Tech Survey — EDA

## Files
- `survey.csv` — source dataset
- `Mental_Health_Tech_Survey_EDA.ipynb` — completed Python EDA notebook
- `app.py` — Streamlit dashboard starter

## Project flow
1. Load and inspect the survey data.
2. Check duplicates and missing values.
3. Clean age and standardize gender for analysis.
4. Perform UBM analysis.
5. Create 20 charts with explanations.
6. Convert findings into workplace recommendations.
7. Use the Streamlit app for interactive exploration.

## Dataset context
The source material describes this as a 2014 survey measuring attitudes toward mental health and the frequency of mental health disorders in the tech workplace.

## Run Streamlit
```bash
pip install streamlit pandas matplotlib seaborn
streamlit run app.py
```

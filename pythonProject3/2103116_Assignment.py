import pandas as pd
import numpy as np
import re

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    confusion_matrix
)


df = pd.read_csv("Stress.csv")

# Drop missing rows
df = df.dropna()


#Text Cleaning Function

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)              # remove URLs
    text = re.sub(r"[^a-z\s]", " ", text)           # keep letters only
    text = re.sub(r"\s+", " ", text).strip()        # normalize spaces
    return text

df["clean_text"] = df["text"].apply(clean_text)

# TF-IDF Vectorization

vectorizer = TfidfVectorizer(
    max_features=3000,
    ngram_range=(1, 2),      # unigrams + bigrams
    stop_words="english",
    min_df=3
)

X = vectorizer.fit_transform(df["clean_text"]).toarray()

# Labels
y = df["label"].values

#  Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)


# Train Multinomial Naive Bayes

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
precision, recall, f1, _ = precision_recall_fscore_support(
    y_test, y_pred, average="binary"
)
cm = confusion_matrix(y_test, y_pred)


print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-score:  {f1:.4f}")

print("\nConfusion Matrix:")
print(cm)

#Prediction
def predict_stress(post, threshold=0.60):
    cleaned = clean_text(post)
    vectorized = vectorizer.transform([cleaned]).toarray()

    # Get probabilities instead of hard prediction
    probs = model.predict_proba(vectorized)[0]
    stress_prob = probs[1]   # probability of label = 1

    if stress_prob >= threshold:
        return f"STRESS (Confidence: {stress_prob:.2f})"
    else:
        return f"NOT STRESS (Confidence: {stress_prob:.2f})"


sample_post = "I am listening to a new song today"

print("\n--- Prediction for New Post ---")
print("Post:", sample_post)
print("Result:", predict_stress(sample_post))

import math
from collections import Counter

# ------------------------------------------------------------
# SIMPLE BM25 WORKED EXAMPLE
# Query: "information retrieval evaluation"
# ------------------------------------------------------------

documents = {
    "D1": "information retrieval evaluation improves search quality",
    "D2": "information retrieval systems retrieve relevant documents",
    "D3": "retrieval evaluation uses precision recall and ranking",
    "D4": "information information information search system"
}

query = "information retrieval evaluation"

# BM25 parameters
k1 = 1.5
b = 0.75


def tokenize(text):
    """Very simple tokenizer for classroom demonstration."""
    return text.lower().split()


# ------------------------------------------------------------
# 1. PREPROCESS DOCUMENTS
# ------------------------------------------------------------

tokenized_docs = {
    doc_id: tokenize(text)
    for doc_id, text in documents.items()
}

query_terms = tokenize(query)

N = len(tokenized_docs)

doc_lengths = {
    doc_id: len(tokens)
    for doc_id, tokens in tokenized_docs.items()
}

avgdl = sum(doc_lengths.values()) / N


# ------------------------------------------------------------
# 2. CALCULATE DOCUMENT FREQUENCY (DF)
# ------------------------------------------------------------

df = {}

for term in query_terms:
    df[term] = sum(
        1
        for tokens in tokenized_docs.values()
        if term in tokens
    )


# ------------------------------------------------------------
# 3. CALCULATE IDF
# Common BM25 IDF form:
#
# IDF(t) = log(1 + (N - DF(t) + 0.5) / (DF(t) + 0.5))
# ------------------------------------------------------------

idf = {}

for term in query_terms:
    idf[term] = math.log(
        1 + (N - df[term] + 0.5)
        / (df[term] + 0.5)
    )


# ------------------------------------------------------------
# 4. BM25 SCORING FUNCTION
# ------------------------------------------------------------

def bm25_score(doc_id):
    tokens = tokenized_docs[doc_id]
    tf_counts = Counter(tokens)
    doc_length = doc_lengths[doc_id]

    total_score = 0.0
    contributions = {}

    for term in query_terms:

        tf = tf_counts[term]

        if tf == 0:
            contributions[term] = 0.0
            continue

        numerator = tf * (k1 + 1)

        denominator = (
            tf
            + k1 * (
                1 - b
                + b * doc_length / avgdl
            )
        )

        term_score = (
            idf[term]
            * numerator
            / denominator
        )

        contributions[term] = term_score
        total_score += term_score

    return total_score, contributions


# ------------------------------------------------------------
# 5. SCORE AND RANK ALL DOCUMENTS
# ------------------------------------------------------------

results = []

for doc_id in documents:
    score, contributions = bm25_score(doc_id)

    results.append(
        (doc_id, score, contributions)
    )

results.sort(
    key=lambda x: x[1],
    reverse=True
)


# ------------------------------------------------------------
# 6. DISPLAY THE WORKED EXAMPLE
# ------------------------------------------------------------

print("QUERY:", query)
print("k1 =", k1)
print("b  =", b)
print("Average document length =", round(avgdl, 2))

print("\nDOCUMENT FREQUENCY AND IDF")
print("-" * 45)

for term in query_terms:
    print(
        f"{term:12s} "
        f"DF={df[term]}  "
        f"IDF={idf[term]:.4f}"
    )


print("\nBM25 DOCUMENT SCORES")
print("-" * 60)

for rank, (doc_id, score, contributions) in enumerate(
    results,
    start=1
):
    print(
        f"\nRank {rank}: {doc_id}"
    )

    print(
        "Document:",
        documents[doc_id]
    )

    print(
        "Length:",
        doc_lengths[doc_id]
    )

    for term in query_terms:
        tf = tokenized_docs[doc_id].count(term)

        print(
            f"  {term:12s} "
            f"TF={tf}  "
            f"Contribution="
            f"{contributions[term]:.4f}"
        )

    print(
        f"TOTAL BM25 SCORE = {score:.4f}"
    )

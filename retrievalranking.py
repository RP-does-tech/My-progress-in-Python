import math

# ------------------------------------------------------------
# TD2309 - CHAPTER 7: RETRIEVAL EVALUATION
# Simple worked example
# ------------------------------------------------------------

# A search system returns 8 documents in this order.
retrieved_ranking = [
    "D3", "D1", "D7", "D5",
    "D2", "D9", "D4", "D8"
]

# For this query, these documents are known to be relevant.
relevant_documents = {
    "D1", "D2", "D3", "D4", "D6", "D7"
}

# Optional graded relevance for nDCG:
# 2 = highly relevant
# 1 = partially relevant
# 0 = non-relevant
graded_relevance = {
    "D1": 2,
    "D2": 1,
    "D3": 2,
    "D4": 1,
    "D5": 0,
    "D6": 2,
    "D7": 1,
    "D8": 0,
    "D9": 0,
    "D10": 0
}


# ------------------------------------------------------------
# 1. BASIC COUNTS: TP, FP, FN
# ------------------------------------------------------------

retrieved_set = set(retrieved_ranking)

TP = len(retrieved_set & relevant_documents)
FP = len(retrieved_set - relevant_documents)
FN = len(relevant_documents - retrieved_set)

print("RETRIEVED RANKING")
print("-" * 40)

for rank, doc_id in enumerate(retrieved_ranking, start=1):
    label = (
        "Relevant"
        if doc_id in relevant_documents
        else "Not Relevant"
    )
    print(f"Rank {rank}: {doc_id} -> {label}")

print("\nBASIC COUNTS")
print("-" * 40)
print("TP =", TP)
print("FP =", FP)
print("FN =", FN)


# ------------------------------------------------------------
# 2. PRECISION
# Precision = TP / (TP + FP)
# ------------------------------------------------------------

precision = TP / (TP + FP)

print("\nPRECISION")
print("-" * 40)
print(f"Precision = {TP} / ({TP} + {FP})")
print(f"Precision = {precision:.3f}")


# ------------------------------------------------------------
# 3. RECALL
# Recall = TP / (TP + FN)
# ------------------------------------------------------------

recall = TP / (TP + FN)

print("\nRECALL")
print("-" * 40)
print(f"Recall = {TP} / ({TP} + {FN})")
print(f"Recall = {recall:.3f}")


# ------------------------------------------------------------
# 4. F1 SCORE
# F1 = 2PR / (P + R)
# ------------------------------------------------------------

f1 = 2 * precision * recall / (precision + recall)

print("\nF1 SCORE")
print("-" * 40)
print(f"F1 = {f1:.3f}")


# ------------------------------------------------------------
# 5. PRECISION AT 5
# ------------------------------------------------------------

k = 5
top_k = retrieved_ranking[:k]

relevant_in_top_k = sum(
    1 for doc_id in top_k
    if doc_id in relevant_documents
)

p_at_k = relevant_in_top_k / k

print("\nPRECISION AT 5")
print("-" * 40)
print("Top 5:", top_k)
print("Relevant in top 5 =", relevant_in_top_k)
print(f"P@5 = {p_at_k:.3f}")


# ------------------------------------------------------------
# 6. RECIPROCAL RANK
# ------------------------------------------------------------

first_relevant_rank = None

for rank, doc_id in enumerate(retrieved_ranking, start=1):
    if doc_id in relevant_documents:
        first_relevant_rank = rank
        break

reciprocal_rank = (
    1 / first_relevant_rank
    if first_relevant_rank
    else 0
)

print("\nRECIPROCAL RANK")
print("-" * 40)
print(
    "First relevant document appears at rank",
    first_relevant_rank
)
print(f"RR = {reciprocal_rank:.3f}")


# ------------------------------------------------------------
# 7. AVERAGE PRECISION (AP)
# ------------------------------------------------------------

precision_values = []
relevant_seen = 0

print("\nAVERAGE PRECISION")
print("-" * 40)

for rank, doc_id in enumerate(retrieved_ranking, start=1):
    if doc_id in relevant_documents:
        relevant_seen += 1
        precision_at_rank = relevant_seen / rank
        precision_values.append(precision_at_rank)

        print(
            f"Relevant at rank {rank}: "
            f"Precision@{rank} = "
            f"{precision_at_rank:.3f}"
        )

average_precision = (
    sum(precision_values)
    / len(relevant_documents)
)

print(f"AP = {average_precision:.3f}")


# ------------------------------------------------------------
# 8. nDCG
# Used when relevance is graded.
# ------------------------------------------------------------

def dcg(relevance_scores):
    total = 0.0

    for rank, rel in enumerate(relevance_scores, start=1):
        if rank == 1:
            total += rel
        else:
            total += rel / math.log2(rank + 1)

    return total


retrieved_grades = [
    graded_relevance.get(doc_id, 0)
    for doc_id in retrieved_ranking
]

dcg_score = dcg(retrieved_grades)

ideal_grades = sorted(
    graded_relevance.values(),
    reverse=True
)[:len(retrieved_ranking)]

ideal_dcg = dcg(ideal_grades)

ndcg = (
    dcg_score / ideal_dcg
    if ideal_dcg > 0
    else 0
)

print("\nnDCG")
print("-" * 40)
print("Grades in retrieved order:", retrieved_grades)
print("Ideal grades:", ideal_grades)
print(f"DCG = {dcg_score:.3f}")
print(f"Ideal DCG = {ideal_dcg:.3f}")
print(f"nDCG = {ndcg:.3f}")


# ------------------------------------------------------------
# 9. FINAL SUMMARY
# ------------------------------------------------------------

print("\nFINAL EVALUATION SUMMARY")
print("-" * 40)
print(f"Precision : {precision:.3f}")
print(f"Recall    : {recall:.3f}")
print(f"F1        : {f1:.3f}")
print(f"P@5       : {p_at_k:.3f}")
print(f"RR        : {reciprocal_rank:.3f}")
print(f"AP        : {average_precision:.3f}")
print(f"nDCG      : {ndcg:.3f}")

print("\nINTERPRETATION")
print("-" * 40)
print("Precision = how clean the retrieved result set is.")
print("Recall    = how much relevant material was found.")
print("P@5       = quality of the first five results.")
print("RR        = how early the first relevant result appears.")
print("AP        = rewards relevant documents appearing early.")
print("nDCG      = useful when relevance has graded levels.")

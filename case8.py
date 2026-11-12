pos_words = ["good", "great", "excellent", "helpful", "clear", "best"]
neg_words = ["bad", "poor", "slow", "boring", "confusing", "worst"]

n = int(input("Enter number of student feedbacks to analyze: "))

for i in range(1, n + 1):
    print("\n--- Feedback", i, "---")
    fb = input("Enter feedback sentence: ").lower()
    words = fb.split()

    p_cnt = 0
    n_cnt = 0

    for w in words:
        w_clean = w.strip(".,!?")
        if w_clean in pos_words:
            p_cnt = p_cnt + 1
        elif w_clean in neg_words:
            n_cnt = n_cnt + 1

    score = p_cnt - n_cnt

    if score > 0:
        status = "POSITIVE"
    elif score < 0:
        status = "NEGATIVE"
    else:
        status = "NEUTRAL"

    print("Positive Words:", p_cnt, "| Negative Words:", n_cnt, "| Score:", score)
    print("Sentiment Classification:", status)

SLOPE = 0.25
print("wyniki na 1000 próbek")
for smartness in [0,1,2]:
    for weapon_amount in [0,1,2,3,4]:
        basic_prob = 0
        success_prob = min(1, (smartness + weapon_amount) * SLOPE + basic_prob)
        failure_prob = max(0, 1 - ((smartness + weapon_amount) * SLOPE + basic_prob))
        result = [True, False]
        weights = [success_prob, failure_prob]
        #weights = [1]
        from collections import Counter
        from random import choices
        samples = choices(result, weights, k=1000)
        print(f"smartness = {smartness}  weapon amount = {weapon_amount}   wyniki na 1000 próbek  {Counter(samples)} ")
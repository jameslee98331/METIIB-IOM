import pandas as pd
from apyori import apriori

sales_data = pd.read_csv('sales.csv')

records = [([str(sales_data.values[i,j]) for j in range(0, 6)]) for i in range(0, sales_data.shape[0])]

association_rules = apriori(
                            records,
                            min_support=0.07,
                            min_confidence=0.8,
                            min_lift=3,
                            min_length=2,
                            max_length=4
                            )
association_results = list(association_rules)

rules = []
supports = []
confidences = []
lifts = []

for item in association_results:

    pair = item[0]
    items = [x for x in pair]
    rule = str(list(item.ordered_statistics[0].items_base)) + " -> " + str(list(item.ordered_statistics[0].items_add))
    support = item.support
    confidence = item[2][0][2]
    lift = item[2][0][3]

    print("Rule: " + rule)
    print("Support: " + str(support))
    print("Confidence: " + str(confidence))
    print("Lift: " + str(lift))
    print("=====================================")

    rules.append(rule)
    supports.append(support)
    confidences.append(confidence)
    lifts.append(lift)

print(rules)
print(supports)
print(confidences)
print(lifts)

apriori_results = pd.DataFrame(list(zip(rules, supports, confidences, lifts)),
               columns =['Rule', 'Support', 'Confidence', 'Lift'])
apriori_results.to_csv('C://Users//James//Desktop//apriori_results.csv', encoding='utf-8', index=False)

print(apriori_results)

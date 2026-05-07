from drug_interaction import Drug

obj = Drug()

medicine_A = obj.fetch_drug(obj.drug_A)
medicine_B = obj.fetch_drug(obj.drug_B)

data_A = obj.save_data(obj.drug_A, medicine_A)
data_B = obj.save_data(obj.drug_B, medicine_B)

result = obj.comparison(obj.drug_A, obj.drug_B)
obj.generate_report(result)
obj.save_history(obj.drug_A, obj.drug_B, result['Risk level'])
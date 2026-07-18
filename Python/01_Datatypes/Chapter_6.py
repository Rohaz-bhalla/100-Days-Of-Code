chai_type = "elaichi"
customer_name = "Rohaz"

chai_preference = "Aromatic and Bold"
print(f"First word : {chai_preference[:8]}")
print(f"Last word : {chai_preference[12:]}")
print(f"Reverse the words : {chai_preference[::-1]}")

print()

label_text = "Chai Spécial"
encoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")
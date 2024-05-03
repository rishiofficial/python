# 7. Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

cofee_size = 'Medium'
extra_shot = False

if extra_shot:
    cofee = cofee_size + " cofee with an extra shot"
else:
    cofee = cofee_size + " Cofee without extra shot"

print(cofee)
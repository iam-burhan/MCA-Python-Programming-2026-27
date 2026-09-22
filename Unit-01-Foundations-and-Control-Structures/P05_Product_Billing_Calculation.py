subtotal = 0
for i in range(1, 4):
    price = float(input(f"Enter price of product {i}: "))
    qty = int(input(f"Enter quantity of product {i}: "))
    subtotal = subtotal + (price * qty)

discount = 0.10 * subtotal  # 10% discount
amount_after_discount = subtotal - discount
gst = 0.18 * amount_after_discount  # 18% GST
final_amount = amount_after_discount + gst

print(f"\nSubtotal: ₹{subtotal:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"GST (18%): ₹{gst:.2f}")
print(f"Final Payable Amount: ₹{final_amount:.2f}")
"""
Program : Find the ststud approved or not
Author : Varshilkumar
"""


def requision_approval ():
    total_amount = 0
    while True:
        price = input("Enter the price of the item (or end to stop): ")
        if price.lower() == "end":
            break
        total_amount = total_amount + float(price)
        return total_amount

def approval_request (total_amount):
    if total_amount < 500:
        status = "pending"
        message = "Follow the process"
    else :
        status = "Approved"
        message = "Approval referance Number"

        print (f"Status :", status)
        print(f"message :", message)
        print("status", status)
        print("message", message)
        # return {"status ": message, "status": message,"message ": status1,"message": status2}
        return {"status": status, "message" : message }
    
def main_ans():
  total_amount = requision_approval()
  approval_ststus = approval_request(total_amount)

main_ans()














def  calculate_total_amount():
    total_amount = 0
    while True:
        price = input("Enter the price of an item (or 'finish' to stop): ")
        if price.lower() == "finish":
            break
        total_amount = total_amount + float(price)
    return total_amount

def categorize_request(total_amount): approval rewquest
    if total_amount < 150:
        category = "Low"
        recommendation = "Proceed with standard processing."
    else:
        category = "High"
        recommendation = "Review for potential discounts."
   
    print(f"Category: {category}")
    print(f"Recommendation: {recommendation}")
    return {"category": category, "recommendation": recommendation}




  print(f"Category: {category}")
    print(f"Recommendation: {recommendation}")
    return {"category": category, "recommendation": recommendation}
def  main_answer():
    total_amount = calculate_total_amount()
    categorization = categorize_request(total_amount)
main_answer()
"""
Program : collect user data
Author : Varshilkumar
"""


print()
def collect_staff_info(requisition_id):
    print("printing Staff Information:")
    date = input("Enter the date in (dd/mm/yyyy) formate :")
    staff_id = input("Staff ID :")
    name = input("Enter the name :")

    unique_id = requisition_id + 1
    requisition_id = unique_id

    print(f"\nPrinting Staff Information:")
    print(f"Date: {date}")
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name: {name}")
    print(f"Requisition ID: {unique_id}")

    return requisition_id,unique_id,staff_id,date,name

def main():
    
    requisition_id = 10000
    requisition_id, unique_id, date, staff_id, name  = collect_staff_info(requisition_id)
main()




    







   
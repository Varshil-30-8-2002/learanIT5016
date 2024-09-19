"""
Program: which is for requestion system.
Author: Varshilkumar
"""
print() # This is used to make space at the top of the output
class RequisitionsSysyem():

    def __init__(self):
        self.request_id_counter = 1
        self.requests = []

    # Method to collect geberal information from the staff

    def staff_info(self, date, staff_id, staff_name, requisition_id):
        return{
        "Date": date,
        "Staff ID": staff_id,
        "Staff name" : staff_name,
        "Requisition ID": requisition_id
    }
    # Method for the items & cost
    def requisition_details(self, items):
        total = sum(item["cost"]for item in items)
        return{"total": total, "items":items}
   
   # Method for Approval status
    def requisition_approval(self, total):
        if total < 500:
            return {"ststus": "approved", "reference": f"ARP - {self.request_id_counter}"}
        else:
            return{"status": "pending", "reference": None}

    # Creates methid to respond 
    def respond_requisition(self, request_id, status):
        for request in self.requests:
            if request["id"] == request_id:
                request["status"] = status
                if status =="Approved":
                    request["Reference"] = f"ARP - {request_id}"
                    break

    # Method created for Display tha info of all requisition
    def display_requisitons(self):
        for request in self.requests:
            print(f"Name: {request['user_info']['name']}")
            print(f"Unique ID: {request['id']}")
            print(f"Total: ${request['total']:.2f}")
            print(f"Status: {request['status']}")
            if request["ststus"] == "Approved":
                print(f"Approval Referance: {request['refetence']}")
            print("")
  
    #This Method print the ststistic information below
    def requisition_statistic(self):
        total_requests = len(self.requests)
        approved_requests = sum(1 for request in self.requests if request["status"] == "Approved")
        pendind_requests = sum(1 for request in self.requests if request["ststus"] == "Pending")
        not_approved_request = sum(1 for request in self.requests if request["status"] == "Not Approved")

        print(f"Total number of requests submitted: {total_requests}")
        print(f"Total number of approved requests: {approved_requests}")
        print(f"Total number of pending requests: {pendind_requests}")
        print(f"Total number of not approved requests: {not_approved_request}")

    # Define Main function to the function
    
def main():

    requisitions_system = RequisitionsSysyem() # object creates

    while True:
        print("Date")
        print("Staff ID")
        print("Staff Name")
        print("Requisition Id")
        print("Tolat")
        print("Status")
        print("Approval Referance Number")
           
   # def

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Date: ")
            staff_id = input("Staff ID")
            staff_name = input("Staff Name")
            requisition_id = input("Requisition ID: ")
            items = []
            while True:
                item_name = input("Enter item name (or 'done' to finish): ")
                if item_name.lower() == "done":
                    break
                item_cost = float(input("Enter item cost: "))
                items.append({"name": item_name, "cost": item_cost})

            staff_info = requisitions_system.staff_info(date, staff_id, staff_name, requisition_id)
            requisition_details =requisitions_system.requisition_details(items)
            total = requisition_details["total"]
            approval_response = requisitions_system.requisition_approval(total)
            requisitions_system.requests.append({"id": requisitions_system.request_id_counter, "staff_info": staff_info, "total": total, "items": items, "status": approval_response["status"], "reference": approval_response["reference"]})
            requisitions_system.request_id_counter += 1
            print("Request submitted successfully!")


            
        elif choice == "2":
            
            requisitions_system = int(input("Enter request ID: "))
            status = input("Enter response (approved/not approved): ")
            requisitions_system.respond_requisition(requisition_id, status)
            print("Request responded successfully!")

        elif choice == "3":
            requisitions_system.display_requisitons()

        elif choice == "4":
            requisitions_system.requisition_statistic()

        elif choice == "5":            
            break

        else:
                print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
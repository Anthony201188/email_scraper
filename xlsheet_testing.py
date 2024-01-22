import openpyxl

def create_excel_file(file_name, data):
    # Create a new workbook and select the active sheet
    wb = openpyxl.Workbook()
    sheet = wb.active

    # Insert data into the first column (column A)
    for email in data:
        sheet.append([email])

    # Save the workbook to a file
    wb.save(file_name)

# Example usage:
email_list = ["user1@example.com", "user2@example.com", "user3@example.com"]
create_excel_file("output.xlsx", email_list)

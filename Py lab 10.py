#CODE 1: MAKE A CSV FILE WHICH CAN BE OPENED IN EXCEL
import csv
with open("text.csv","w") as f:
    add=csv.writer(f);
    add.writerow(["name","marks","subject"])
    add.writerow(["Parth","20","Maths"])

#CODE2: Read the data stored in MS-Excel file and convert it into a dictionary. The record contains rollno, name of student, marks of three subjects. Also calculate total. Display the dictionary data on the monito
import csv
students_data = {}
with open('students.csv', mode='r') as file:
    reader = csv.DictReader(file);
    for row in reader:
        rollno = row['rollno'];
        name = row['name'];
        marks1 = int(row['subject1']);
        marks2 = int(row['subject2']);
        marks3 = int(row['subject3']);
        total = marks1 + marks2 + marks3
        students_data[rollno] = {'name': name,'subject1': marks1,'subject2': marks2,'subject3': marks3,'total': total};
for rollno, data in students_data.items():
    print("Roll No:", rollno, "Name:", data['name'], "Marks:", data['subject1'], data['subject2'], data['subject3'], "Total:", data['total']);
    
#CODE3:Accept contact details from the user and create a vcard that we can directly store in our mobile
name = input("Pls full name: ");
phone = input("Pls phone number: ");
vcard = "BEGIN:VCARD\n";
vcard += "FN:" + name + "\n";
vcard += "TEL;TYPE=CELL:" + phone + "\n";
vcard += "END:VCARD\n";
with open("contact.vcf", "w") as file:
    file.write(vcard);
#CODE4:Create a specific subdirectory and copy one file from another subdirectory to this newly created subdirectory
source_path = "f1/file1.txt";
target_path = "f2/file2.txt";
source_file = open(source_path, "r");
target_file = open(target_path, "w");
for line in source_file:
    target_file.write(line);
source_file.close();
target_file.close();

print("File copied successfully.")

#CODE5:Write a program to copy contents of one file to another. While doing so, replace all lowercase characters into uppercase characters
with open("event.txt", "r") as f1:
    with open("emqweek6.txt", "w") as f2:
        lines = f1.readlines();
        for line in lines:
            f2.write(line.lower());

#CODE6:Write a program that merges lines alternatively from two files and writes the results to new file. If one file has less number of lines than the other, the remaining lines from the larger file should be simply copied into the target file.
source_file1 = "file1.txt";
source_file2 = "file2.txt";
target_file = "merged.txt";
with open(source_file1, "r") as f1, open(source_file2, "r") as f2, open(target_file, "w") as f3:
    lines1 = f1.readlines();lines2 = f2.readlines();
    max_lines = max(len(lines1), len(lines2));
    for i in range(max_lines):
        if i < len(lines1):
            f3.write(lines1[i]);
        if i < len(lines2):
            f3.write(lines2[i]);

#CODE7:If an Employee object contains following details:empcode, empname, Date of Joining, Salary Write a program to serialize and deserialize this data.
empcode = 101;empname = "Raj";date_of_joining = "2025";salary = 50000;
def serialize_employee(empcode, empname, date_of_joining, salary, filename):
    with open(filename, "w") as file:
        file.write(str(empcode) + "\n");
        file.write(empname + "\n");
        file.write(date_of_joining + "\n");
        file.write(str(salary) + "\n");
def deserialize_employee(filename):
    with open(filename, "r") as file:
        empcode = int(file.readline().strip());
        empname = file.readline().strip();
        date_of_joining = file.readline().strip();
        salary = float(file.readline().strip());
        return empcode, empname, date_of_joining, salary;
serialize_employee(empcode, empname, date_of_joining, salary, "employee_data.txt");
empcode, empname, date_of_joining, salary = deserialize_employee("employee_data.txt");
print(empcode, empname, date_of_joining, salary);



#CDOE:8. Given a text file, write a program to create another text file deleting the words ‘a’, ‘the’, ‘an’ and replacing each one of them with a blank spac


words = ['a', 'the', 'an']
with open('input_file.txt', 'r') as input_file:
    content = input_file.read();
for word in words:
    content = content.replace(' ' + word + ' ', ' ');
    content = content.replace(' ' + word + '\n', '\n'); 
    content = content.replace('\n' + word + ' ', '\n');
with open('output_file.txt', 'w') as output_file:
    output_file.write(content);








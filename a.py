import docx
import csv

def replace_string (search_text, replace_text):
    doc = docx.Document('test_doc_1.docx')
      
    for p in doc.paragraphs:
        if search_text in p.text:
            p.text = p.text.replace(search_text,replace_text,1)
            break
    doc.save('test_doc_1.docx')

with open('./1.csv', 'r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_file:
        row = row.replace('\n','').split(',')

        ticket_number = row[0]
        lane_number = row[1]
        building_number = row[2]
        room_number = row[3]

        replace_string ('XXXX', ticket_number)
        replace_string ('AAA', lane_number)
        replace_string ('BBB', building_number)
        replace_string ('CCC', room_number)

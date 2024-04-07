import os
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle


def buyer_details():
    detail = {}
    detail["Name"] = input("ENTER YOUR NAME :-")
    detail["EM"] = input("ENTER YOUR Email :-")
    detail["PH"] = int(input("ENTER YOUR Phone No :-"))
    return detail

def get_item_details(num_items):
    items = []
    for i in range(num_items):
        item = {}
        item["name"] = input(f"Enter name of item {i+1}: ")
        item["quantity"] = int(input(f"Enter quantity of item {i+1}: "))
        item["rate"] = float(input(f"Enter rate of item {i+1}: "))
        item["total"] = item["quantity"] * item["rate"]
        items.append(item)
    return items

c = canvas.Canvas("Receipt.pdf")
c.setFont("Helvetica-Bold", 30)
c.drawString(160, 780, "PAYMENT RECEIPT")

text = c.beginText(60, 700)
text.setFont("Helvetica-BoldOblique", 15)
text.textLine("SELLER DETAILS:-")
c.line(60,695,200,695)
text.setFont("Times-Roman", 13)
text.textLine("Metro Plaza")
text.textLine("123, Park Street, Kolkata")
text.textLine("Ph: 305-266-0212")
c.drawText(text)

c.line(60, 635, 530, 635)

text2 = c.beginText(60, 620)
text2.textLine("")
text2.textLine("")
text2.setFont("Helvetica-BoldOblique", 15)
text2.textLine("BUYER DETAILS:-")
c.line(60,583,200,583)
c.drawText(text2)

buyer = buyer_details()
text3 = c.beginText(60, 600)
text3.textLine("")
text3.textLine("")
text3.setFont("Times-Roman", 12)
text3.textLine(f"NAME:  {buyer['Name']}")
text3.textLine(f"EMAIL: {buyer['EM']}")
text3.textLine(f"PHONE: {buyer['PH']}")
text3.textLine("")
text3.textLine("")
c.drawText(text3)

table_y = text3.getY() - 20

num_items = int(input("How many items have you purchased? "))
items = get_item_details(num_items)
data = [["ITEM", "QTY", "RATE", "TOTAL"]]
subtotal = 0
for item in items:
    data.append([item["name"], item["quantity"], item["rate"], item["total"]])
    subtotal += item["total"]


data.append(["SUBTOTAL", "", "", subtotal])

table = Table(data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('VALIGN', (0, 0), (-3, -3), 'MIDDLE'),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('FONTNAME', (-1, -1), (-1, -1), 'Helvetica-Bold'),
]))

table_width, table_height = table.wrap(400, 600)
table_x = (c._pagesize[0] - table_width) / 2

table.drawOn(c, table_x, table_y)

c.save()

os.system("start Receipt.pdf")

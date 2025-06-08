import pandas as pd
from fpdf import FPDF

# 1️⃣ Read the data
df = pd.read_csv('data.csv')

# 2️⃣ Analyze the data
average_score = df['Score'].mean()
highest_score = df['Score'].max()
lowest_score = df['Score'].min()

# 3️⃣ Generate PDF report
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Automated Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Create PDF instance
pdf = PDF()
pdf.add_page()

# Title
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Data Summary', ln=True)

# Insert analysis results
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, f'Average Score: {average_score:.2f}', ln=True)
pdf.cell(0, 10, f'Highest Score: {highest_score}', ln=True)
pdf.cell(0, 10, f'Lowest Score: {lowest_score}', ln=True)

# Insert table data
pdf.cell(0, 10, ' ', ln=True)  # Empty line
pdf.set_font('Arial', 'B', 12)
pdf.cell(40, 10, 'Name', border=1)
pdf.cell(30, 10, 'Age', border=1)
pdf.cell(30, 10, 'Score', border=1)
pdf.ln()

pdf.set_font('Arial', '', 12)
for index, row in df.iterrows():
    pdf.cell(40, 10, row['Name'], border=1)
    pdf.cell(30, 10, str(row['Age']), border=1)
    pdf.cell(30, 10, str(row['Score']), border=1)
    pdf.ln()

# Save the PDF
pdf.output('report.pdf')
print("PDF report generated: report.pdf")

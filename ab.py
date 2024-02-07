import PyPDF2
import pandas as pd

def extract_variables_from_pdf(pdf_file_path):
    # Open the PDF file
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # Extract text from each page
        text = ''
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extractText()
    
    # Extracting variables from the text
    variable1 = None
    variable2 = None
    # Modify this part to extract your specific variables from the 'text' variable

    # Example: Extracting two numbers separated by a comma
    parts = text.split(',')
    if len(parts) >= 2:
        variable1 = parts[0].strip()
        variable2 = parts[1].strip()

    return variable1, variable2

def save_to_csv(variable1, variable2, output_file):
    data = {'Variable1': [variable1], 'Variable2': [variable2]}
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    pdf_file_path = '/Users/macbook/Documents/Projects/ishkode/Class_1.pdf'
    output_csv_file = 'output.csv'

    var1, var2 = extract_variables_from_pdf(pdf_file_path)
    save_to_csv(var1, var2, output_csv_file)



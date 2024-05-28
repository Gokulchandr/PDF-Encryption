import PyPDF2 as p
output = p.PdfWriter()
input_pdf=input("Enter your PDF name: ")
input_stream = p.PdfReader(open(input_pdf + ".pdf", "rb"))
for i in range(len(input_stream.pages)):
    output.add_page(input_stream.pages[i])
name=input("Enter the name of PDF after the encryption: ")
output_stream=open(name + ".pdf","wb")
Password=input("Enter the Password: ")
output.encrypt(Password, use_128bit=True)
output.write(output_stream)
output_stream.close()

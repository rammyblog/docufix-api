import PyPDF2

# def getPdfText(filename)
#     pdfFileObj = open(filenam, 'rb')
#     pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#     pageNumber = pdfReader.numPages
#     for m in range(pageNumber)
#         pageObj = pdfReader.getPage(m)
#     pageObj.extractText()


# This function will extract and return the pdf file text content.
def getPdfText(filename):

    # Open the pdf file in read binary mode.
    fileObject = open('.'+filename, 'rb')

    # Create a pdf reader .
    pdfFileReader = PyPDF2.PdfFileReader(fileObject)

    # Get total pdf page number.
    totalPageNumber = pdfFileReader.numPages

    # Print pdf total page number.
    print('This pdf file contains totally ' + str(totalPageNumber) + ' pages.')

    currentPageNumber = 0
    text = ''

    # Loop in all the pdf pages.
    while(currentPageNumber < totalPageNumber ):

        # Get the specified pdf page object.
        pdfPage = pdfFileReader.getPage(currentPageNumber)

        # Get pdf page text.
        text = text + pdfPage.extractText()

        # Process next page.
        currentPageNumber += 1

    if(text == ''):
        # If can not extract text then use ocr lib to extract the scanned pdf file.
        text = textract.process(filePath, method='tesseract', encoding='utf-8')
       
    return text
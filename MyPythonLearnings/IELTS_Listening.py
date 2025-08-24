# print("Introduction")
# print("How can this book help you with your listening ?\nListening and reading both are considered as thr easy part of the IELTS test, but this does not mean that they do not require preparation.\nThis book provides you with the means of preparing fully for the listening test.\nIt is designed as a complete A-toZ guide and should be read in its entirety.\nIf you are reading this book, you already have the required level of English to do well in both tests. What you are probably lacking is a sound knowledge of the strategies needed to get very high marks.\nThis book will take you step by step through the different sub skills. that are required and the different strategies I suggest for dealing with all of the different question types.")
# print("\nTips for Effective Listening Practice:")
# print("1. Listen to a variety of accents and topics.")
# print("2. Practice with both audio and video materials.")
# print("3. Take notes while listening to improve retention.")
# print("4. Review transcripts to understand missed information.")
# print("5. Simulate exam conditions for practice tests.")



import PyPDF2

with open("/Users/devanshshah/Developer/Youtube/100DaysOfCode/100_Days_Of_Code/MyPythonLearnings/listeningGuide.pdf", "rb") as f:
    reader = PyPDF2.PdfReader(f)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

print(text)
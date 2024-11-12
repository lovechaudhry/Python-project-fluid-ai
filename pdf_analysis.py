import fitz  # PyMuPDF
import openai
import re
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up the OpenAI API key
openai.api_key = "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"


def extract_text_from_pdf(pdf_path):
    """
    Extracts text from each page of a PDF file.

    Parameters:
    pdf_path (str): Path to the PDF file.

    Returns:
    str: Concatenated text of all pages.
    """
    try:
        text = ""
        with fitz.open(pdf_path) as pdf:
            for page_num in range(pdf.page_count):
                page = pdf[page_num]
                text += page.get_text()
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None

def clean_text(text):
    """
    Cleans and preprocesses extracted text for analysis.

    Parameters:
    text (str): Raw text extracted from the PDF.

    Returns:
    str: Cleaned text.
    """
    text = re.sub(r'\n+', '\n', text)  # Remove excessive newlines
    text = re.sub(r'\s+', ' ', text)   # Reduce multiple spaces to one
    return text.strip()

def analyze_text_with_gpt(text, prompt_template):
    """
    Sends text to OpenAI's GPT model to analyze and extract key information.

    Parameters:
    text (str): Cleaned text for analysis.
    prompt_template (str): Template prompt for GPT analysis.

    Returns:
    str: GPT response with key extracted information.
    """
    prompt = prompt_template.format(text=text)
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that extracts investor-relevant information."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=800,
            temperature=0.2
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error with GPT analysis: {e}")
        return None



def main(pdf_path):
    """
    Main function to extract and analyze key information from a PDF for investor evaluation.

    Parameters:
    pdf_path (str): Path to the input PDF file.
    """
    # Define the prompt for GPT analysis
    prompt_template = """
    Analyze the following company report text for key information relevant to an investor looking to evaluate the company's growth and performance.
    Focus on: future growth prospects, key changes in the business, important triggers or material information that could impact next year's earnings and growth.

    Text:
    {text}

    Provide a concise summary focusing on these investor-centric factors.
    """
    
    # Step 1: Extract text from the PDF
    raw_text = extract_text_from_pdf(pdf_path)
    if raw_text is None:
        return
    
    # Step 2: Clean the extracted text
    cleaned_text = clean_text(raw_text)
    
    # Step 3: Analyze the cleaned text using GPT
    analysis = analyze_text_with_gpt(cleaned_text, prompt_template)
    if analysis:
        print("Key Information Extracted for Investor Evaluation:\n")
        print(analysis)
    else:
        print("Failed to analyze the text with GPT.")

# Usage
pdf_path = "company_report.pdf"  # Path to your PDF file
main(pdf_path)

# GPT-PDF Analysis Project

This project extracts and analyzes key information from a PDF document using OpenAI's GPT-3.5 (or later) model. It targets investor-relevant insights, focusing on growth prospects, key changes, potential triggers, and factors affecting future earnings.

## Table of Contents
- [Project Overview](#project-overview)
- [Setup](#setup)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
- [Usage](#usage)
  - [Running in Jupyter Notebook](#running-in-jupyter-notebook)
  - [Running as a Python Script](#running-as-a-python-script)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Project Overview
The purpose of this project is to extract meaningful insights from company reports or similar PDF documents, which can assist investors in evaluating a company’s financial prospects. The project uses OpenAI’s GPT-3.5 model to summarize and highlight relevant sections of the document, such as:
- Future growth prospects
- Key business changes
- Potential triggers for investment
- Material factors affecting future earnings

## Setup

### Requirements
- Python 3.6+
- `openai` library
- `python-dotenv` (optional for `.env` file loading)
- `PyMuPDF` (for PDF parsing)

### Installation

1. **Clone the repository** (if using version control):
   ```bash
   git clone https://github.com/yourusername/GPT-PDF-Analysis.git
   cd GPT-PDF-Analysis

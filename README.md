# FMP Data
This project was created to facilitate the acquisition of data from [Financial Modeling Prep](https://site.financialmodelingprep.com/)


# Important Files & Directories

### main.py

The entry point for this project. It coordinates the flow of data by calling relevant functions from the 'src/' modules to download, process and store financial data from FMP.

### src/

The src/ directory contains modular functions for downloading, formatting and storing data from FMP. These functions are organized to handle specific tasks, making them reusable and easy to maintain.

# Requirements
To access data from FMP you will need an API Key. You can obtain a key by signing up on their [website](https://site.financialmodelingprep.com/). If you are running this repository in [Codespaces](https://github.com/features/codespaces), you can add the key as an environmental variable.

 **(Settings > Secrets and variables > Codespaces)** 

If you are running this repository locally, please review the .env.example file for further instructions.
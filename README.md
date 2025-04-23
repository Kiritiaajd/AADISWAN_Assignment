# AADISWAN Assignment

## Project Overview
The **AADISWAN Assignment** is a comprehensive financial analysis tool that integrates RBI circulars compliance checks, financial calculations (like Drawing Power), and an intuitive user interface using Streamlit. The project is divided into several components that handle data processing, calculations, and user interaction.

### Project Structure:

- **app/**: Contains the Streamlit app components.
  - **components/**: Includes individual components for displaying circulars, compliance status, Drawing Power (DP), MPBF, etc.
  - **main.py**: Main script to run the Streamlit application.
  - **style.css**: Custom CSS styles for the app.

- **backend/**: Handles the calculations and model inference logic.
  - **calculator/**: Contains specific files for financial calculations (e.g., DP and MPBF calculators).
  - **inference.py**: Logic for running inference with fine-tuned models.
  - **model_loader.py**: Handles model loading and setup.

- **data/**: Contains data files and scenario mappings for RBI circulars and MPBF calculations.
  - **rbi_guidelines_scenario_mappingcircular_1.json**
  - **rbi_guidelines_scenario_mapping_circular_2.json**
  - **Final_MPBF_Inputs_Table.xlsx**

- **docs/**: Documentation files for the project.
  - **MPBF_Calculation_Steps_and_Formulas.docx**: Detailed steps for MPBF calculation.

- **models/**: Contains your fine-tuned models.
  - **model3_gpt2/**: First version of the fine-tuned model.
  - **model3_gpt2_01/**: Second version of the fine-tuned model.

- **notebooks/**: Jupyter Notebooks for experimentation and model training.
  - **Model01_2.ipynb**
  - **Model2_3.ipynb**

- **requirements.txt**: List of Python dependencies required for the project.
- **run_app.py**: Entry point for running the Streamlit application.
- **setup.bat**: Windows setup script to create the virtual environment and install dependencies.
- **setup.sh**: Linux/macOS setup script to create the virtual environment and install dependencies.
- **template.py**: Template file for initializing modules.

## Setup Instructions

### Prerequisites:
1. Ensure you have Python 3.7+ installed.
2. Clone the repository to your local machine.

### Windows Setup:
1. Run the `setup.bat` script:
   ```bash
   setup.bat

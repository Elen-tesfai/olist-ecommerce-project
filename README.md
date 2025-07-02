# Olist E-commerce Data Cleaning Project

This project focuses on cleaning customer data from the Olist Brazilian e-commerce dataset. The original dataset contained various data quality issues such as missing values, duplicate records, and inconsistent formatting. The goal of this project is to clean the dataset for accurate analysis and modeling.

## Project Objectives

- Inspect and assess the quality of the raw customer data
- Remove duplicate records
- Handle missing values appropriately
- Standardize data types and formats
- Export a cleaned version of the dataset

## Tools and Libraries Used

- Python
- Pandas
- Jupyter Notebook or Visual Studio Code
- Git and GitHub

## Project Structure

```plaintext
olist-ecommerce-project/
│
├── data/
│ ├── olist_customers_dataset.csv         # Original raw customer dataset.
│ └── olist_customers_cleaned.csv         # Cleaned customer dataset after data cleaning.
│
├── computational_analysis_overview/
│ ├── histogram_customer_zip_code_prefix.png  # Histogram of ZIP code prefixes.
│ ├── box plot_customer_zip_code_prefix.png  # Box plot of ZIP code prefixes.
│ ├── bar plot_customer_state_distribution.png # Bar plot of customer state distribution.
│ └── density plot_customer_zip_code_prefix.png # Density plot of ZIP code prefixes.
│
├── notebooks/
│ └── data_inspection.ipynb              # Jupyter notebook for data inspection and cleaning.
│
├── data_inspection.py                   # Python script for data inspection and cleaning.
├── README.md                            # This file.
├── requirements.txt                     # List of dependencies required to run the project.
├── .gitignore                           # Specifies files to ignore in version control.
└── env/                                  # Virtual environment directory (optional).

```
## Project Description

This project involves the **cleaning and analysis** of the Olist E-commerce dataset. The data is cleaned, preprocessed, and analyzed to derive useful insights regarding customer demographics, ZIP code prefixes, and state distributions. Several visualizations, such as histograms, box plots, and density plots, have been generated to better understand the data distribution.

## Folder Breakdown

### `data/`
- **`olist_customers_dataset.csv`**: This is the **raw customer data** before cleaning.
- **`olist_customers_cleaned.csv`**: The **cleaned version** of the customer data after removing duplicates, handling missing values, and addressing any data inconsistencies.

### `computational_analysis_overview/`
- **`histogram_customer_zip_code_prefix.png`**: A **histogram** showing the distribution of customer ZIP code prefixes.
- **`box_plot_customer_zip_code_prefix.png`**: A **box plot** visualizing the spread and distribution of customer ZIP code prefixes.
- **`bar_plot_customer_state_distribution.png`**: A **bar plot** representing the distribution of customers across different states.
- **`density_plot_customer_zip_code_prefix.png`**: A **density plot** of customer ZIP code prefixes for a smoother visualization of the distribution.

### `notebooks/`
- **`data_inspection.ipynb`**: A **Jupyter notebook** used for performing data inspection and cleaning tasks, such as identifying missing values, duplicates, and outliers.

### Scripts and Other Files
- **`data_inspection.py`**: A **Python script** that mirrors the work done in the Jupyter notebook for data inspection and cleaning, potentially used for automation or larger-scale projects.
- **`README.md`**: This **Markdown file** describing the project, data structure, and other essential information.
- **`requirements.txt`**: A text file listing all the **dependencies** needed to run the project (e.g., pandas, numpy, matplotlib, etc.).
- **`.gitignore`**: A file specifying which files or directories should be ignored by Git (e.g., virtual environments, compiled files).
- **`env/`**: This optional directory contains the **virtual environment** for the project (if using one).

## Setup Instructions

1. Clone the repository:

## Installation

To get a copy of this project locally, run the following commands:

```bash
git clone https://github.com/Elen-tesfai/olist-ecommerce-project.git
cd olist-ecommerce-project
```
2. (Optional) Create and activate a virtual environment:

## Setup Virtual Environment

```bash
python -m venv env
```
# Activate on Windows
env\Scripts\activate

# Activate on macOS/Linux
source env/bin/activate

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Run the cleaning script:
```bash
python data_inspection.py
```

  ## Conclusion

In this project, the Olist e-commerce dataset was cleaned and preprocessed to improve data quality for further analysis. The dataset had several data issues, such as missing values and duplicate records, which were successfully addressed. The cleaned dataset is now ready for advanced analysis or machine learning models.

The data inspection revealed interesting patterns, such as ZIP code distribution variations and state-level customer density, which can provide valuable insights for businesses looking to optimize their marketing strategies.

## References

1. Olist E-commerce dataset. (n.d.). Retrieved from [https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).

2. Smith, J., & Johnson, L. (2020). Data Science for E-commerce. *Journal of Business Analytics, 34*(2), 45-58. [https://doi.org/10.1016/j.jba.2020.03.005](https://doi.org/10.1016/j.jba.2020.03.005).

3. Tesfai, E. (2025). Olist E-commerce Data Analysis Project. Retrieved from [https://github.com/Elen-tesfai/olist-ecommerce-project](https://github.com/Elen-tesfai/olist-ecommerce-project).

## Author

Elen Tesfai  
Data Analytics Graduate Student  
Northwest Missouri State University  
Class of 2025  
Email: [S567983@nwmissouri.edu](mailto:S567983@nwmissouri.edu)

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

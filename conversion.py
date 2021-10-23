import pandas as pd

def excelToCSV(excelFile, csvFile):
    """Does a conversion from excel sheets to CSV file."""
    file = pd.DataFrame(pd.read_excel(excelFile, "Exchange Trades"))
    file.to_csv("wazirX_Report.csv", header=True)
    csv = pd.DataFrame(pd.read_csv(csvFile))
    print(f"Converted {excelFile} to CSV {csvFile}")
    return csv

# excelToCSV("example.xlsx", "example.csv")
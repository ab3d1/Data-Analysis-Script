# data-analysis/reconciliation.py
import pandas as pd
from datetime import datetime

def perform_reconciliation():
    # Sample transaction data
    transactions = pd.DataFrame({
        'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'amount': [1000, 2500, 1750],
        'status': ['processed', 'pending', 'processed']
    })

    # Sample ledger data
    ledger = pd.DataFrame({
        'date': ['2023-01-01', '2023-01-03'],
        'amount': [1000, 1750],
        'confirmed': [True, True]
    })

    # Reconciliation check
    merged = pd.merge(transactions, ledger, on=['date', 'amount'], how='outer', indicator=True)
    discrepancies = merged[merged['_merge'] != 'both']

    # Generate report
    report = f"""
    RECONCILIATION REPORT ({datetime.now().date()})
    --------------------------------------------
    Total Transactions: {len(transactions)}
    Verified Transactions: {len(ledger)}
    Discrepancies Found: {len(discrepancies)}
    
    Discrepancy Details:
    {discrepancies.to_markdown()}
    """
    
    with open('reconciliation_report.md', 'w') as f:
        f.write(report)
    
    print("Reconciliation complete. Report generated.")

if __name__ == "__main__":
    perform_reconciliation()

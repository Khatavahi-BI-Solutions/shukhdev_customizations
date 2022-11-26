def validate(doc,method):
    if doc.purchase_expense_account and not doc.ignore_purchase_expense_account:
        for row in doc.items:
            row.expense_account = doc.purchase_expense_account
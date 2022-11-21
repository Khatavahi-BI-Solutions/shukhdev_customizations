def validate(doc,method):
    if doc.sales_income_account:
        for row in doc.items:
            row.income_account = doc.sales_income_account
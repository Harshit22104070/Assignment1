gross_income=int(input("Enter the income"))


dependents=int(input("Enter the number of dependents"))

standard_deduction=10000

Taxable_income=gross_income-standard_deduction-(dependents*3000)

Tax=Taxable_income*20/100
print(Tax)
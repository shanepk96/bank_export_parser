import csv
import pandas


my_data = pandas.read_csv('Transaction_Export_01.02.2019_19.18.csv', header='infer')


columns_to_drop = [" Posted Transactions Date",
                   "Posted Account",
                   " Description2",
                   " Description3",
                   "Balance",
                   "Posted Currency",
                   "Local Currency Amount",
                   "Local Currency"]

debit_columns_to_drop = [" Credit Amount",
                         "Transaction Type"]
credit_columns_to_drop = [" Debit Amount",
                          "Transaction Type"]

my_data.drop(columns_to_drop, axis=1, inplace=True)
print(my_data.head())
my_data.sort_values(by='Transaction Type', axis=0, inplace=True)
my_data.set_index(keys='Transaction Type', drop=False, inplace=True)
print(my_data.head())

transaction_type = my_data['Transaction Type'].unique().tolist()

credit = my_data.loc[my_data.index == 'Credit']
credit.drop(credit_columns_to_drop, axis=1, inplace=True)
print(credit.head())
credit_output = credit.groupby(by=" Description1").sum()
print(credit_output)

debit = my_data.loc[my_data.index == 'Debit']
debit.drop(debit_columns_to_drop, axis=1, inplace=True)
debit_output = debit.groupby(by=" Description1").sum()
print(debit_output)

pandas.concat([debit_output, credit_output], axis=1, sort=False).to_csv('output.csv')

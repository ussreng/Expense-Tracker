def show_menu():
  print("\n============== Personal Expense Tracker===============")
  print('1. Add Expense')
  print('2. View All Expenses')
  print('3. View Summary')
  print('4. Delete Expense')
  print('5. Exit')

# To input expense details and save to csv
import csv
from datetime import datetime
def add_expense():
  date=datetime.now().strftime("%Y-%m-%d")
  category=input("Enter Category (Food, Travel, etc.): ")
  amount=float(input('Enter amount:'))
  description=input('Enter description: ')

  with open('expenses.csv',mode='a',newline='') as file:
    writer=csv.writer(file)
    writer.writerow([date, category, amount, description])
  print('Expense added Successfully! U+2705')  

# View Expenses
import pandas as pd
def view_expenses():
  try:
    df=pd.read_csv('expenses.csv',names=['Date', 'Category', 'Amount', 'Description']) 
    print('\n=== All Expenses ===')
    print(df)
  except FileNotFoundError:
    print('\u274c No expenses found. Please add one first!')

# View Summary
def show_summary():
  df=pd.read_csv('expenses.csv',names=['Date', 'Category', 'Amount', 'Description'])
  print('\n=== Summary ===')
  print('Total Spent:',df['Amount'].sum())
  print('\nCategory-wise Spending:\n',df.groupby('Category')['Amount'].sum())

# Add Visualization
import matplotlib.pyplot as plt
def plot_summary():
  df=pd.read_csv('expenses.csv',names=['Date', 'Category', 'Amount', 'Description'])
  grouped=df.groupby('Category')['Amount'].sum()
  grouped.plot(kind='bar',title='Expenses by Category')
  plt.xlabel('Category')
  plt.ylabel('Total Spent') 
  plt.show() 

# Delete Expense
def delete_expense():
  try:
    df=pd.read_csv('expenses.csv',names=['Date', 'Category', 'Amount', 'Description'])
    print('\n=== All Expenses ===')
    index_to_delete=int(input('\nEnter the index of the expense to delete: '))
    if index_to_delete in df.index:
      df=df.drop(index_to_delete)
      df.to_csv('expenses.csv',header=False, index=False)
      print('Expense deleted successfully!')
    else:
      print('Invalid index!')
  except FileNotFoundError:
    print('No Expenses Found. Please add it first!')

  except ValueError:
    print('Please enter a valid value')                

# Integrate Everything
while True:
  show_menu()
  choice=input('Enter your choice: ')
  if choice=="1":
    add_expense()
  elif choice=="2":
    view_expenses()
  elif choice=="3":
    show_summary()
    plot_summary()
  elif choice=="4":
    delete_expense()  
  elif choice=="5":
    print('Goodbye 👋')  
    break
  else:
    print('Invalid choice! Please try again.')      
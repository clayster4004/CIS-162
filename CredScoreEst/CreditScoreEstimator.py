"""Project 1 - Credit Score Estimator

Clay Beal
I certify that this work was done in accordance with
GV academic honesty policies.

Fall, 2022"""

# Printing out a header for the Credit Score Estimator
print(f'############################')
print(f'## Credit Score Estimator ##')
print(f'############################')
print()

# Constant for baseline credit score
BASELINE_SCORE = 500

# Variables for each aspect of the one's credit score
payment_history = 0
debt = 0
credit_history_len = 0
new_credit = 0
credit_cards = 0
score = 0
overall_score = 0


# Ask the user about previous credit history
payment_history = input(f'How many months since a negative '
                        f'report has been made? (N/A for never) -> ')

debt = input(f'What is your current balance of debt? '
             f'(N/A for no accounts) -> ')

credit_history_len = int(input(f'How many months have you had credit? -> '))

new_credit = int(input(f'How many new credit attempts have you done '
                       f'in the last 6 months? -> '))

credit_cards = int(input(f'How many credit accounts do you have that '
                         f'are credit cards? -> '))


# Calculate the credit score for each section
# Calculate payment history score
if payment_history.lower() != 'n/a':
    payment_history = int(payment_history)
    if payment_history <= 5:
        score = 10
    elif payment_history <= 11:
        score = 15
    elif payment_history <= 23:
        score = 25
    else:
        score = 55
else:
    score = 75


# Calculates the balance of debt score
if debt.lower() != 'n/a':
    debt = int(debt)
    if debt == 0:
        score += 55
    elif debt <= 99:
        score += 65
    elif debt <= 499:
        score += 50
    elif debt <= 749:
        score += 40
    elif debt <= 999:
        score += 25
    else:
        score += 15
else:
    score += 30


# Calculates credit history length score
if credit_history_len < 12:
    score += 12
elif credit_history_len <= 23:
    score += 35
elif credit_history_len <= 47:
    score += 60
else:
    score += 75


# Calculates number of new credit attempts in the last 6 months score
if new_credit == 0:
    score += 70
elif new_credit == 1:
    score += 60
elif new_credit == 2:
    score += 45
elif new_credit == 3:
    score += 25
else:
    score += 20


# Calculates number of credit cards score
if credit_cards == 0:
    score += 15
elif credit_cards == 1:
    score += 25
elif credit_cards == 2:
    score += 50
elif credit_cards == 3:
    score += 65
else:
    score += 50


# Calculates one's overall credit score
overall_score = BASELINE_SCORE + score

print(f'Your estimated credit score is {overall_score}.')

# Calculate the approval criteria for loans
if overall_score > 650:

    if type(payment_history) is not str:
        if (new_credit == 0) and (payment_history > 12) and (overall_score > 650):
            print('You are approved for a loan $500-$2000.')

    elif (type(payment_history is str)) and (overall_score > 800):
        print('You are approved for a loan $500-$10000.')
    elif (new_credit == 0) and (type(payment_history is str)) and (overall_score > 700):
        print('You are approved for a loan $500-$5000.')
    else:
        print(f'I\'m sorry you do not qualify for a loan.')

else:
    print(f'I\'m sorry you do not qualify for a loan.')

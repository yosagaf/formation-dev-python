import re

user_password = input("Saisissez un mot de passe: ")
score = 0
total_len = len(user_password)

# functions


def NbCMaj(password):

    match = re.findall(r"[A-Z]", password)
    return len(match)


def NbCMin(password):

    match = re.findall(r"[a-z]", password)
    return len(match)


def NbCAlpha(password):

    match = re.findall(r"[0-9]", password)
    match2 = re.findall(r"\W", password)
    match3 = re.findall(r"_", password)
    return(len(match)+len(match2)+len(match3))


def LongMaj(password):

    pattern = ["[A-Z]+"]
    for p in pattern:
        match = re.findall(p, password)
        print(match)


def LongMin(password):
    pattern = ["[a-z]+"]

    for p in pattern:
        match = re.findall(p, password)
        print(match)


# score calcul

score_step_one = (total_len - NbCMin(user_password)) * 3
score_step_two = (total_len - NbCMaj(user_password)) * 2
print(total_len * 4 + score_step_one +
      score_step_two + NbCAlpha(user_password)*5)

print(NbCAlpha(user_password))
LongMaj(user_password)

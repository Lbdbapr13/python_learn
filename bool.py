#Python has a type of a variable called bool it has 2 values: true & false

x=True
print(x)
print(type(x))

#def is stand for definition
# "_" tanda menggatikan spasi dalam python
def can_run_for_president(age):
    """can someone of the given age run for president in Indonesia?"""
    #the Indonesia constitution says you must at least 40 years old
    return age >= 40
print("Can a 19 years old run for president?", can_run_for_president(19))
print("Can a 41 years old run for president?", can_run_for_president(41))

#contoh kasus
def can_vote_in_elections(age):
    """can someone of the given age vote in election """
    #the Indonesia constitution says you must at least 17 years old
    return age>= 17
print("can a 16 years old vote in election?",can_vote_in_elections(16))
print("can a 18 years old vote in election?",can_vote_in_elections(18))

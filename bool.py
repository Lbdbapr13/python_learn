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

# n % 2 == 1, it's one syntax means "True"
def is_odd(n):
    return (n % 2)== 1 
print("is 100 odd?", is_odd(100))
print("is -1 odd?", is_odd(-1))

print (3.0 == 3)

#contoh kasus
def can_run_for_president(age, is_natural_born_citizen):
    """Can someone of the given age and citizenship status run for president in the Indonesia?"""
    #The Indonesia Constitution says you must be a natual born citizen *and* at least 40 years old
    return is_natural_born_citizen and (age>=40)
print(can_run_for_president(20, True))
print(can_run_for_president(40, False))
print(can_run_for_president(35, True))
print(can_run_for_president(40, True))

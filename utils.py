"""
first file in the repo
"""

def square(x):
    return x*x

"""
Ora creiamo il main in modo che il file da solo faccia qualcosa!

Se stai esguendo questo file dal command line: fai questo;
Se altrimenti lo stai importando, non fare la seguent cosa
"""

if __name__ == "__main__":
    print(square(5))
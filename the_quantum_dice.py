from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.providers.ibmq import least_busy
import msvcrt as m
from colorama import Fore, init

init()




def wait():
    m.getch()

def run_quantum_circuit():
    provider= IBMQ.get_provider(hub="ibm-q")
    backend = least_busy(provider.backends(filters=
    lambda x: x.configuration().n_qubits >= 2
    and not x.configuration().simulator 
    and x.status().operational==True))

    qc = QuantumCircuit(3, 3) 

    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.measure(0,0)
    qc.measure(1,1)
    qc.measure(2,2)

    job = execute(qc, backend, shots=1)



    counts = job.result().get_counts()
    measured_bits = max(counts, key=counts.get)
    return measured_bits
    
def roll_dice():
    results= run_quantum_circuit()

    if results=="100":
        print(" ------- ")
        print("|       |")
        print("|   o   |")
        print("|       |")
        print(" ------- ")
        print("")
        print("[+] You rolled a 1")
        

    elif results=="010":
        print(" ------- ")
        print("|o      |")
        print("|       |")
        print("|      o|")
        print(" ------- ")
        print("")
        print("[+] You rolled a 2")
        

    elif results=="001":
        print(" ------- ")
        print("|o      |")
        print("|   o   |")
        print("|      o|")
        print(" ------- ")
        print("")
        print("[+] You rolled a 3")
        
    elif results=="110":
        print(" ------- ")
        print("|o     o|")
        print("|       |")
        print("|o     o|")
        print(" ------- ")
        print("")
        print("[+] You rolled a 4")
        
    elif results=="101":
        print(" ------- ")
        print("|o     o|")
        print("|   o   |")
        print("|o     o|")
        print(" ------- ")
        print("")
        print("[+] You rolled a 5")
        
    elif results=="011":
        print(" ------- ")
        print("|o  o  o|")
        print("|       |")
        print("|o  o  o|")
        print(" ------- ")
        print("")
        print("[+] You rolled a 6")
    else:
        roll_dice()
        
        


print("")
print("")
print("▀█▀ █ █ █▀▀   █▀█ █ █ ▄▀█ █▄ █ ▀█▀ █ █ █▀▄▀█   █▀▄ █ █▀▀ █▀▀")
print(" █  █▀█ ██▄   ▀▀█ █▄█ █▀█ █ ▀█  █  █▄█ █ ▀ █   █▄▀ █ █▄▄ ██▄")
print("")
print("For the ultimate gambling experience!")
print("")


print("[+] Loading IBM account...")
try:
    IBMQ.load_account()
except :
    print(Fore.RED+"[-] IBM account failed to load"+Fore.WHITE)
    IBMQ.save_account(input("Please enter your API token > "))
    IBMQ.load_account()

print(Fore.LIGHTGREEN_EX+"[+] IBM account loaded successfully"+Fore.WHITE)

while True:
    print("")
    print("[+] Press any key to roll the dice")
    wait()
    print("[+] Running quantum circuit, this may take a while...\n")
    roll_dice()


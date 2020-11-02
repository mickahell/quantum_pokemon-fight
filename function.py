import math
from qiskit import Aer, QuantumCircuit, execute, IBMQ


def quantum_fight(psi):
    # Init Qasm simulator backend
    qasm = Aer.get_backend('qasm_simulator')

    # Init Real Quantum computer
    IBMQ.load_account()
    provider = IBMQ.get_provider('ibm-q')
    quantum_computer = provider.get_backend('ibmq_16_melbourne')

    backend_sim = qasm  # Choose your backend : <quantum_computer> or <qasm>

    qc = QuantumCircuit(1, 1)

    qc.rx(math.pi * psi, 0)
    qc.measure(0, 0)

    job = execute(qc, backend_sim, shots=1, memory=True)
    result_job = job.result().get_memory()
    to_return = int(result_job[0], 2)

    return to_return


def calcul_dommage(attaq, pokemon_att, pokemon_def):
    quantum_precision = quantum_fight(attaq.precision)
    if quantum_precision == 1:
        STAB = 1
        RESISTANCE = 1
        CRIT = 1
        if attaq.type in pokemon_att.type:
            STAB = 1.5
        if attaq.type.name in pokemon_def.type.faiblesse:
            RESISTANCE = 2
            print("C'est super efficace !")
        elif attaq.type.name in pokemon_def.type.resistance:
            RESISTANCE = 0.5
            print("Ce n'est pas très efficace !")
        elif attaq.type.name in pokemon_def.type.imunite:
            RESISTANCE = 0
            print("{} n'est pas affecté par cette attaque !".format(pokemon_def.name))

        quantum_crit = quantum_fight(0.0417)
        if quantum_crit == 1:
            CRIT = 1.5
            print("coup critique !")

        degats = ((((100 * 0.4 + 2) * pokemon_att.points_attaque * attaq.puissance) / (
                pokemon_def.points_defence * 50)) + 2) * STAB * RESISTANCE * CRIT
    else:
        print("{} a loupé son attaque !".format(pokemon_att.name))
        degats = 0

    return degats


def action_attaque(attaque, pokemon_att, pokemon_def):
    pokemon_att.action = 0
    print("{} utilise {}".format(pokemon_att.name, attaque.name))
    pokemon_def.degats = pokemon_def.degats + calcul_dommage(attaque, pokemon_att, pokemon_def)
    if pokemon_def.degats >= pokemon_def.pv:
        pokemon_def.status = 0
        print("{} est KO".format(pokemon_def.name))
        pokemon_def.action == 0

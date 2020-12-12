from qiskit import Aer, QuantumCircuit, QuantumRegister, ClassicalRegister, execute, IBMQ
from qiskit.tools.monitor import job_monitor


def quantum_ia(attaquant, defenseur, qc_type, backend_sim):
    def diffuser(qc):
        qc.h(qram_q)
        qc.z(qram_q)
        qc.cz(qram_q[0], qram_q[1])
        qc.h(qram_q)

    def or_faib(qc):
        qc.barrier()
        qc.cx(advfaib_q[0], faibcheck_q[0])
        qc.cx(advfaib_q[1], faibcheck_q[0])
        qc.ccx(advfaib_q[1], advfaib_q[0], faibcheck_q[0])
        qc.barrier()

    def or_resist(qc):
        qc.barrier()
        qc.cx(advresist_q[0], resistcheck_q[0])
        qc.cx(advresist_q[1], resistcheck_q[0])
        qc.ccx(advresist_q[1], advresist_q[0], resistcheck_q[0])
        qc.barrier()

    def immunite(defenseur, qc):
        for i in defenseur.types:
            if i.imunite[0] != "None":
                qc.cx(i.imunite[0].qubit, immu_q)

    def calcul_resist(defenseur, qc):
        resist_compteur = 0
        for i in defenseur.types:
            for u in i.resistance:
                if i.resistance[0] != "None":
                    qc.cx(u.qubit, advresist_q[resist_compteur])
            resist_compteur += 1

    def calcul_faib(defenseur, qc):
        faib_compteur = 0
        for i in defenseur.types:
            for u in i.faiblesse:
                qc.cx(u.qubit, advfaib_q[faib_compteur])
            faib_compteur += 1

    def qram_att(attaquant, qc):
        # 00
        qc.x(qram_q)
        qc.ccx(qram_q[0], qram_q[1], attaquant.attaques[0].type.qubit)
        qc.x(qram_q)
        # 01
        qc.x(qram_q[1])
        qc.ccx(qram_q[0], qram_q[1], attaquant.attaques[1].type.qubit)
        qc.x(qram_q[1])
        # 10
        qc.x(qram_q[0])
        qc.ccx(qram_q[0], qram_q[1], attaquant.attaques[2].type.qubit)
        qc.x(qram_q[0])
        # 11
        qc.ccx(qram_q[0], qram_q[1], attaquant.attaques[3].type.qubit)

    qram_q = QuantumRegister(2, 'attaques')
    qc_qram = QuantumCircuit(qram_q)
    advfaib_q = QuantumRegister(2, 'faiblesse_map')
    faibcheck_q = QuantumRegister(1, 'check_faiblesse')
    advresist_q = QuantumRegister(2, 'resistance_map')
    resistcheck_q = QuantumRegister(1, 'check_resistance')
    immu_q = QuantumRegister(1, 'immunite')
    qc_faib = QuantumCircuit(advfaib_q, faibcheck_q, advresist_q, resistcheck_q, immu_q)
    check_q = QuantumRegister(1, 'check')
    out_q = QuantumRegister(1, 'flag')
    c = ClassicalRegister(2, 'c')
    qc_c = QuantumCircuit(check_q, out_q, c)

    # Circuit final
    qc = qc_qram + qc_type + qc_faib + qc_c

    # Init
    qc.h(qram_q)
    qc.x(immu_q)
    qc.x(resistcheck_q)
    qc.x(out_q)
    qc.h(out_q)
    qc.barrier()

    for i in range(1):
        # Compute
        qram_att(attaquant, qc)
        calcul_faib(defenseur, qc)
        calcul_resist(defenseur, qc)
        or_faib(qc)
        or_resist(qc)
        immunite(defenseur, qc)

        # Flag
        qc.mcx([faibcheck_q, resistcheck_q, immu_q], check_q)
        qc.cx(check_q, out_q)
        qc.mcx([faibcheck_q, resistcheck_q, immu_q], check_q)

        # Uncompute
        immunite(defenseur, qc)
        or_resist(qc)
        or_faib(qc)
        calcul_resist(defenseur, qc)
        calcul_faib(defenseur, qc)
        qram_att(attaquant, qc)

        # Apply generic diffuser
        diffuser(qc)

    qc.measure(qram_q, c)

    # Interprete result
    job = execute(qc, backend_sim, shots=512, memory=True)
    result_job = job.result().get_counts()
    result_memory = job.result().get_memory()

    if len(result_job) == 1:
        to_return = int(result_memory[0], 2)
    else:
        to_return = max(result_job, key=result_job.get)
        to_return = int(to_return, 2)

    return to_return

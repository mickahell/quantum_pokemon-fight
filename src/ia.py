from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute


def quantum_attaq(attacker, defender, qc_type, backend_sim):
    def diffuser(qc):
        qc.h(qram_q)
        qc.z(qram_q)
        qc.cz(qram_q[0], qram_q[1])
        qc.h(qram_q)

    def or_weak(qc):
        qc.barrier()
        qc.cx(advweak_q[0], weakcheck_q[0])
        qc.cx(advweak_q[1], weakcheck_q[0])
        qc.ccx(advweak_q[1], advweak_q[0], weakcheck_q[0])
        qc.barrier()

    def or_resist(qc):
        qc.barrier()
        qc.cx(advresist_q[0], resistcheck_q[0])
        qc.cx(advresist_q[1], resistcheck_q[0])
        qc.ccx(advresist_q[1], advresist_q[0], resistcheck_q[0])
        qc.barrier()

    def immunite(defender, qc):
        for i in defender.types:
            if i.imunite[0] != "None":
                qc.cx(i.imunite[0].qubit, immu_q)

    def calcul_resist(defender, qc):
        resist_count = 0
        for i in defender.types:
            for u in i.resistance:
                if i.resistance[0] != "None":
                    qc.cx(u.qubit, advresist_q[resist_count])
            resist_count += 1

    def calcul_weak(defender, qc):
        weak_count = 0
        for i in defender.types:
            for u in i.weakness:
                if i.weakness[0] != "None":
                    qc.cx(u.qubit, advweak_q[weak_count])
            weak_count += 1

    def qram_att(attacker, qc):
        # 00
        qc.x(qram_q)
        qc.ccx(qram_q[0], qram_q[1], attacker.attacks[0].type.qubit)
        qc.x(qram_q)
        # 01
        qc.x(qram_q[1])
        qc.ccx(qram_q[0], qram_q[1], attacker.attacks[1].type.qubit)
        qc.x(qram_q[1])
        # 10
        qc.x(qram_q[0])
        qc.ccx(qram_q[0], qram_q[1], attacker.attacks[2].type.qubit)
        qc.x(qram_q[0])
        # 11
        qc.ccx(qram_q[0], qram_q[1], attacker.attacks[3].type.qubit)

    qram_q = QuantumRegister(2, "attacks")
    qc_qram = QuantumCircuit(qram_q)
    advweak_q = QuantumRegister(2, "weakness_map")
    weakcheck_q = QuantumRegister(1, "check_weakness")
    advresist_q = QuantumRegister(2, "resistance_map")
    resistcheck_q = QuantumRegister(1, "check_resistance")
    immu_q = QuantumRegister(1, "immunity")
    qc_weak = QuantumCircuit(advweak_q, weakcheck_q, advresist_q, resistcheck_q, immu_q)
    check_q = QuantumRegister(1, "check")
    out_q = QuantumRegister(1, "flag")
    c = ClassicalRegister(2, "c")
    qc_c = QuantumCircuit(check_q, out_q, c)

    # Circuit final
    qc = qc_qram + qc_type + qc_weak + qc_c

    # Init
    qc.h(qram_q)
    qc.x(immu_q)
    qc.x(resistcheck_q)
    qc.x(out_q)
    qc.h(out_q)
    qc.barrier()

    for i in range(1):
        # Compute
        qram_att(attacker, qc)
        calcul_weak(defender, qc)
        calcul_resist(defender, qc)
        or_weak(qc)
        or_resist(qc)
        immunite(defender, qc)

        # Flag
        qc.mcx([weakcheck_q, resistcheck_q, immu_q], check_q)
        qc.cx(check_q, out_q)
        qc.mcx([weakcheck_q, resistcheck_q, immu_q], check_q)

        # Uncompute
        immunite(defender, qc)
        or_resist(qc)
        or_weak(qc)
        calcul_resist(defender, qc)
        calcul_weak(defender, qc)
        qram_att(attacker, qc)

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


def quantum_action(defender, attacker, qc_type, backend_sim):
    def diffuser(qc):
        qc.h(qram_q)
        qc.z(qram_q)
        qc.cz(qram_q[0], qram_q[1])
        qc.h(qram_q)

    def immunite(defender, qc):
        for i in defender.types:
            if i.imunite[0] != "None":
                qc.cx(i.imunite[0].qubit, immu_q)

    def calcul_resist(defender, qc):
        resist_count = 0
        for i in defender.types:
            for u in i.resistance:
                if i.resistance[0] != "None":
                    qc.cx(u.qubit, resist_q[resist_count])
            resist_count += 1

    def calcul_weak(defender, qc):
        weak_count = 0
        for i in defender.types:
            for u in i.weakness:
                if i.weakness[0] != "None":
                    qc.cx(u.qubit, weak_q[weak_count])
            weak_count += 1

    def or_weak(qc):
        qc.barrier()
        qc.cx(weak_q[0], weakcheck_q[0])
        qc.cx(weak_q[1], weakcheck_q[0])
        qc.ccx(weak_q[1], weak_q[0], weakcheck_q[0])
        qc.barrier()

    def qram_att(attacker, qc):
        # 00
        qc.x(qram_q)
        qc.ccx(qram_q[0], qram_q[1], attacker.types[0].qubit)
        qc.x(qram_q)
        # 11
        if len(attacker.types) > 1:
            qc.ccx(qram_q[0], qram_q[1], attacker.types[1].qubit)

    qram_q = QuantumRegister(2, "attacks")
    qc_qram = QuantumCircuit(qram_q)

    weak_q = QuantumRegister(2, "weakness_map")
    weakcheck_q = QuantumRegister(1, "check_weakness")
    resist_q = QuantumRegister(2, "resistance_map")
    immu_q = QuantumRegister(1, "immunity")
    qc_weak = QuantumCircuit(weak_q, weakcheck_q, resist_q, immu_q)

    check_q = QuantumRegister(1, "check")
    out_q = QuantumRegister(1, "flag")
    c = ClassicalRegister(2, "c")
    qc_c = QuantumCircuit(check_q, out_q, c)

    # Circuit final
    qc = qc_qram + qc_type + qc_weak + qc_c

    # Init
    qc.h(qram_q)
    qc.x(resist_q)
    qc.x(immu_q)
    qc.x(out_q)
    qc.h(out_q)
    qc.barrier()

    for i in range(1):
        # Compute
        qram_att(attacker, qc)
        calcul_weak(defender, qc)
        calcul_resist(defender, qc)
        or_weak(qc)
        immunite(defender, qc)

        # Flag
        qc.mcx([weakcheck_q, resist_q[0], resist_q[1], immu_q], check_q)
        qc.cx(check_q, out_q)
        qc.mcx([weakcheck_q, resist_q[0], resist_q[1], immu_q], check_q)

        # Uncompute
        immunite(defender, qc)
        or_weak(qc)
        calcul_resist(defender, qc)
        calcul_weak(defender, qc)
        qram_att(attacker, qc)

        # Apply generic diffuser
        diffuser(qc)

    qc.measure(qram_q, c)

    # Interprete result
    job = execute(qc, backend_sim, shots=512, memory=True)
    result_job = job.result().get_counts()

    if len(result_job) == 1:
        to_return = 1
    else:
        to_return = 0

    return to_return


def quantum_switch(attacker, defender, qc_type, backend_sim):
    def diffuser(nqubits):
        qc = QuantumCircuit(nqubits)
        for qubit in range(nqubits):
            qc.h(qubit)
        for qubit in range(nqubits):
            qc.x(qubit)
        qc.h(nqubits - 1)
        qc.mct(list(range(nqubits - 1)), nqubits - 1)
        qc.h(nqubits - 1)
        for qubit in range(nqubits):
            qc.x(qubit)
        for qubit in range(nqubits):
            qc.h(qubit)
        U_s = qc.to_gate()
        U_s.name = "$U_s$"
        return qc

    def immunite(defender, qc):
        for i in defender.types:
            if i.imunite[0] != "None":
                qc.cx(i.imunite[0].qubit, immu_q)

    def calcul_resist(defender, qc):
        resist_count = 0
        for i in defender.types:
            for u in i.resistance:
                if i.resistance[0] != "None":
                    qc.cx(u.qubit, resist_q[resist_count])
            resist_count += 1

    def calcul_weak(defender, qc):
        weak_count = 0
        for i in defender.types:
            for u in i.weakness:
                if i.weakness[0] != "None":
                    qc.cx(u.qubit, weak_q[weak_count])
            weak_count += 1

    def or_weak(qc):
        qc.barrier()
        qc.cx(weak_q[0], weakcheck_q[0])
        qc.cx(weak_q[1], weakcheck_q[0])
        qc.ccx(weak_q[1], weak_q[0], weakcheck_q[0])
        qc.barrier()

    def qram_att(attacker, qc):
        # 0
        qc.x(qrampoke_q)
        # 00 0
        qc.x(qramatt_q)
        qc.mcx(
            [qrampoke_q[0], qramatt_q[0], qramatt_q[1]],
            attacker[0].attacks[0].type.qubit,
        )
        qc.x(qramatt_q)
        # 01 0
        qc.x(qramatt_q[1])
        qc.mcx(
            [qrampoke_q[0], qramatt_q[0], qramatt_q[1]],
            attacker[0].attacks[1].type.qubit,
        )
        qc.x(qramatt_q[1])
        # 10 0
        qc.x(qramatt_q[0])
        qc.mcx(
            [qrampoke_q[0], qramatt_q[0], qramatt_q[1]],
            attacker[0].attacks[2].type.qubit,
        )
        qc.x(qramatt_q[0])
        # 11 0
        qc.mcx(
            [qrampoke_q[0], qramatt_q[0], qramatt_q[1]],
            attacker[0].attacks[3].type.qubit,
        )
        qc.x(qrampoke_q)
        # 1
        if len(attacker) > 1:
            # 00 1
            qc.x(qramatt_q)
            qc.mcx(
                [qrampoke_q[0], qramatt_q[0], qramatt_q[1]],
                attacker[1].attacks[0].type.qubit,
            )
            qc.x(qramatt_q)
            # 01 1
            qc.x(qramatt_q[1])
            qc.mcx(
                [qrampoke_q[0], qramatt_q[0], qramatt_q[1]],
                attacker[1].attacks[1].type.qubit,
            )
            qc.x(qramatt_q[1])
            # 10 1
            qc.x(qramatt_q[0])
            qc.mcx(
                [qrampoke_q[0], qramatt_q[0], qramatt_q[1]],
                attacker[1].attacks[2].type.qubit,
            )
            qc.x(qramatt_q[0])
            # 11 1
            qc.mcx(
                [qrampoke_q[0], qramatt_q[0], qramatt_q[1]],
                attacker[1].attacks[3].type.qubit,
            )

    qrampoke_q = QuantumRegister(1, "team")
    qramatt_q = QuantumRegister(2, "attacks")
    qc_qram = QuantumCircuit(qrampoke_q, qramatt_q)

    weak_q = QuantumRegister(2, "weakness_map")
    weakcheck_q = QuantumRegister(1, "check_weakness")
    resist_q = QuantumRegister(2, "resistance_map")
    immu_q = QuantumRegister(1, "immunite")
    qc_weak = QuantumCircuit(weak_q, weakcheck_q, resist_q, immu_q)

    check_q = QuantumRegister(1, "check")
    out_q = QuantumRegister(1, "flag")
    c = ClassicalRegister(1, "c")
    qc_c = QuantumCircuit(check_q, out_q, c)

    # Circuit final
    qc = qc_qram + qc_type + qc_weak + qc_c

    # Init
    qc.h(qrampoke_q)
    qc.h(qramatt_q)
    qc.x(resist_q)
    qc.x(immu_q)
    qc.x(out_q)
    qc.h(out_q)
    qc.barrier()

    for i in range(1):
        # Compute
        qram_att(attacker, qc)
        calcul_weak(defender, qc)
        calcul_resist(defender, qc)
        or_weak(qc)
        immunite(defender, qc)

        # Flag
        qc.mcx([weakcheck_q, resist_q[0], resist_q[1], immu_q], check_q)
        qc.cx(check_q, out_q)
        qc.mcx([weakcheck_q, resist_q[0], resist_q[1], immu_q], check_q)

        # Uncompute
        immunite(defender, qc)
        or_weak(qc)
        calcul_resist(defender, qc)
        calcul_weak(defender, qc)
        qram_att(attacker, qc)

        # Apply generic diffuser
        qc.append(diffuser(3), [0, 1, 2])

    qc.measure(qrampoke_q, c)

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

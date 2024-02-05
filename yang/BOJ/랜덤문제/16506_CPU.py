# 31120KB / 44ms
import sys
input = sys.stdin.readline

opcode_assemble = ["ADD", "ADDC", "SUB", "SUBC", "MOV", "MOVC", "AND", "ANDC", "OR", "ORC", "NOT", "MULT", "MULTC", "LSFTL", "LSFTLC", "LSFTR", "LSFTRC", "ASFTR", "ASFTRC", "RL", "RLC", "RR", "RRC"]
opcode_machine  = ["00000", "00001", "00010", "00011", "00100", "00101", "00110", "00111", "01000", "01001", "01010", "01100", "01101", "01110", "01111", "10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111"]
opcode_dict = dict(zip(opcode_assemble, opcode_machine))

N = int(input())
for _ in range(N):
    answer = ""
    opcode, rd, ra, rb = input().split()
    brd, bra, brb = map(lambda x: bin(int(x))[2:], [rd, ra, rb])
    answer += opcode_dict[opcode] + "0"
    answer += "0"*(3 - len(brd)) + brd
    answer += "0"*(3 - len(bra)) + bra
    if opcode[-1] == "C":
        answer += "0"*(4 - len(brb)) + brb
    else:
        answer += "0"*(3 - len(brb)) + brb + "0"
    print(answer)
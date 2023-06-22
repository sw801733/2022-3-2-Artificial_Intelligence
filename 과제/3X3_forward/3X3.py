import math

input = [0.9, 0.1, 0.8]
Winput_hidden = [[0.9, 0.3, 0.4], [0.2, 0.8, 0.2], [0.1, 0.5, 0.6]]
Whidden_output = [[0.3, 0.7, 0.5], [0.6, 0.5, 0.2], [0.8, 0.1, 0.9]]

Xhidden = []
Ohidden = []
Xoutput = []
Ooutput = []

# Weight input to hidden
for i in range(3):
    temp = 0
    for j in range(3):
        temp += input[j] * Winput_hidden[i][j]
    Xhidden.append(temp)
    Ohidden.append(1 / (1 + math.exp(-Xhidden[i])))

# Weight hidden to output
for i in range(3):
    temp = 0
    for j in range(3):
        temp += Ohidden[j] * Whidden_output[i][j]
    Xoutput.append(temp)
    Ooutput.append(1 / (1 + math.exp(-Xoutput[i])))

print(" input    Ohidden    Ooutput")
for i in range(3):
    print(f"{input[i] : 0.1f} --> {Ohidden[i] : 0.3f} --> {Ooutput[i] : 0.3f}")

# Given params 
AIFSN = 6
CWmin = 15
CWmax = 1023
T_slot = 13
T_sifs = 32
T_preamble = 32
T_signal = 8
T_sym = 8
T_rxdelay = 49
T_tx2400bits = 448

t_ACK_wait = T_sifs + T_slot + T_rxdelay # Eq.(4) in project description
t_AIFS = T_sifs + (AIFSN * T_slot) # Eq.(6) in project description

k = 0
n = 10 # number of retransmissions
CW = CWmin
# Eq.(5) in project description for evaluating value of k with normal distribution (0, CW)
for i in range(0, n): 
    CW = ((2**i)*(CWmin + 1)) - 1
    k += min(CW, CWmax)
    if CW > CWmax:
        CW = CWmin

# Backoff time is t_cw
T_cw = T_slot * int(k)
# T_worst is evaluated to be 72742 microSeconds
T_worst = (10*(t_AIFS + T_tx2400bits + t_ACK_wait)) + T_cw 
print(T_worst)

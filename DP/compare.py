import numpy as np
from matplotlib import pyplot as plt

M_character = np.load('character.npy')
M_weapon = np.load('weapon.npy')

# 进行绘图
plt.figure(dpi=150, figsize=(6, 5))
plt.title("Expectation Compare of 7 UP characters and 5 same UP weapons")

plt.axvline(x=644, ls=":", c="lightgray")
plt.axvline(x=532, ls=":", c="lightgray")
max_pos = np.zeros(10, dtype=int)
plot_upper_bound = 2000
for j in range(7, 8):
    P_full_constellation = M_character[:, j, 1]  # 取出j-1命时的概率分布
    max_p = 0
    P_sum = np.zeros(plot_upper_bound+1, dtype=float)
    Expectation = 0
    plt.text(644, P_full_constellation[644], str(644), c="lightgray")
    for i in range(1, 1+plot_upper_bound):
        if P_full_constellation[i] > max_p:
            max_p = P_full_constellation[i]
            max_pos[j] = i
        Expectation += i * P_full_constellation[i]
        P_sum[i] = P_sum[i-1] + P_full_constellation[i]  # 累加
    print("Expectation of pulling "+str(j)+" UP characters is "+str(Expectation)+"  max probability at "+str(max_pos[j]))
    plt.plot(range(1, 1 + plot_upper_bound), P_full_constellation[1:1 + plot_upper_bound], linewidth=1.5, c='salmon', label='character')

for j in range(5, 6):
    P_full_constellation = M_weapon[:, j, 1]  # 取出j精时的概率分布
    max_p = 0
    P_sum = np.zeros(plot_upper_bound+1, dtype=float)
    Expectation = 0
    plt.text(532, P_full_constellation[532], str(532), c="lightgray")
    for i in range(1, 1+plot_upper_bound):
        if P_full_constellation[i] > max_p:
            max_p = P_full_constellation[i]
            max_pos[j] = i
        Expectation += i * P_full_constellation[i]
        P_sum[i] = P_sum[i-1] + P_full_constellation[i]  # 累加
    print("Expectation of pulling "+str(j)+" UP characters is "+str(Expectation)+"  max probability at "+str(max_pos[j]))
    plt.plot(range(1, 1 + plot_upper_bound), P_full_constellation[1:1 + plot_upper_bound], linewidth=1.5, c='#847db3', label='weapon')
plt.legend()
plt.show()

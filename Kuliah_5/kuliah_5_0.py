import numpy as np
from matplotlib import pyplot as plt

x = [5, 2, 9, 4, 7]
y = [10, 5, 8, 4, 2]

plt.plot(x, y)
plt.show()

plt.bar(x, y)
plt.show()

plt.hist(y)
plt.show()

plt.scatter(x, y)
plt.show()

# kita coba buat data dummy
x = np.linspace(0, 10, 20)  # ada 20 data antara 0 - 10
y = x**2


plt.plot(x, y)
plt.title('ini plot pertama saya')
plt.xlabel('Sumbu-X')
plt.ylabel('Sumbu-Y')


plt.subplot(1, 2, 1)
plt.plot(x, y, 'red')

plt.subplot(1, 2, 2)
plt.plot(x, y, 'green')


# ------------------------------------
# mulai dgn konsep objek oriented
# ------------------------------------
fig = plt.figure()
ax = fig.add_axes([0.1, 0.2, 0.9, 0.9])
ax.plot(x, y, 'purple')
ax.set_xlabel('Sumbu-X')
ax.set_ylabel('Sumbu-Y')
ax.set_title('Ini Judul Kedua Saya')
plt.show()
# ini kerennya kenapa manual seperti diatas
import numpy as np
from matplotlib import pyplot as plt
x = np.linspace(0, 10, 20)  # ada 20 data antara 0 - 10
y = x**2
fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.bar(x, y)
axes2.set_xlabel('Sumbu-X')
axes1.set_ylabel('Sumbu-Y')
axes2.plot(y, x)

# -------
fig, ax = plt.subplots(nrows=2, ncols=3)
ax[0, 1].plot(x, y)
ax[1, 0].plot(y, x)
ax[1, 1].bar(x, y)
# plt.show()
plt.tight_layout()

# mengatur dimensi dan DPI
fig = plt.figure(figsize=(8, 2), dpi=100)
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y)

# ---menggunakan subplots
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(8, 2), dpi=100)
ax[0].plot(x, y)
ax[1].plot(y, x)
plt.tight_layout()

# --legend
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(8, 4), dpi=100)
ax[0].plot(x, y, label="ini ke-1")
ax[1].plot(y, x)

ax[0].legend()

plt.tight_layout()

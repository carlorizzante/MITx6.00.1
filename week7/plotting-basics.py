import pylab as plt

sample = []
linear = []
quadratic = []
cubic = []
exponential = []

for i in range(30):
    sample.append(i)
    linear.append(i)
    quadratic.append(i**2)
    cubic.append(i**3)
    exponential.append(1.5**i)

# plt.plot(sample, linear)
# plt.plot(sample, quadratic)
# plt.plot(sample, cubic)
# plt.plot(sample, exponential)
# plt.show()

plt.figure("lin")
plt.title("Linear")
plt.xlabel("sample")
plt.ylabel("function")
plt.ylim(0, 1000)
plt.plot(sample, linear)

plt.figure("qua")
plt.title("Quadratic")
plt.xlabel("sample")
plt.ylabel("function")
plt.ylim(0, 1000)
plt.plot(sample, quadratic)

plt.figure("cub")
plt.title("Cubic")
plt.xlabel("sample")
plt.ylabel("function")
plt.plot(sample, cubic)

plt.figure("exp")
plt.title("Exponential")
plt.xlabel("sample")
plt.ylabel("function")
plt.plot(sample, exponential)

plt.show()

plt.figure("lin-qua")
plt.title("Linear vs Quadratic")
plt.xlabel("sample")
plt.ylabel("function")
plt.subplot(211)
plt.plot(sample, linear, "b-", label="linear")
plt.subplot(212)
plt.plot(sample, quadratic, "ro", label="quadratic")
plt.legend(loc="upper left")

plt.figure("qua-cub")
plt.title("Quadratic vs Cubic")
plt.xlabel("sample")
plt.ylabel("function")
plt.subplot(121)
plt.plot(sample, quadratic, "g^", label="quadratic")
plt.subplot(122)
plt.plot(sample, cubic, "r--", label="cubic")
plt.legend(loc="upper left")

plt.figure("cub-exp")
plt.title("Cubic vs Exponential")
plt.xlabel("sample")
plt.ylabel("function")
plt.plot(sample, cubic, label="cubic")
plt.plot(sample, exponential, label="exponential")
plt.legend(loc="upper left")

plt.show()
h = int(input("Height/Width= "))
padding = int(input("Padding[0]= "))
dilation = int(input("Dilation[1]= "))
kernel = int(input("Kernel= "))
stride = int(input("Stride[1]= "))
hout = ((h + (2*padding) - (dilation*(kernel - 1))-1)/stride) + 1
print("Dimension= ", hout)

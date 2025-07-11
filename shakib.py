import math
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate rectifier parameters
def calculate_parameters(Vm, R):
    Vdc = (2 * Vm) / math.pi
    Vrms = Vm / math.sqrt(2)
    Idc = Vdc / R
    Irms = Vrms / R

    efficiency = (Vdc ** 2) / (Vrms ** 2) * 100
    ripple_factor = math.sqrt((Vrms / Vdc) ** 2 - 1)

    return Vdc, Vrms, Idc, Irms, efficiency, ripple_factor

# Function to plot full-wave rectified waveform
def plot_waveform(Vm):
    t = np.linspace(0, 2 * np.pi, 1000)
    input_wave = Vm * np.sin(t)
    output_wave = abs(input_wave)

    plt.figure(figsize=(10, 5))
    plt.plot(t, input_wave, label="Input AC Wave", linestyle="--")
    plt.plot(t, output_wave, label="Full-Wave Rectified Output", color="red")
    plt.title("Full-Wave Rectifier")
    plt.xlabel("Time (rad)")
    plt.ylabel("Voltage (V)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Main Program
if __name__ == "__main__":
    print("🔌 Full-Wave Rectifier Analyzer 🔍")
    Vm = float(input("Enter peak voltage Vm (in volts): "))
    R = float(input("Enter load resistance R (in ohms): "))

    Vdc, Vrms, Idc, Irms, efficiency, ripple = calculate_parameters(Vm, R)

    print(f"\n📊 Results:")
    print(f"DC Output Voltage (Vdc): {Vdc:.2f} V")
    print(f"RMS Voltage (Vrms): {Vrms:.2f} V")
    print(f"DC Current (Idc): {Idc:.2f} A")
    print(f"RMS Current (Irms): {Irms:.2f} A")
    print(f"Efficiency: {efficiency:.2f} %")
    print(f"Ripple Factor: {ripple:.4f}")

    plot_waveform(Vm)
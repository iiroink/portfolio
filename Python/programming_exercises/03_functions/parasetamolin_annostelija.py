"""
Ohjelmointi 1: tehtävä 3.8.3 Parasetamolin annostelusta
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

def calculate_dose(weight, time_passed, earlier_dose):
    """
    Calculates the correct dose for paracetamol.

    :param weight: int, weight of the patient.
    :param time_passed: int, time from the previous dose.
    :param earlier_dose: int, amount of paracetamol given in previous 24h.
    :return: int, the correct dose of paracetamol
    """
    maximum_dose = weight * 15
    if earlier_dose > 4000 or time_passed < 6:
        dose = 0
    elif earlier_dose + maximum_dose > 4000:
        dose = 4000 - earlier_dose
    else:
        dose = maximum_dose

    return dose

def main():
    weight = int(input("Patient's weight (kg): "))
    time_passed = int(input("How much time has passed from the previous dose\
 (full hours): "))
    earlier_dose = int(input("The total dose for the last 24 hours (mg): "))

    print(f"The amount of Parasetamol to give to the patient:\
 {calculate_dose(weight, time_passed, earlier_dose)}")

if __name__ == "__main__":
    main()
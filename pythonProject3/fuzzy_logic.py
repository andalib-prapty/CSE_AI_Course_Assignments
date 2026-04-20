
def trimf(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b <= x < c:
        return (c - x) / (c - b)

def fan_speed_fuzzy(temp):
    low = trimf(temp, 0, 0, 20)
    medium = trimf(temp, 15, 22, 30)
    high = trimf(temp, 25, 40, 40)

    fan_low = low
    fan_med = medium
    fan_high = high

    numerator = fan_low * 20 + fan_med * 50 + fan_high * 90
    denominator = fan_low + fan_med + fan_high

    return numerator / denominator if denominator != 0 else 0


def irrigation_fuzzy(moisture):
    dry = trimf(moisture, 0, 0, 40)
    medium = trimf(moisture, 30, 50, 70)
    wet = trimf(moisture, 60, 100, 100)

    ir_low = wet
    ir_medium = medium
    ir_high = dry

    numerator = ir_low * 20 + ir_medium * 50 + ir_high * 90
    denominator = ir_low + ir_medium + ir_high

    return numerator / denominator if denominator != 0 else 0


def ac_temp_fuzzy(humidity):
    low = trimf(humidity, 0, 0, 40)
    medium = trimf(humidity, 30, 50, 70)
    high = trimf(humidity, 60, 100, 100)

    out_high = low  # low humidity → high AC temp
    out_medium = medium
    out_low = high  # high humidity → low AC temp

    numerator = out_low * 18 + out_medium * 23 + out_high * 28
    denominator = out_low + out_medium + out_high

    return numerator / denominator if denominator != 0 else 0



def calorie_burn_fuzzy(bmi):
    low = trimf(bmi, 10, 10, 18)
    normal = trimf(bmi, 17, 22, 27)
    high = trimf(bmi, 25, 40, 40)

    burn_low = low
    burn_med = normal
    burn_high = high

    numerator = burn_low * 100 + burn_med * 250 + burn_high * 450
    denominator = burn_low + burn_med + burn_high

    return numerator / denominator if denominator != 0 else 0


if __name__ == "__main__":
    print("---- FUZZY LOGIC SYSTEM OUTPUTS ----")

    # 1. Fan speed based on temperature
    temp = 30
    print(f"Fan Speed for Temp={temp}°C → {fan_speed_fuzzy(temp):.2f}")

    # 2. Irrigation based on soil moisture
    moisture = 25
    print(f"Irrigation Level for Moisture={moisture}% → {irrigation_fuzzy(moisture):.2f}")

    # 3. AC temperature based on humidity
    humidity = 80
    print(f"AC Temperature for Humidity={humidity}% → {ac_temp_fuzzy(humidity):.2f}")

    # 4. Calorie burn based on BMI
    bmi = 30
    print(f"Estimated Calorie Burn for BMI={bmi} → {calorie_burn_fuzzy(bmi):.2f}")


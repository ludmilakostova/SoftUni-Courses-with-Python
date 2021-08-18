scum_price = float(input())
tsa_price = float(input())
pala_kg = float(input())
saf_kg = float(input())
midi_kg = int(input())
total_pala = 1.6 * scum_price * pala_kg
total_saf = 1.8 * tsa_price * saf_kg
total_midi = 7.50 * midi_kg
total = total_pala + total_saf + total_midi
total_format = "{:.2f}".format(total)
print(total_format)
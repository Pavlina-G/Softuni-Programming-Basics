price_skumria_kg = float(input())
price_tsatsa_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = float(input())

palamud_price = price_skumria_kg + (price_skumria_kg * 0.6)
safrid_price = price_tsatsa_kg + (price_tsatsa_kg* 0.8)
price_midi = 7.50

total_cost = palamud_price * palamud_kg + safrid_price * safrid_kg + midi_kg* price_midi
print ('%.2f' % (total_cost))
bitcoin_number = int(input())
cny_number = float(input())
commission_fee = float(input())

exchange_rate_bitcoin_to_bgn = 1168
exchange_rate_usd_to_bgn = 1.76
exchange_rate_eur_to_bgn = 1.95
exchange_rate_cny_to_usd = 0.15

bgn = bitcoin_number * exchange_rate_bitcoin_to_bgn
usd = cny_number * exchange_rate_cny_to_usd
bgn = bgn + (usd * exchange_rate_usd_to_bgn)
eur = bgn / exchange_rate_eur_to_bgn

if commission_fee > 0:
    eur = eur - (commission_fee /100 * eur)
else:
    pass
print(f"{eur:.2f}")


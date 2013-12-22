## Vraag invoer op
bedrag = input ( 'Geef bedrag tussen 0 en 500 eurocent: ' )
#@ 0 <= bedrag <= 500

## Bepaal minimale betaling van bedrag
betaling = ''         # reeds gevonden deel van de betaling
totaal = 0            # totaal aantal munten
restbedrag = bedrag   # resterende te passen bedrag

#@ inv: 0 <= restbedrag <= 500
#@      betaling + restbedrag = bedrag

for munt in 200, 100, 50, 20, 10, 5, 2, 1 :
    aantal = restbedrag // munt  # aantal keer dat munt gebruikt kan worden
    restbedrag = restbedrag % munt

    #@ betaling + aantal*munt + restbedrag = bedrag
    #@ restbedrag < munt

    if aantal > 0 :  # munt is inderdaad gebruikt
        betaling = betaling + '%d x %3d = %3d\n' % (aantal, munt, aantal*munt)
        totaal = totaal + aantal
#@ restbedrag = 0, dus betaling voldoet bedrag

## Schrijf minimale betaling

## print totaalregel


print betaling
print 14*'-'
print '%2d munten: %3d'  % (totaal, bedrag) 
# Surfing the Waves
> Credits to @ZeroDayTea

Looking at the sound signal in audacity or any visualization software and we can visually see that the amplitudes are in some sort of pattern.
## Method
By using `scripy.io` we are able to read the WAV file in and collect all the amplitudes. If we check those value we can see they all lie within printable ASCII hex code. Thus, by converting all the unique points/peaks, we are able to recover the flag.

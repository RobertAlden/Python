cyphertext = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}"

chars = [c for c in cyphertext]
plaintext = []
for c in chars:
    if (97 <= ord(c) <= 97+26):
        plaintext.append(chr((((ord(c)-97)+13)%26)+97))
    elif (65 <= ord(c) <= 65+26):
        plaintext.append(chr((((ord(c)-65)+13)%26)+65))
    else:
        plaintext.append(c)


print("".join(plaintext))
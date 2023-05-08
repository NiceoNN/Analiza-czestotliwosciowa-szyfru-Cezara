def decode_ceaser(ciphertext):
    frequency = {
        'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253,
        'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094,
        'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025,
        'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929,
        'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
        'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
        'y': 0.01974, 'z': 0.00074
    }
    max_score = float("-inf")
    decoded = ""
    for key in range(26):
        score = 0
        decoded_text = ""
        for char in ciphertext:
            if char.isalpha():
                decoded_char = chr((ord(char) - 97 + key) % 26 + 97)
                decoded_text += decoded_char
                score += frequency.get(decoded_char.lower(), 0)
            else:
                decoded_text += char
        if score > max_score:
            max_score = score
            decoded = decoded_text
    return decoded

ciphertext = "urphr dqg mxolhw lv d wudjhgb zulwwhq eb zlooldp vkdnhvshduh hduob lq klv fduhhu derxw wkh urpdqfh ehwzhhq wzr Lwdoldq brxwkv iurp ihxglqj idplolhv. lw zdv dprqj vkdnhvshduh'v prvw srsxodu sodbv gxulqj klv olihwlph dqg, dorqj zlwk kdpohw, lv rqh ri klv prvw iuhtxhqwob shuiruphg sodbv. wrgdb, wkh wlwoh fkdudfwhuv duh uhjdughg dv dufkhwbsdo brxqj oryhuv.urphr dqg mxolhw ehorqjv wr d wudglwlrq ri wudjlf urpdqfhv vwuhwfklqj edfn wr dqwltxlwb. Wkh sorw lv edvhg rq dq Lwdoldq wdoh wudqvodwhg lqwr yhuvh dv wkh wudjlfdo klvwrub ri urphxv dqg mxolhw eb duwkxu eurrnh lq 1562 dqg uhwrog lq survh lq sdodfh ri sohdvxuh eb zlooldp sdlqwhu lq 1567. vkdnhvshduh eruurzhg khdylob iurp erwk exw hasdqghg wkh sorw eb ghyhorslqj d qxpehu ri vxssruwlqj fkdudfwhuv, sduwlfxoduob Phufxwlr dqg sdulv. eholhyhg wr kdyh ehhq zulwwhq ehwzhhq 1591 dqg 1595, wkh sodb zdv iluvw sxeolvkhg lq d txduwr yhuvlrq lq 1597. wkh whaw ri wkh iluvw txduwr yhuvlrq zdv ri srru txdolwb, krzhyhu, dqg odwhu hglwlrqv fruuhfwhg wkh whaw wr frqirup pruh forvhob zlwk vkdnhvshduh'v ruljlqdo.vkdnhvshduh'v xvh ri srhwlf gudpdwlf vwuxfwxuh (lqfoxglqj hiihfwv vxfk dv vzlwfklqj ehwzhhq frphgb dqg wudjhgb wr khljkwhq whqvlrq, wkh hasdqvlrq ri plqru fkdudfwhuv, dqg qxphurxv vxe-sorwv wr hpehoolvk wkh vwrub) kdv ehhq sudlvhg dv dq hduob vljq ri klv gudpdwlf vnloo. wkh sodb dvfulehv gliihuhqw srhwlf irupv wr gliihuhqw fkdudfwhuv, vrphwlphv fkdqjlqj wkh irup dv wkh fkdudfwhu ghyhorsv. urphr, iru hadpsoh, jurzv pruh dghsw dw wkh vrqqhw ryhu wkh frxuvh ri wkh sodb.Urphr dqg mxolhw kdv ehhq dgdswhg qxphurxv wlphv iru vwdjh, ilop, pxvlfdo, dqg rshud yhqxhv. gxulqj wkh hqjolvk uhvwrudwlrq, lw zdv uhylyhg dqg khdylob uhylvhg eb zlooldp gdyhqdqw. gdylg Jduulfn'v 18wk-fhqwxub yhuvlrq dovr prglilhg vhyhudo vfhqhv, uhprylqj pdwhuldo wkhq frqvlghuhg lqghfhqw, dqg Jhruj ehqgd'v Urphr xqg mxolh rplwwhg pxfk ri wkh dfwlrq dqg xvhg d kdssb hqglqj."
decoded_text = decode_ceaser(ciphertext)
print("Decoded text: ", decoded_text)
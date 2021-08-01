import base64

def show_best_message():

    the_value = base64.b64decode(b'TmV2ZXIgZ29uZSBnaXZlIHlvdSB1cCwgbmV2ZXIgZ29uZSBsZXQgeW91IGRvd24sIC4uLiwgSGFoYSB5b3UgZ290IFJJQ0tST0xMRUQ=')

    return str(the_value.decode('utf-8')).split(", ")

the_final_result = show_best_message()

print(the_final_result[0] + "," + "\n" + the_final_result[1] + "," + "\n" + the_final_result[2] + "\n" + the_final_result[3])
text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('0.8475')
snippet = text[pos:]
print(float(snippet))

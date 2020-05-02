text = "X-DSPAM-Confidence:    0.8475";

#----find index of '0' using find() method---- 
value = text.find('0')

#----apply slicing to extract 0.8475----
data = text[value:value+6]

#----convert that piece of data into float----
data = float(data)
print(data)

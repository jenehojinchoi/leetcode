# 193. Valid Phone Numbers 
egrep '^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$' file.txt
grep -P '^(\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$' file.txt
We accessed the embedded device's asynchronous serial debugging interface while it was operational and 
captured some messages that were being transmitted over it. Can you decode them?

1. Analyze .sal file:

   ~/CTF/Challenge/Hardware/Debugging Interface    main !1 ?2  file debugging_interface_signal.sal                                                                                          ✔  23:37:37  
debugging_interface_signal.sal: Zip archive data, at least v2.0 to extract, compression method=deflate

    ~/CTF/Challenge/Hardware/Debugging Interface    main !1 ?2  unzip -l debugging_interface_signal.sal                                                                                      ✔  23:38:20  
Archive:  debugging_interface_signal.sal
  Length      Date    Time    Name
---------  ---------- -----   ----
    22090  2021-03-23 12:02   digital-0.bin
    27810  2021-03-23 12:02   meta.json
---------                     -------
    49900                     2 files

2. Software used (Logic 2)

A. Open the software (Logic 2) 

B. Try to decode the protocol

We know that the properties of the Asynchronous serial communication :
    - The number of bits per character -- currently almost always 8-bit characters, but historically some transmitters have used a five-bit character code, six-bit character code, or a 7-bit ASCII.
    - Endianness: the order in which the bits are sent
    - Transmission is ASCII over RS-232
    - The speed or bits per second of the line (equal to the Baud rate when each symbol represents one bit). Some systems use automatic speed detection, also called automatic baud rate detection.
    - The number of stop bits sent must be chosen (the number sent must be at least what the receiver needs)

Calcul Baudrate:
    x represent the lowest intervale betwen 2 bits.
    - x = 32.02*10^(-6) (converted in second)    
    1/x = 31,230.480949406621 = 31,230 (with Round)

Export the data from Logic 2 and you can get the flag (data-extracted)


# Format the data from python

#!/bin/python
import csv

if __name__ == "__main__":
    value = ""
    
    with open('data-extracted') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            value += row[3]

    print(value)

## Result : 

data[MSG] Activity from: ec1c7e7449341b58478c93c27ea6e08a53cc834279e1643dbba994a0e7f3ea43

[MSG] Activity from: 003b9434a45f0eecd2d35bcc78129aa3edc363f802ae5abdd161c4f421ca49a7

[MSG] Activity from: 65ec312325f43f40107dfcba651cab2d1afb6df54578065f1d8bba89801d3ef2

[MSG] Activity from: 223e634cea203ba2c7d4e7931a2dafdf0d452309c1a1eb1a28fc2fae057df400

[MSG] Activity from: 431d591c6eed3b6e793b316d7bf6ce2e3be51aa707680b6f14511fbc9dae9e32

[MSG] Activity from: 65ec312325f43f40107dfcba651cab2d1afb6df54578065f1d8bba89801d3ef2

[MSG] Activity from: 65ec312325f43f40107dfcba651cab2d1afb6df54578065f1d8bba89801d3ef2

[MSG] Activity from: ebb2b5d1dfbbb8174f5fb1fd15230540aea77772d3a65482def3d978f6caf152

[MSG] Activity from: f7fab4b591754a190be32cb607f257f436fa3f325d71edf41b6179c5330cd75a

[MSG] Activity from: 476bdcaf166385371f49c54ba74d275cfdfa5c70c255ea45363e3795cbc11ae5

[MSG] Activity from: 63681fa3c03451c49f9fc2ab9be43bea7f069069c1c472f6a41e3ef3a761de50

[MSG] Activity from: 36257a19934b71cea753da3df9be8ae8ca49ee843b72b1c5468f8f5dab8a7ad0

[MSG] Activity from: 36257a19934b71cea753da3df9be8ae8ca49ee843b72b1c5468f8f5dab8a7ad0

[MSG] Activity from: HTB{d38u991n9_1n732f4c35_c4n_83_f0und_1n_41m057_3v32y_3m83dd3d_d3v1c3!!52}


## Ressources :
    https://en.wikipedia.org/wiki/Asynchronous_serial_communication
    https://support.saleae.com/faq/technical-faq/sal-file-format
    https://discuss.saleae.com/t/logic-2-capture-format-sal/1858

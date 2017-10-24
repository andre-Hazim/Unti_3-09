# Created by: Andre
# Created on: Sep 2017
# Created for: ICS3U
# This program shows an example of nested loops


counter = 65
counter2 = 97
for counter in range(65, 91):
    for counter2 in range(97, 122):
        print(unichr(counter) + "->" + unichr(counter2))

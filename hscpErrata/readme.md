|||||||||
|-|-|-|-|-|-|-|-|
|Page in the Main Text|Page in the PDF File|Chapter|Sector|Location in the Sector|The Original|Should be|Comments|
|121|142|Chapter 8 – The Transposition Cipher, Encrypting|Key Size and Message Length|4th Line From the Bottom|key size becomes more than twice the message length|key size becomes more than half the message length|
|90|110|Chapter 7 – Hacking the Caesar Cipher with the Brute Force Technique|Source code for caesarHacker.py|Line 22 in .py|# handle the wrap-around if num is 26 or larger or less than 0|# handle the wrap-around if num is less than 0|When decrypting, the number to wrap-around can only be less than 0 since it is always doing a subtraction to decrypt|
|140|160|Chapter 10 – Programming a Program to Test Our Program|Sample Run of the Transposition Cipher Tester Program|The first 20 lines in the output result of the program|omitted|see below|Since the seed is set to be 42, the output should be all the same whenever you run it, the first message being identical with that in P152(main text or P172 in pdf file)|

```
Test #1: "JEQLDFKJZWALCOYACUPLTRRMLWHOBXQNEAWSLGWAGQQSRSIUIQ..."
Test #2: "SWRCLUCRDOMLWZKOMAGVOTXUVVEPIOJMSBEQRQOFRGCCKENINV..."
Test #3: "BIZBPZUIWDUFXAPJTHCMDWEGHYOWKWWWSJYKDQVSFWCJNCOZZA..."
Test #4: "JEWBCEXVZAILLCHDZJCUTXASSZZRKRPMYGTGHBXPQPBEBVCODM..."
Test #5: "DMMEDKAHCZJDBNCCCZNENAOSJUKGHGUANOCHFGSEVDOMYHVBRK..."
Test #6: "WPOWKFRGLWZFRPXYPDUQADOXPGEABHKNMDLYTITYOBEATVLAIB..."
Test #7: "KVNJOCYPGIUNVLPRZFFAESDUTZRMDKRSSAWQIWXWCPGWUISLHP..."
Test #8: "RMVZKCBLEFVZSLTEUGCQRJUWQWQILELVNTGHONBIXNJGTRMGHH..."
Test #9: "PVHJOFQJRGXYXFFRRJZTQXRFLWVHPQSHNYOZRJSKJFNRIGQYCH..."
Test #10: "CFWPWYEKXSREXTZZLITJIXIXESHFJCSPLVZQTMWBRTSYBEDCHK..."
Test #11: "QNUZXADCRFYBODYWYJZTPFMGYNWNKGYUBCJXHSSPIIWYYRXCXK..."
Test #12: "DZSEKFURFHNLMFRITPTNQWEVVJVDSBOUUFKXZJNRXHANWCBEYX..."
Test #13: "FXCAYLCKJIACMGATEPYLHAHVSMTHIHDHNBBNFWVXURLVADSGDB..."
Test #14: "QKGAZJEFOIWILSENDNVWZUBLSRVHEEDFUSFNMOURJKPAIRWXMG..."
Test #15: "WHXYUOUIJQLVDKKSZBTPYOHHGAJFUGILNMQAWTMUOICNFIOJXO..."
Test #16: "GMZMPQAMZDMWCMDMCLUOSWDRJZBVPKYGZDXCWOUVIQLLECWSMU..."
Test #17: "KPKHHLPUWPSSIOULGKVEFHZOKBFHXUKVSEOWOENOZSNIDELAWR..."
Test #18: "OYLFXXZENDFGSXTEAHGHPBNORCFEPBMITILSSJRGDVMNSOMURV..."
Test #19: "SOCLYBRVDPLNVJKAFDGHCQMXIOPEJSXEAAXNWCCYAGZGLZGZHK..."
Test #20: "JXJGRBCKZXPUIEXOJUNZEYYSEAEGVOJWIRTSSGPUWPNZUBQNDA..."
```

  
Page in the Main Text  
Page in the PDF File  
Chapter  
Sector  
Location in the Sector  
The Original  
Should be  
Comments  
  
90  
110  
Chapter 7 – Hacking the Caesar Cipher with the Brute Force Technique  
Source code for caesarHacker.py  
Line 22 in .py  
# handle the wrap-around if num is 26 or larger or less than 0  
 - [] Should be: # handle the wrap-around if num is less than 0  
When decrypting, the number to wrap-around can only be less than 0 since it is always doing a subtraction to decrypt  
  
  
121  
142  
Chapter 8 – The Transposition Cipher, Encrypting  
Key Size and Message Length  
4th Line From the Bottom  
key size becomes more than twice the message length  
 - [] Should be: key size becomes more than half the message length  
  
  
140  
160  
Chapter 10 – Programming a Program to Test Our Program  
Sample Run of the Transposition Cipher Tester Program  
The first 20 lines in the output result of the program  
see below(original)  
 - [] Should be:see below(should be)  
Since the seed is set to be 42, the output should be all the same whenever you run it, the first message being identical with that in P152(main text or P172 in pdf file)  
  
  
original:  
```  
Test #1: "KQDXSFQDBPMMRGXFKCGIQUGWFFLAJIJKFJGSYOSAWGYBGUNTQX..."  
Test #2: "IDDXEEWUMWUJPJSZFJSGAOMFIOWWEYANRXISCJKXZRHMRNCFYW..."  
Test #3: "DKAYRSAGSGCSIQWKGARQHAOZDLGKJISQVMDFGYXKCRMPCMQWJM..."  
Test #4: "MZIBCOEXGRDTFXZKVNFQWQMWIROJAOKTWISTDWAHZRVIGXOLZA..."  
Test #5: "TINIECNCBFKJBRDIUTNGDINHULYSVTGHBAWDQMZCNHZOTNYHSX..."  
Test #6: "JZQIHCVNDWRDUFHZFXCIASYDSTGQATQOYLIHUFPKEXSOZXQGPP..."  
Test #7: "BMKJUERFNGIDGWAPQMDZNHOQPLEOQDYCIIWRKPVEIPLAGZCJVN..."  
Test #8: "IPASTGZSLPYCORCVEKWHOLOVUFPOMGQWZVJNYQIYVEOFLUWLMQ..."  
Test #9: "AHRYJAPTACZQNNFOTONMIPYECOORDGEYESYFHROZDASFIPKSOP..."  
Test #10: "FSXAAPLSQHSFUPQZGTIXXDLDMOIVMWFGHPBPJROOSEGPEVRXSX..."  
Test #11: "IVBCXBIHLWPTDHGEGANBGXWQZMVXQPNJZQPKMRUMPLLXPAFITN..."  
Test #12: "LLNSYMNRXZVYNPRTVNIBFRSUGIWUJREMPZVCMJATMLAMCEEHNW..."  
Test #13: "IMWRUJJHRWAABHYIHGNPSJUOVKRRKBSJKDHOBDLOUJDGXIVDME..."  
Test #14: "IZVXWHTIGKGHKJGGWMOBAKTWZWJPHGNEQPINYZIBERJPUNWJMX..."  
Test #15: "BQGFNMGQCIBOTRHZZOBHZFJZVSRTVHIUJFOWRFBNWKRNHGOHEQ..."  
Test #16: "LNKGKSYIPHMCDVKDLNDVFCIFGEWQGUJYJICUYIVXARMUCBNUWM..."  
Test #17: "WGNRHKIQZMOPBQTCRYPSEPWHLRDXZMJOUTJCLECKEZZRRMQRNI..."  
Test #18: "PPVTELDHJRZFPBNMJRLAZWRXRQVKHUUMRPNFKXJCUKFOXAGEHM..."  
Test #19: "UXUIGAYKGLYUQTFBWQUTFNSOPEGMIWMQYEZAVCALGOHUXJZPTY..."  
Test #20: "JSYTDGLVLBCVVSITPTQPHBCYIZHKFOFMBWOZNFKCADHDKPJSJA..."  
```  
  
should be:  
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
  
  
Page in the Main Text  
Page in the PDF File  
Chapter  
Sector  
Location in the Sector  
The Original  
Should be  
Comments  
  
165  
185  
Chapter 11 – Encrypting and Decrypting Files  
transpositionFileCipher.py  
Line 51 in codes  
If transpositionCipherFile.py is run  
 - [] Should be:If transpositionFileCipher.py is run  
  
  
169  
189  
Chapter 12 – Detecting English Programmatically  
Source code for detectEnglish.py  
Line 5, 6 in codes  
ommitted  
ommitted  
 - [] Should be:This is a print/display error. When copied and pasted, the words are one space from # but when viewed, it is obviously larger  
  
  
169  
189  
Chapter 12 – Detecting English Programmatically  
How the Program Works  
Line 5, 6 in codes  
ommitted  
ommitted  
 - [] Should be:ibid  
  
  
  
  
Page in the Main Text  
Page in the PDF File  
Chapter  
Sector  
Location in the Sector  
The Original  
Should be  
Comments  
  
  
  
198  
218  
Chapter 14 – Modular Arithmetic and the Multiplicative Cipher  
10 O’Clock + 5 Hours = 3 O’Clock  
Line 5 to 6  
Whether or not it is 3 AM or 3PM depends on if the current time is 10 AM or 10 PM.  
 - [] Should be:Whether or not it is 3 AM or 3PM depends on if the current time is 10 PM or 10 AM.  
The latter should be consistent with the former.  
  
  
264  
284  
Chapter 18 – Hacking the Simple Substitution Cipher  
simpleSubHacker.py  
Line 100 in .py code  
If a letter is solved, than it cannot possibly be a potential  
 - [] Should be:If a letter is solved, `then` it cannot possibly be a potential  
  
  
280  
300  
ibid  
  
  
  
  
  
  
P326 main text  
`http://invpy.com/vigenereHacking.py`  
 - [] should be `http://invpy.com/vigenereHacker.py`  
  
makeRsaKeys.py line 47  
`with the the n,e`  
 - [] one more 'the'  
  
P386 main text  
```  
The private key is a 617 and a 309 digit number.  
Writing private key to file al_sweigart_privkey.txt...  
```  
 - [] Lack a line `Key files made.`  
  
  
P386 main text  
```  
Making key files...  
WARNING: The file al_sweigart_pubkey.txt or al_sweigart_privkey.txt already  
exists! Use a different name or delete these files and re-run this program.  
```  
 - [] WARNING does not show when the .py is run in idle  
  
  
 - [] Table 24-4  
2nd Block’s Indexes should begin with `128`  
3rd Block’s Indexes should begin with `256`
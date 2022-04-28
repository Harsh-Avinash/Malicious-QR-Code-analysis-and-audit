# Transmitting Malware Through a QR Code

A QR code is a type of barcode that can be read easily by a digital device and which stores information as a series of pixels in a square-shaped grid. QR codes are frequently used to track information about products in a supply chain and – because many smartphones have built-in QR readers – they are often used in marketing and advertising campaigns. More recently, they have played a key role in helping to trace coronavirus exposure and slow the spread of the virus.

## Introduction


The first QR code system was invented in 1994 by the Japanese company Denso Wave, a Toyota subsidiary. They needed a more accurate way to track vehicles and parts during the manufacturing process. To achieve this, they developed a type of barcode that could encode kanji, kana, and alphanumeric characters.
Standard barcodes can only be read in one direction – top to bottom. That means they can only store a small amount of information, usually in an alphanumeric format. But a QR code is read in two directions – top to bottom and right to left. This allows it to house significantly more data.
The data stored in a QR code can include website URLs, phone numbers, or up to 4,000 characters of text. QR codes can also be used to:
<br> <br> Link directly to download an app on the Apple App Store or Google Play.
<br> 	Authenticate online accounts and verify login details.
<br> 	Access Wi-Fi by storing encryption details such as SSID, password, and encryption type.
<br> 	Send and receive payment information.
<br> 	And much more – a company in the UK called QR Memories even creates QR codes for use on gravestones, allowing people to scan the code to read more about that deceased person’s life (if they have an obituary or news story relating to them online).

## Related Work

Attackers can use QR codes for various types of attacks. However, two critical attacks we are interested in for this study are phishing and malware attacks. 

**Phishing**: phishing is an activity that tricks people to divulge their sensitive information by masquerading as a trustworthy entity [1, 2]. A QR code can redirect users to a fake bank that looks exactly like the real bank. A normal user cannot see the differences and type in his or her information and hand it to the attackers [3-5]. 

**Malware**: A malicious QR code can be used to redirect users to a URL containing malware[3]. An early example of malware attacks through QR code was that people were fooled into scanning a QR code and downloading a malicious application, which sent off multiple text messages to a number that charged users $5 per SMS message [6]. 

There are other types of attacks such as social engineering [7] and cross-site attacks [8]. Though interesting, a complete study to analyse these rather rare cases was out of purview of our study

Google Play, the official Android Market, is used as a reliable source for users to download the apps. On Jun 6, 2012, we searched for QR code scanning apps from Google Play market using keywords “QR code”, “QR code reader”, and “QR code scanner,” and we found 31 apps. We installed them in an HTC Nexus One with Android 2.3.6 and used them to scan QR codes with benign URLs randomly chosen from DMOZ [9], a manually edited directory, and QR codes with malicious URLs selected from Phish Tank [10], a blacklist of phishing URLs, to find out the features of these scanners.

However, none of the features seems to provide users with information that will help them make a better security decision. As to the user confirmation feature, users see only a URL and they often click to continue to visit the site without much thinking about the security consequences. Unsophisticated users may even not be able to recognize malicious URLs. The preview feature can be easily abused, incapable of providing users with needed security information either; a well-designed fraudulent website can only give a false sense of security to users.

Among the 31 scanners, only two (0.06%), “Norton Snap QR Code Reader” and “QR Pal – QR & Barcode Scanner”, had a feature called security warning. Upon scanning a QR code containing a malicious URL, Norton Snap and QR Pal equipped 342 with the feature display the URL along with a warning message before loading the website of the URL

Malware attack is another popular attack on Android. We tested the two QR code scanners against the attacks using malware obtained from http://malgenomeproject.org. Specifically, we used malware under the drive-by download categories (GGTracker, Jifake, Spitmo, and Zitmo) and repackaging malware categories (AnserverBot and DroidKungFu). Each of the four drive-by downloaded categories contains only one malware. We chose all these four malwares for testing. For AnserverBot and DroidKungFu, we randomly picked one malware from each category. We uploaded these six malwares to a personal homepage http://infohost.nmt.edu/~hyao, and tested the corresponding URLs, thus simulating a zero-day attack.

![image](https://user-images.githubusercontent.com/64661719/165730996-a290fd11-152f-4bee-9d1b-7e3af41d9ff8.png)

## Proposed Work
Two well-known security APIs, Google Safe Browsing API [19] and PhishTank API [20], were adopted for our solution to improve the effectiveness of detecting malicious URLs.

Safe Browsing, developed by Google, is a service that enables applications to check URLs against Google’s constantly updated lists of suspected phishing and malware websites. For simplicity, we chose Safe Browsing Lookup API [21], queried the URLs through HTTP GET request, and got the state of the URL(s) directly. PhishTank contains a blacklist of phishing URLs consisting of manually verified websites. PhishTank provides API for developers to lookup a URL’s status in their database. We used the API to query a URL’s status, thus further enhancing the capability for detecting phishing scams.

In addition, if the URL string ends with .apk, this means that a non-official Android market application will be downloaded to a user’s mobile phone. Specifically, if “Unknown Sources” setting is checked in Android, the app will be automatically downloaded to the user’s Android device. If the setting is not checked, a dialog will pop up to ask the user if she wants to check the option to download the app. Users can easily tick “Unknown Sources” option just by following the instructions in the dialog, and then download and install the application. Our solution checked if the URL ended with “.apk”, and if yes, then we provided potential warnings to users.

## Conclusion
In this paper, I presented an approach to preventing QR codebased phishing and malware attacks. Specifically, I first studied the current status of existing QR code scanners in terms of their detection rate for malicious URLs. Then proposed a solution to detect malicious URLs more effectively by using two well know security APIs along with visual security warning design. Lastly I discussed our user study design to evaluate the effectiveness of the proposed solution.

## Reference

1.	R. Dhamija, J. D. Tygar, and M. Hearst, "Why phishing works," Proceedings of Conference on Human Factors in Computing Systems, Montréal, Québec, Canada, 2006.

2.	P. Soni, S. Firake, and B. B. Meshram, "A phishing analysis of web based systems," Proceedings of the 2011 International Conference on Communication, Computing; Security, Rourkela, Odisha, India, 2011.

3.	P. Kieseberg, M. Leithner, M. Mulazzani, L. Munroe, S. Schrittwieser, M. Sinha, and E. Weippl, "QR code security," Proceedings of the 8th International Conference on Advances in Mobile Computing, Paris, France, 2010.

4.	V. Sharma, "A Study of Malicious QR Codes," International Journal of Computational Intelligence and Information Security (IJCIIS), vol. 3, May 2012.

5.	A. P. Felt and D. Wagner, "Phishing on Mobile Devices," the WEB 2.0 Security and Privacy (W2SP), Oakland, California, USA, 2011.

6.	Monthly Malware Statistics: September 2011. Available: www.securelist.com/en/analysis /204792195/Monthly_Malware_Statistics_September_2011

7.	L. Borrett. (2011). Beware of Malicious QR Codes. Available: http://www.abc.net.au/technology/articles/ 2011/06/08/3238443.htm

8.	A. Kieyzun, P. J. Guo, K. Jayaraman, and M. D. Ernst, "Automatic creation of SQL Injection and cross-site scripting attacks," Proceedings of the 31st International Conference on Software Engineering, 2009.

9.	Netscape. DMOZ Open Directory Project. Available: http://www.dmoz.org

10.	PhishTank. Available: http://www.phishtank.com

11.	Huiping Yao and Dongwan Shin. 2013. Towards preventing QR code-based attacks on android phone using security warnings. In Proceedings of the 8th ACM SIGSAC symposium on Information, computer, and communications security (ASIA CCS '13). Association for Computing Machinery, New York, NY, USA, 341–346. DOI:https://doi.org/10.1145/2484313.2484357

12.	Zhou, Y. and Jiang, X., 2012, May. Dissecting android malware: Characterization and evolution. In 2012 IEEE symposium on security and privacy (pp. 95-109). IEEE.

13.	Yao, H. and Shin, D., 2013, May. Towards preventing qr code based attacks on android phone using security warnings. In Proceedings of the 8th ACM SIGSAC symposium on Information, computer and communications security (pp. 341-346).

14.	Cheon, W.B., il Heo, K., Lim, W.G., Park, W.H. and Chung, T.M., 2011, April. The new vulnerability of service set identifier (SSID) using QR code in android phone. In 2011 international conference on information science and applications (pp. 1-6). IEEE.

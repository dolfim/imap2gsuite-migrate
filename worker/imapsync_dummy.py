import os
import time
import subprocess

SOURCE_IMAP_HOST=os.getenv('SOURCE_IMAP_HOST', '')
SOURCE_IMAP_PORT=os.getenv('SOURCE_IMAP_PORT', None)
TARGET_AUTH_FILE=os.getenv('TARGET_AUTH_FILE')


_example_out = r"""
Here is imapsync 1.983 on host 39eb9c59f7a5, a linux system with 0.6/1.9 free GiB of RAM
with Perl 5.28.1 and Mail::IMAPClient 3.42
Transfer started at Sun May  3 12:08:04 2020
PID is 1 my PPID is 0
Load is 0.40 0.09 0.03 4/418 on 2 cores
Current directory is /var/tmp
Real user id is nobody (uid 65534)
Effective user id is nobody (euid 65534)
$RCSfile: imapsync,v $ $Revision: 1.983 $ $Date: 2020/03/19 02:08:12 $ 
Command line used, run by /usr/bin/perl:
/usr/bin/imapsync --host1 imap.mail.hostpoint.ch --ssl1 --user1 m.dolfi@olympiad.ch --password1 MASKED --gmail2 --user2 test1@physics.olympiad.ch --password2 MASKED --authmech2 XOAUTH2
Temp directory is /tmp ( to change it use --tmpdir dirpath )
Under docker context so installing only signals to exit
kill -INT 1 # special behavior: call to sub catch_exit
kill -QUIT 1 # special behavior: call to sub catch_exit
kill -TERM 1 # special behavior: call to sub catch_exit
No variable pid_filename
PID file is unset ( to set it, use --pidfile filepath ; to avoid it use --pidfile "" )
Modules version list:
Authen::NTLM         1.09
CGI                  4.40
Compress::Zlib       2.074
Crypt::OpenSSL::RSA  0.31
Data::Uniqid         0.12
Digest::HMAC_MD5     1.01
Digest::HMAC_SHA1    1.03
Digest::MD5          2.55
Encode               2.97
Encode::IMAPUTF7     1.05
File::Copy::Recursive 0.44
File::Spec           3.74
Getopt::Long         2.5
HTML::Entities       3.69
IO::Socket           1.39
IO::Socket::INET     1.39
IO::Socket::INET6    2.72
IO::Socket::IP       0.39
IO::Socket::SSL      2.060
IO::Tee              0.65
JSON                 4.02
JSON::WebToken       0.10
LWP                  6.36
MIME::Base64         3.15
Mail::IMAPClient     3.42
Net::Ping            2.62
Net::SSLeay          1.85
Term::ReadKey        2.38
Test::MockObject     1.20180705
Time::HiRes          1.9759
URI::Escape          3.31
Unicode::String      2.10
( use --no-modulesversion to turn off printing this Perl modules list )
Info: will resync flags for already transferred messages. Use --noresyncflags to not resync flags.
SSL debug mode level is --debugssl 1 (can be set from 0 meaning no debug to 4 meaning max debug)
Host1: SSL default mode is like --sslargs1 "SSL_verify_mode=0", meaning for host1 SSL_VERIFY_NONE, ie, do not check the certificate server.
Host1: Use --sslargs1 SSL_verify_mode=1 to have SSL_VERIFY_PEER, ie, check the certificate server of host1
Host2: SSL default mode is like --sslargs2 "SSL_verify_mode=0", meaning for host2 SSL_VERIFY_NONE, ie, do not check the certificate server.
Host2: Use --sslargs2 SSL_verify_mode=1 to have SSL_VERIFY_PEER, ie, check the certificate server of host2
Info: turned ON syncinternaldates, will set the internal dates (arrival dates) on host2 same as host1.
Host1: will try to use LOGIN authentication on host1
Host2: will try to use XOAUTH2 authentication on host2
Host1: imap connection timeout is 120 seconds
Host2: imap connection timeout is 120 seconds
Host1: IMAP server [imap.mail.hostpoint.ch] port [993] user [m.dolfi@olympiad.ch]
Host2: IMAP server [imap.gmail.com] port [993] user [test1@physics.olympiad.ch]
Host1: connecting and login on host1 [imap.mail.hostpoint.ch] port [993] with user [m.dolfi@olympiad.ch]
Host1 IP address: 217.26.49.199
Host1 banner: * OK [CAPABILITY IMAP4rev1 LITERAL+ SASL-IR LOGIN-REFERRALS ID ENABLE IDLE AUTH=PLAIN] Dovecot ready.
Host1 capability before authentication: IMAP4rev1 LITERAL+ SASL-IR LOGIN-REFERRALS ID ENABLE IDLE AUTH=PLAIN AUTH
Host1: success login on [imap.mail.hostpoint.ch] with user [m.dolfi@olympiad.ch] auth [LOGIN]
Host2: connecting and login on host2 [imap.gmail.com] port [993] with user [test1@physics.olympiad.ch]
Host2 IP address: 108.177.126.109
Host2 banner: * OK Gimap ready for requests from 51.154.214.166 u21mb183888216edq
Host2 capability before authentication: IMAP4rev1 UNSELECT IDLE NAMESPACE QUOTA ID XLIST CHILDREN X-GM-EXT-1 XYZZY SASL-IR AUTH=XOAUTH2 AUTH=PLAIN AUTH=PLAIN-CLIENTTOKEN AUTH=OAUTHBEARER AUTH=XOAUTH AUTH
Host2: imap.gmail.com says it has CAPABILITY for AUTHENTICATE XOAUTH2
Host2: success login on [imap.gmail.com] with user [test1@physics.olympiad.ch] auth [XOAUTH2]
Host1: state Authenticated
Host2: state Authenticated
Host1 capability once authenticated: IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE SORT SORT=DISPLAY THREAD=REFERENCES THREAD=REFS THREAD=ORDEREDSUBJECT MULTIAPPEND URL-PARTIAL CATENATE UNSELECT CHILDREN NAMESPACE UIDPLUS LIST-EXTENDED I18NLEVEL=1 CONDSTORE QRESYNC ESEARCH ESORT SEARCHRES WITHIN CONTEXT=SEARCH LIST-STATUS BINARY MOVE SNIPPET=FUZZY PREVIEW=FUZZY LITERAL+ NOTIFY SPECIAL-USE QUOTA THREAD I18NLEVEL CONTEXT SNIPPET PREVIEW
Host2 capability once authenticated: IMAP4rev1 UNSELECT IDLE NAMESPACE QUOTA ID XLIST CHILDREN X-GM-EXT-1 UIDPLUS COMPRESS=DEFLATE ENABLE MOVE CONDSTORE ESEARCH UTF8=ACCEPT LIST-EXTENDED LIST-STATUS LITERAL- SPECIAL-USE APPENDLIMIT=35651584 COMPRESS UTF8 APPENDLIMIT

Host1: found ID capability. Sending/receiving ID, presented in raw IMAP for now.
In order to avoid sending/receiving ID, use option --noid
Sending: 4 ID ("name" "imapsync" "version" "1.983" "os" "linux" "vendor" "Gilles LAMIRAL" "support-url" "https://imapsync.lamiral.info/" "date" "19-Mar-2020 02:08:12 +0000" "side" "host1")
Sent 181 bytes
Read: 	* ID ("name" "Dovecot")
  	4 OK ID completed (0.001 + 0.000 secs).

Sending: 4 ID ("name" "imapsync" "version" "1.983" "os" "linux" "vendor" "Gilles LAMIRAL" "support-url" "https://imapsync.lamiral.info/" "date" "19-Mar-2020 02:08:12 +0000" "side" "host2")

Host2: found ID capability. Sending/receiving ID, presented in raw IMAP for now.
In order to avoid sending/receiving ID, use option --noid
Sent 181 bytes
Read: 	* ID ("name" "GImap" "vendor" "Google, Inc." "support-url" "https://support.google.com/mail" "version" "gmail_imap_200428.12_p0" "remote-host" "51.154.214.166")
  	4 OK Success


Host2: found quota, presented in raw IMAP
Sending: 5 GETQUOTAROOT INBOX
Sent 22 bytes

Host2: Quota current storage is 460800 bytes. Limit is 32212254720 bytes. So 0.00 % full
Host2: found APPENDLIMIT=35651584 in CAPABILITY (use --appendlimit xxxx to override this automatic setting)
Read: 	* QUOTAROOT "INBOX" ""
  	* QUOTA "" (STORAGE 450 31457280)
  	5 OK Success
Host2: Setting maxsize to 35651584 (min of --maxsize 35651584 and appendlimit 35651584
Host1: found 5 folders.
Host2: found 9 folders.
Host1: guessing separator from folder listing: [/]
Host1: separator given by NAMESPACE: [/]
Host2: guessing separator from folder listing: [/]
Host2: separator given by NAMESPACE: [/]
Host1: guessing prefix from folder listing: []
Host1: prefix given by NAMESPACE: []
Host2: guessing prefix from folder listing: []
Host2: prefix given by NAMESPACE: []
Host1: separator and prefix: [/][]
Host2: separator and prefix: [/][]
Including all folders found by default. Use --subscribed or --folder or --folderrec or --include to select specific folders. Use --exclude to unselect specific folders.
Excluding folders matching pattern \[Gmail\]$

Host1: Checking wanted folders exist. Use --nocheckfoldersexist to avoid this check (shared of public namespace targeted).
Host1: Checking wanted folders are selectable. Use --nocheckselectable to avoid this check.
Turned on automapping folders ( use --noautomap to turn off automapping )
Host1: special Drafts               = \Drafts
Host1: special Sent                 = \Sent
Host1: special Trash                = \Trash
Host1: special spam                 = \Junk

Host2: special [Gmail]/All Mail     = \All
Host2: special [Gmail]/Bin          = \Trash
Host2: special [Gmail]/Drafts       = \Drafts
Host2: special [Gmail]/Sent Mail    = \Sent
Host2: special [Gmail]/Spam         = \Junk
Host2: special [Gmail]/Starred      = \Flagged


++++ Listing folders
All foldernames are presented between brackets like [X] where X is the foldername.
When a foldername contains non-ASCII characters it is presented in the form
[X] = [Y] where
X is the imap foldername you have to use in command line options and
Y is the utf8 output just printed for convenience, to recognize it.

Host1: folders list (first the raw imap format then the [X] = [Y]):
* LIST (\HasNoChildren \UnMarked \Drafts) "/" Drafts
* LIST (\HasNoChildren \UnMarked \Sent) "/" Sent
* LIST (\HasNoChildren \UnMarked \Trash) "/" Trash
* LIST (\HasNoChildren \UnMarked \Junk) "/" spam
* LIST (\HasNoChildren) "/" INBOX
15 OK List completed (0.001 + 0.000 secs).

[Drafts]
[INBOX]
[Sent]
[Trash]
[spam]

Host2: folders list (first the raw imap format then the [X] = [Y]):
* LIST (\HasNoChildren) "/" "INBOX"
* LIST (\HasNoChildren) "/" "Originals"
* LIST (\HasChildren \Noselect) "/" "[Gmail]"
* LIST (\All \HasNoChildren) "/" "[Gmail]/All Mail"
* LIST (\HasNoChildren \Trash) "/" "[Gmail]/Bin"
* LIST (\Drafts \HasNoChildren) "/" "[Gmail]/Drafts"
* LIST (\HasNoChildren \Important) "/" "[Gmail]/Important"
* LIST (\HasNoChildren \Sent) "/" "[Gmail]/Sent Mail"
* LIST (\HasNoChildren \Junk) "/" "[Gmail]/Spam"
* LIST (\Flagged \HasNoChildren) "/" "[Gmail]/Starred"
11 OK Success

[INBOX]
[Originals]
[[Gmail]/All Mail]
[[Gmail]/Bin]
[[Gmail]/Drafts]
[[Gmail]/Important]
[[Gmail]/Sent Mail]
[[Gmail]/Spam]
[[Gmail]/Starred]

Folders in host2 not in host1:
[[Gmail]/Starred]
[[Gmail]/Important]
[[Gmail]/All Mail]
[Originals]

Folders mapping from --automap feature (use --f1f2 to override any mapping):
[spam]                                   -> [[Gmail]/Spam]                          
[Sent]                                   -> [[Gmail]/Sent Mail]                     
[Drafts]                                 -> [[Gmail]/Drafts]                        
[Trash]                                  -> [[Gmail]/Bin]                           

Checking SEARCH ALL works on both accounts. To avoid that check, use --nochecknoabletosearch
Host1: checking if SEARCH ALL works on INBOX
Host1: folder [INBOX] has 25 messages mentioned by SELECT
Host1: folder [INBOX] has 25 messages found by SEARCH ALL
Host1: folder [INBOX] has the same messages count (25) by SELECT and SEARCH ALL
Host2: checking if SEARCH ALL works on INBOX
Host2: folder [INBOX] has 32 messages mentioned by SELECT
Host2: folder [INBOX] has 32 messages found by SEARCH ALL
Host2: folder [INBOX] has the same messages count (32) by SELECT and SEARCH ALL
Good! SEARCH ALL works on both accounts.

Folders sizes before the synchronization.
You can remove foldersizes listings by using "--nofoldersizes" and "--nofoldersizesatend"
but then you will also lose the ETA (Estimation Time of Arrival) given after each message copy.
Host1 folder     1/5 [Drafts]                            Size:         0 Messages:     0 Biggest:         0
Host2 folder     1/5 [[Gmail]/Drafts]                    Size:         0 Messages:     0 Biggest:         0
Host2-Host1                                                            0               0                  0

Host1 folder     2/5 [INBOX]                             Size:    393251 Messages:    25 Biggest:     59437
Host2 folder     2/5 [INBOX]                             Size:    461389 Messages:    32 Biggest:     59437
Host2-Host1                                                        68138               7                  0

Host1 folder     3/5 [Sent]                              Size:         0 Messages:     0 Biggest:         0
Host2 folder     3/5 [[Gmail]/Sent Mail]                 Size:         0 Messages:     0 Biggest:         0
Host2-Host1                                                            0               0                  0

Host1 folder     4/5 [Trash]                             Size:         0 Messages:     0 Biggest:         0
Host2 folder     4/5 [[Gmail]/Bin]                       Size:         0 Messages:     0 Biggest:         0
Host2-Host1                                                            0               0                  0

Host1 folder     5/5 [spam]                              Size:         0 Messages:     0 Biggest:         0
Host2 folder     5/5 [[Gmail]/Spam]                      Size:         0 Messages:     0 Biggest:         0
Host2-Host1                                                            0               0                  0

Host1 Nb folders:                     5 folders
Host2 Nb folders:                     5 folders

Host1 Nb messages:                   25 messages
Host2 Nb messages:                   32 messages

Host1 Total size:                393251 bytes (384.034 KiB)
Host2 Total size:                461389 bytes (450.575 KiB)

Host1 Biggest message:            59437 bytes (58.044 KiB)
Host2 Biggest message:            59437 bytes (58.044 KiB)

Time spent on sizing:         2.4 seconds
++++ Looping on each one of 5 folders to sync
ETA: Sun May  3 12:08:06 2020  0 s  25/25 msgs left
Folder     1/5 [Drafts]                            -> [[Gmail]/Drafts]                   
Host1: folder [Drafts] has 0 messages in total (mentioned by SELECT)
Host2: folder [[Gmail]/Drafts] has 0 messages in total (mentioned by SELECT)
Host2: folder [[Gmail]/Drafts] permanentflags: 
Host1: Expunging Drafts 
Host1: folder [Drafts] considering 0 messages
Host2: folder [[Gmail]/Drafts] considering 0 messages
Host1: folder [Drafts] selected 0 messages, duplicates 0
Host2: folder [[Gmail]/Drafts] selected 0 messages, duplicates 0
Host1: Expunging folder Drafts 
ETA: Sun May  3 12:08:09 2020  2 s  25/25 msgs left
Folder     2/5 [INBOX]                             -> [INBOX]                            
Host1: folder [INBOX] has 25 messages in total (mentioned by SELECT)
Host2: folder [INBOX] has 32 messages in total (mentioned by SELECT)
Host2: folder [INBOX] permanentflags: 
Host1: Expunging INBOX 
Host1: folder [INBOX] considering 25 messages
Host2: folder [INBOX] considering 32 messages
Host1: folder [INBOX] selected 25 messages, duplicates 0
Host2: folder [INBOX] selected 32 messages, duplicates 0
Host1: Expunging folder INBOX 
ETA: Sun May  3 12:08:07 2020  0 s  0/25 msgs left
Folder     3/5 [Sent]                              -> [[Gmail]/Sent Mail]                
Host1: folder [Sent] has 0 messages in total (mentioned by SELECT)
Host2: folder [[Gmail]/Sent Mail] has 0 messages in total (mentioned by SELECT)
Host2: folder [[Gmail]/Sent Mail] permanentflags: 
Host1: Expunging Sent 
Host1: folder [Sent] considering 0 messages
Host2: folder [[Gmail]/Sent Mail] considering 0 messages
Host1: folder [Sent] selected 0 messages, duplicates 0
Host2: folder [[Gmail]/Sent Mail] selected 0 messages, duplicates 0
Host1: Expunging folder Sent 
ETA: Sun May  3 12:08:07 2020  0 s  0/25 msgs left
Folder     4/5 [Trash]                             -> [[Gmail]/Bin]                      
Host1: folder [Trash] has 0 messages in total (mentioned by SELECT)
Host2: folder [[Gmail]/Bin] has 0 messages in total (mentioned by SELECT)
Host2: folder [[Gmail]/Bin] permanentflags: 
Host1: Expunging Trash 
Host1: folder [Trash] considering 0 messages
Host2: folder [[Gmail]/Bin] considering 0 messages
Host1: folder [Trash] selected 0 messages, duplicates 0
Host2: folder [[Gmail]/Bin] selected 0 messages, duplicates 0
Host1: Expunging folder Trash 
ETA: Sun May  3 12:08:07 2020  0 s  0/25 msgs left
Folder     5/5 [spam]                              -> [[Gmail]/Spam]                     
Host1: folder [spam] has 0 messages in total (mentioned by SELECT)
Host2: folder [[Gmail]/Spam] has 0 messages in total (mentioned by SELECT)
Host2: folder [[Gmail]/Spam] permanentflags: 
Host1: Expunging spam 
Host1: folder [spam] considering 0 messages
Host2: folder [[Gmail]/Spam] considering 0 messages
Host1: folder [spam] selected 0 messages, duplicates 0
Host2: folder [[Gmail]/Spam] selected 0 messages, duplicates 0
Host1: Expunging folder spam 
ETA: Sun May  3 12:08:07 2020  0 s  0/25 msgs left
++++ End looping on each folder

Folders sizes after the synchronization.
You can remove this foldersizes listing by using  "--nofoldersizesatend"
Host1 folder     1/5 [Drafts]                            Size:         0 Messages:     0 Biggest:         0
Host2 folder     1/5 [[Gmail]/Drafts]                    Size:         0 Messages:     0 Biggest:         0
Host2-Host1                                                            0               0                  0

Host1 folder     2/5 [INBOX]                             Size:    393251 Messages:    25 Biggest:     59437
Host2 folder     2/5 [INBOX]                             Size:    461389 Messages:    32 Biggest:     59437
Host2-Host1                                                        68138               7                  0

Host1 folder     3/5 [Sent]                              Size:         0 Messages:     0 Biggest:         0
Host2 folder     3/5 [[Gmail]/Sent Mail]                 Size:         0 Messages:     0 Biggest:         0
Host2-Host1                                                            0               0                  0

Host1 folder     4/5 [Trash]                             Size:         0 Messages:     0 Biggest:         0
Host2 folder     4/5 [[Gmail]/Bin]                       Size:         0 Messages:     0 Biggest:         0
Host2-Host1                                                            0               0                  0

Host1 folder     5/5 [spam]                              Size:         0 Messages:     0 Biggest:         0
Host2 folder     5/5 [[Gmail]/Spam]                      Size:         0 Messages:     0 Biggest:         0
Host2-Host1                                                            0               0                  0

Host1 Nb folders:                     5 folders
Host2 Nb folders:                     5 folders

Host1 Nb messages:                   25 messages
Host2 Nb messages:                   32 messages

Host1 Total size:                393251 bytes (384.034 KiB)
Host2 Total size:                461389 bytes (450.575 KiB)

Host1 Biggest message:            59437 bytes (58.044 KiB)
Host2 Biggest message:            59437 bytes (58.044 KiB)

Time spent on sizing:         0.4 seconds
++++ Statistics
Transfer started on                     : Sun May  3 12:08:04 2020
Transfer ended on                       : Sun May  3 12:08:07 2020
Transfer time                           : 3.4 sec
Folders synced                          : 5/5 synced
Messages transferred                    : 0 
Messages skipped                        : 25
Messages found duplicate on host1       : 0
Messages found duplicate on host2       : 0
Messages found crossduplicate on host2  : 0
Messages void (noheader) on host1       : 0  
Messages void (noheader) on host2       : 0
Messages found in host1 not in host2    : 0 messages
Messages found in host2 not in host1    : 7 messages
Messages deleted on host1               : 0
Messages deleted on host2               : 0
Total bytes transferred                 : 0 (0.000 KiB)
Total bytes skipped                     : 393251 (384.034 KiB)
Message rate                            : 0.0 messages/s
Average bandwidth rate                  : 0.0 KiB/s
Reconnections to host1                  : 0
Reconnections to host2                  : 0
Memory consumption at the end           : 183.0 MiB (started with 159.8 MiB)
Load end is                             : 0.40 0.09 0.03 1/418 on 2 cores
Biggest message                         : 0 bytes (0.000 KiB)
Memory/biggest message ratio            : NA
Start difference host2 - host1          : 7 messages, 68138 bytes (66.541 KiB)
Final difference host2 - host1          : 7 messages, 68138 bytes (66.541 KiB)
The sync looks good, all 25 identified messages in host1 are on host2.
There is no unidentified message
The sync is not strict, there are 7 messages in host2 that are not on host1. Use --delete2 to delete them and have a strict sync. (32 identified messages in host2)
Detected 0 errors

This imapsync is up to date. ( local 1.983 >= official 1.977 )( Use --noreleasecheck to avoid this release check. )
Homepage: https://imapsync.lamiral.info/
Exiting with return value 0 (EX_OK: successful termination) 0/50 nb_errors/max_errors
"""


def imapsync(source_username, source_password, target_email):
    print(f'Received task with {source_username} {target_email}')
    time.sleep(10)
    return _example_out

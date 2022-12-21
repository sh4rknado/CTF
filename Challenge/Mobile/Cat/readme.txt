
File format:

file cat.ab
cat.ab: Android Backup, version 5, Compressed, Not-Encrypted

1. uncompress the android Backup

I use abe.jar for convert into tar format

java -jar /opt/HackingTools/Mobile/abe.jar unpack cat.ab cat.tar.gz
0% 1% 2% 3% 4% 5% 6% 7% 8% 9% 10% 11% 12% 13% 14% 15% 16% 17% 18% 19% 20% 21% 22% 23% 24% 25% 26% 27% 28% 29% 30% 31% 32% 33% 34% 35% 36% 37% 38% 39% 40% 41% 42% 43% 44% 45% 46% 47% 48% 49% 50% 51% 52% 53% 54% 55% 56% 57% 58% 59% 60% 61% 62% 63% 64% 65% 66% 67% 68% 69% 70% 71% 72% 73% 74% 75% 76% 77% 78% 79% 80% 81% 82% 83% 84% 85% 86% 87% 88% 89% 90% 91% 92% 93% 94% 95% 96% 97% 98% 99% 100% 
4853760 bytes written to cat.tar.gz.

file cat.tar.gz 
cat.tar.gz: POSIX tar archive

tar -xvf cat.tar.gz

# clean
rm cat.tar.gz

2. Show all files

.
├── apps
│   ├── com.android.basicsmsreceiver
│   │   └── _manifest
│   ├── com.android.bips
│   │   └── _manifest
│   ├── com.android.bluetoothmidiservice
│   │   └── _manifest
│   ├── com.android.bookmarkprovider
│   │   └── _manifest
│   ├── com.android.camera2
│   │   ├── _manifest
│   │   └── sp
│   │       └── com.android.camera2_preferences.xml
│   ├── com.android.captiveportallogin
│   │   └── _manifest
│   ├── com.android.carrierdefaultapp
│   │   └── _manifest
│   ├── com.android.contacts
│   │   ├── _manifest
│   │   └── sp
│   │       └── com.android.contacts.xml
│   ├── com.android.cts.ctsshim
│   │   └── _manifest
│   ├── com.android.cts.priv.ctsshim
│   │   └── _manifest
│   ├── com.android.dialer
│   │   ├── _manifest
│   │   └── sp
│   │       └── com.android.dialer_preferences.xml
│   ├── com.android.dreams.basic
│   │   └── _manifest
│   ├── com.android.egg
│   │   └── _manifest
│   ├── com.android.emergency
│   │   └── _manifest
│   ├── com.android.externalstorage
│   │   └── _manifest
│   ├── com.android.gallery3d
│   │   ├── _manifest
│   │   └── sp
│   │       └── com.android.gallery3d_preferences.xml
│   ├── com.android.htmlviewer
│   │   └── _manifest
│   ├── com.android.inputmethod.latin
│   │   ├── d_db
│   │   │   ├── pendingUpdates
│   │   │   ├── pendingUpdates.com.android.inputmethod.latin
│   │   │   ├── pendingUpdates.com.android.inputmethod.latin-shm
│   │   │   ├── pendingUpdates.com.android.inputmethod.latin-wal
│   │   │   ├── pendingUpdates-shm
│   │   │   └── pendingUpdates-wal
│   │   └── _manifest
│   ├── com.android.internal.display.cutout.emulation.corner
│   │   └── _manifest
│   ├── com.android.internal.display.cutout.emulation.double
│   │   └── _manifest
│   ├── com.android.internal.display.cutout.emulation.tall
│   │   └── _manifest
│   ├── com.android.launcher3
│   │   ├── _manifest
│   │   └── sp
│   │       └── com.android.launcher3.prefs.xml
│   ├── com.android.managedprovisioning
│   │   └── _manifest
│   ├── com.android.mtp
│   │   ├── db
│   │   │   ├── database
│   │   │   ├── database-shm
│   │   │   └── database-wal
│   │   └── _manifest
│   ├── com.android.pacprocessor
│   │   └── _manifest
│   ├── com.android.providers.downloads.ui
│   │   └── _manifest
│   ├── com.android.providers.partnerbookmarks
│   │   └── _manifest
│   ├── com.android.providers.telephony
│   │   └── _manifest
│   ├── com.android.proxyhandler
│   │   └── _manifest
│   ├── com.android.settings.intelligence
│   │   ├── _manifest
│   │   └── sp
│   │       ├── SuggestionEventStore.xml
│   │       └── suggestions.xml
│   ├── com.android.simappdialog
│   │   └── _manifest
│   ├── com.android.systemui.theme.dark
│   │   └── _manifest
│   ├── com.android.traceur
│   │   └── _manifest
│   ├── com.android.wallpaperbackup
│   │   ├── f
│   │   │   ├── empty
│   │   │   └── wallpaper-info-stage
│   │   └── _manifest
│   ├── com.android.wallpapercropper
│   │   └── _manifest
│   ├── com.android.wallpaper.livepicker
│   │   └── _manifest
│   ├── com.android.wallpaperpicker
│   │   └── _manifest
│   ├── com.example.android.notepad
│   │   └── _manifest
│   ├── com.example.android.rssreader
│   │   └── _manifest
│   ├── com.farmerbb.taskbar.androidx86
│   │   ├── _manifest
│   │   └── sp
│   │       └── com.farmerbb.taskbar.androidx86_preferences.xml
│   ├── com.google.android.backuptransport
│   │   └── _manifest
│   ├── com.google.android.ext.services
│   │   └── _manifest
│   ├── com.google.android.feedback
│   │   └── _manifest
│   ├── com.google.android.gms.setup
│   │   └── _manifest
│   ├── com.google.android.gsf.login
│   │   └── _manifest
│   ├── com.google.android.onetimeinitializer
│   │   ├── _manifest
│   │   └── sp
│   │       └── oti.xml
│   ├── org.android_x86.analytics
│   │   ├── f
│   │   │   ├── gaClientId
│   │   │   └── lastInfo.json
│   │   ├── _manifest
│   │   └── sp
│   │       └── org.android_x86.analytics.prefs.xml
│   └── org.lineageos.eleven
│       ├── db
│       │   ├── musicdb.db
│       │   ├── musicdb.db-shm
│       │   └── musicdb.db-wal
│       └── _manifest
├── cat.ab
├── readme.txt
└── shared
    └── 0
        ├── Alarms
        ├── DCIM
        ├── Download
        ├── Movies
        ├── Music
        ├── Notifications
        ├── Pictures
        │   ├── IMAG0001.jpg
        │   ├── IMAG0002.jpg
        │   ├── IMAG0003.jpg
        │   ├── IMAG0004.jpg
        │   ├── IMAG0005.jpg
        │   └── IMAG0006.jpg
        ├── Podcasts
        └── Ringtones


the backup is composed of 2 parts:
    apps: data of the installed apps
    shared: internal SDCARD (internal memory)


shared
    └── 0
        ├── Pictures
        │   ├── IMAG0001.jpg
        │   ├── IMAG0002.jpg
        │   ├── IMAG0003.jpg
        │   ├── IMAG0004.jpg
        │   ├── IMAG0005.jpg
        │   └── IMAG0006.jpg


After search into the photo we see the flag on the IMAG0004.jpg into the confidential document (at the end of the document)

HTB{ThisBackupIsUnprotected}

## Ressources
    abe.jar: https://github.com/nelenkov/android-backup-extractor/releases

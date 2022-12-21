Tools used:
    -> apkstudio
    -> apktool
    -> jadx
    -> adb-tools

1. Decompile the apk from jadx-gui or apk-studio

2. Check the mainActivity (sources/com/AwesomeProject/mainActivity.java)

from this point you see an implementation of com.facebook.react.ReactActivity

import com.facebook.react.ReactApplication;
public class MainApplication extends Application implements ReactApplication

3. Check the ReactApplication (com.facebook.react.ReactActivity).

public abstract class ReactNativeHost {
    protected String getBundleAssetName() {
        return "index.android.bundle";
    }

We see that the bundle used is index.android.bundle

4. Open the files  (Ressources/assets/index.android.bundle)

__d(function(g,r,i,a,m,e,d){Object.defineProperty(e,"__esModule",{value:!0}),e.myConfig=void 0;var t={importantData:"baNaNa".toLowerCase(),apiUrl:'https://www.hackthebox.eu/',debug:'SFRCezIzbTQxbl9jNDFtXzRuZF9kMG43XzB2MzIyMzRjN30='};e.myConfig=t},400,[]);

this line use an data SFRCezIzbTQxbl9jNDFtXzRuZF9kMG43XzB2MzIyMzRjN30=.


5. Identify the cipher of the data

-> I use an online cipher identifier / base64 decoder (https://www.dcode.fr/cipher-identifier).
-> the dection of the cipher is an base64 i will use now oneline base64 decoder (https://www.dcode.fr/base-64-encoding)

FLAG is HTB{23m41n_c41m_4nd_d0n7_0v32234c7}


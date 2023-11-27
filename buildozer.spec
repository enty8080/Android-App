[app]

title = Pwny

package.name = pwny
package.domain = org.entysec

source.dir = .
source.include_exts = py,pyc,pyo,png,jpg,kv,atlas
source.exclude_dirs = python-for-android, bin

version = 0.1
orientation = landscape

osx.python_version = 3
osx.kivy_version = 1.9.1

fullscreen = 0

android.arch = armeabi-v7a
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,VIBRATE,CAMERA,READ_CONTACTS,GET_ACCOUNTS,RECORD_AUDIO,READ_PHONE_STATE,READ_CALL_LOG,WRITE_CALL_LOG,CALL_PHONE,CALL_PRIVILEGED,USE_SIP,PROCESS_OUTGOING_CALLS,ADD_VOICEMAIL,READ_SMS,SEND_SMS,RECEIVE_SMS,RECEIVE_MMS,RECEIVE_WAP_PUSH,CHANGE_CONFIGURATION,CHANGE_NETWORK_STATE,CHANGE_WIFI_MULTICAST_STATE,CHANGE_WIFI_STATE,CLEAR_APP_CACHE,CONTROL_LOCATION_UPDATES,DELETE_PACKAGES,DUMP,FACTORY_TEST,FLASHLIGHT,GLOBAL_SEARCH,KILL_BACKGROUND_PROCESSES,MANAGE_DOCUMENTS,MEDIA_CONTENT_CONTROL,MODIFY_AUDIO_SETTINGS,NFC,ACCESS_COARSE_LOCATION,ACCESS_FINE_LOCATION,ACCESS_LOCATION_EXTRA_COMMANDS,ACCOUNT_MANAGER,BLUETOOTH_ADMIN,BLUETOOTH,BLUETOOTH_PRIVILEGED,ACCESS_NETWORK_STATE
android.whitelist = lib-dynload/termios.so,lib-dynload/mmap.so,lib-dynload/_json.so,lib-dynload/pyexpat.so

p4a.source_dir = python-for-android
p4a.local_recipes = python-for-android/pythonforandroid/recipes
p4a.branch = develop
p4a.bootstrap = badservice

log_level = 2
warn_on_root = 0
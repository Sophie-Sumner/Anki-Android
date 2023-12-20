# bug reproduction script for bug #13717 of ankidroid
import sys
import time

import uiautomator2 as u2


def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)


    d.app_start("com.ichi2.anki")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "com.ichi2.anki":
            break
        time.sleep(2)
    wait()

    out = d(resourceId="com.ichi2.anki.debug:id/fab_main").click()
    if not out:
        print("Success: click +")
    wait()

    out = d(resourceId="com.ichi2.anki.debug:id/add_deck_action").click()
    if not out:
        print("Success: click create deck")
    wait()

    out = d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_2_3"]/android.widget.TextView[1]').click()
    if not out:
        print("Success: input ' ")
    wait()

    out = d(resourceId="com.ichi2.anki.debug:id/md_button_positive", text="OK").click()
    if not out:
        print("Success: click OK")
    wait()

    out = d(resourceId="com.ichi2.anki.debug:id/fab_main").click()
    if not out:
        print("Success: click + ")
    wait()

    out = d(resourceId="com.ichi2.anki.debug:id/add_note_action").click()
    if not out:
        print("Success: click add")
    wait()

    out = d(resourceId="com.ichi2.anki.debug:id/action_save")
    if not out:
        print("Success: add note to deck ' ")
    wait()

    out = d.xpath('//*[@resource-id="com.ichi2.anki.debug:id/files"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').long_click()
    if not out:
        print("Success: longclick the deck ' ")
    wait()

    out = d(resourceId="com.ichi2.anki.debug:id/md_title", text="Export deck").click()
    if not out:
        print("Success: click Export deck")
    wait()

    out = d(resourceId="com.ichi2.anki.debug:id/md_button_positive", text="OK").click()
    if not out:
        print("Success: click OK")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
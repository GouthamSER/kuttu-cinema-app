# Kuttu Cinema

Android app for the [KuttuBot](https://github.com/GouthamSER) movie website.
It is a thin Capacitor shell that opens the live site (`https://kuttu-bot.koyeb.app`) full screen.
Website updates show up in the app instantly, with no new APK.

- Search, posters, quality / language / season filters: same as the website
- "Get on Telegram" buttons open the Telegram app (via `telegram.dog`)
- Offline / sleeping-server page with a retry button

## Get the APK
1. Push this repo to GitHub.
2. **Actions → Build APK → Run workflow** (it also runs on every push to `main`).
3. Download `KuttuCinema-apk` from the run, unzip, install `KuttuCinema.apk`.

For a public download link: `git tag v1.0.0 && git push --tags`. The APK is attached to the GitHub Release.

## Change the site address
Edit `server.url` and `allowNavigation` in `capacitor.config.json`, then push.

## Build locally (optional)
Needs Node 18+, JDK 17, Android SDK.
```
npm install
npm run icons
npx cap add android
npx capacitor-assets generate --android
npx cap sync android
cd android && ./gradlew assembleDebug
```
APK: `android/app/build/outputs/apk/debug/app-debug.apk`

Debug-signed APK is fine for sharing directly. A Play Store release would need your own keystore.

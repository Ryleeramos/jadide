# Vega packaged distribution

This build packages the Python application in `core.pkg` (zlib/Base85) and the Jinja HTML templates in `ui.pkg` (ZIP/Deflate). `app.py` is a small loader. This is **reversible code obfuscation**, not encryption, traffic encryption or DPI evasion. Browser-visible HTML, JavaScript, response bodies, public URLs and standard protocol identifiers remain observable.

## Deploy

Build using the provided `Dockerfile`, or install `requirements.txt` then run `python app.py`. Python 3.10+ is required. Configure admin credentials via `ADMIN_USER` and `ADMIN_PASS` and configure `SECRET_KEY` securely. Ensure the persistent data directory has appropriate permissions.

The source installation's `obfuscation.json` is retained to preserve existing transport paths. Do not set `VEGA_REGEN_PATHS=1` on an existing deployment unless you intend to invalidate previously issued links. Panel route and any newly generated values are persisted in the configured data directory.

For testing only: `python -m py_compile app.py`; this checks the loader, not the decoded application. The package was additionally checked by compiling the decoded application and parsing the bundled Jinja templates.

## Limitations

* This is primarily source-code packaging; it does not disguise the protocol on the wire.
* The runtime must reconstruct readable code in memory. Do not treat code obfuscation as a security boundary.
* A fresh secret key is generated automatically if it is absent. For production, supply `SECRET_KEY` as a secret or ensure persistent storage.
* Protocol names, client configuration formats, route parameters and infrastructure-level references are unchanged to avoid breaking compatibility.
* If using an existing installation, back up its data, user database, keys and settings before replacing files.
* Default admin credentials in the upstream source are insecure; set secure `ADMIN_USER` and `ADMIN_PASS` before exposing this service.

## Files

* `app.py` — entrypoint and decoder.
* `core.pkg` — reversible encoded application source.
* `ui.pkg` — compressed HTML templates.
* `static/` — publicly served CSS and images, retained unchanged.
* `Dockerfile` — original container setup.
* `obfuscation.json` — pre-existing transport-path configuration, retained for compatibility.


## Fixed admin URL

The login page is available at `https://YOUR-DOMAIN/dash/login`.
The admin interface uses `/dash` for all internal pages. Existing data/obfuscation.json panel tokens do not override this route.
Other transport and subscription paths are unchanged.
Keep strong admin credentials and HTTPS; a predictable path is not an access control.


# Crop+Send Arxiv Papers to your Remarkable with one click.

This is a bookmarklet that calls a local python server that downloads, crops and sends the file. You need to have a couple of things locally, namely

```
ghostscript (sudo apt-get install ghostscript)
rmapi (go get -u github.com/juruen/rmapi)
```

Once you have those, you need to connect `rmapi`, do that by running it+following the instructions.

The python dependencies are managed with `pipenv` so running `pipenv install` sets you up.

After that's done, you can do `pipenv run service.py` and navigate to `{wherever this is}/js/dist/test-page.html` from where you can copy the bookmarklet into your browser's toolbar.

"That's it" (lol this is a pain for functionality that should be out-of-the-box)

If you want to make sure the service is always running, then start it on startup.

The libraries that do all the hard work are `rmapi` and `pdfCropMargins`, which more or less rock. 


# Crop+Send Arxiv Papers to your Remarkable with one click.

This is a one-click bookmarklet that calls a local python server that downloads, crops and sends the file. Cropping takes ~10 seconds or so.

You need to have a couple of things locally, namely

```
ghostscript (sudo apt-get install ghostscript)
rmapi (go get -u github.com/juruen/rmapi)
```

Once you have those, you need to connect `rmapi`, do that by running it+following the instructions.

The python dependencies are managed with `pipenv` so running `pipenv install` sets you up.

The bookmarklet itself is built with `gulp`, so you can do 
```
cd js && npm install && npm run gulp
```
To build the `dist` folder with the bookmarklet.

After that's done, you can do `pipenv run service.py` and navigate to `{wherever this is}/js/dist/test-page.html` from where you can copy the bookmarklet into your browser's toolbar.

"That's it" (lol this is a pain for functionality that should be out-of-the-box)

If you want to make sure the service is always running, then start it on startup. I do this with a crontab
`crontab -e` to edit them, then add the line
```
@reboot sudo -H -u {your user name} {path to this}/run-service &
```
However note that fiddling with an @reboot crontab is a *classic* way to boot-cycle / brick your laptop, so proceed with caution.

The libraries that do all the hard work are `rmapi` and `pdfCropMargins`, which more or less rock. 

security - hideously insecure I imagine. Apart from anything else, there's a shell injection from arxiv titles that would be hilarious to execute.

This software is provided without warranty, implicit or otherwise.
